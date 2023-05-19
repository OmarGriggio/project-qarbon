import api from "@/services/api"
import { ref } from "vue"

// it would be better to store refresh token and then use it to get a new access token
export const LOCALSTORARGE_TOKEN_KEY = "access_token"
export const LOCALSTORARGE_REFRESH_TOKEN_KEY = "refresh_token"
export const LOCALSTORAGE_TOKEN_TIMESTRAMP = "tokenTimestamp"

let access_token = localStorage.getItem(LOCALSTORARGE_TOKEN_KEY)
let refresh_token = localStorage.getItem(LOCALSTORARGE_REFRESH_TOKEN_KEY)
let timestamp_token = localStorage.getItem(LOCALSTORAGE_TOKEN_TIMESTRAMP)
let user = ref()

api.interceptors.request.use((config) => {
  if (access_token) {
    config.headers["Authorization"] = `Bearer ${access_token}`
  }
  return config
})

api.interceptors.response.use(null, (error) => {
  // Ensure error.response exists before deconstructing it
  if (error.response) {
    const { status } = error.response
    const originalRequest = error.config
    // Check for 401 status
    if (status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      return api
        .post("dj-rest-auth/token/refresh/", { refresh: refresh_token })
        .then((response) => {
          if (response.status === 201) {
            access_token = response.data.access_token
            localStorage.setItem(LOCALSTORARGE_TOKEN_KEY, access_token)

            refresh_token = response.data.refresh_token
            localStorage.setItem(LOCALSTORARGE_REFRESH_TOKEN_KEY, refresh_token)

            localStorage.setItem(LOCALSTORAGE_TOKEN_TIMESTRAMP, Date.now().toString())
            api.defaults.headers.common["Authorization"] = "Bearer " + access_token
            return api(originalRequest)
          }
        })
        .catch((refreshError) => {
          console.error("Refresh token error:", refreshError)
          return Promise.reject(refreshError)
        })
    }
    // Check for 403 status
    if (status === 403 && !originalRequest._retry) {
      // Handle 403 error here
      console.error("403 Forbidden Error:", error)
    }
    // If status is neither 401 nor 403, or request was retried, reject the promise
    console.error("API Error:", error)
    return Promise.reject(error)
  }

  // If error.response is undefined, log a custom error message
  console.error("Unexpected Error:", error)
  return Promise.reject(error)
})

export default {
  user,
  login(payload) {
    if (!payload.username || !payload.password) {
      return Promise.reject("Username and password are required.")
    }

    return api.post(`dj-rest-auth/login/`, payload).then((response) => {
      access_token = response.data.access_token
      refresh_token = response.data.refresh_token
      localStorage.setItem(LOCALSTORARGE_TOKEN_KEY, access_token)
      localStorage.setItem(LOCALSTORARGE_REFRESH_TOKEN_KEY, refresh_token)
      localStorage.setItem(LOCALSTORAGE_TOKEN_TIMESTRAMP, Date.now().toString())
      user.value = response.data.user
      return response.data.user
    })
  },
  logout() {
    return api.post(`dj-rest-auth/logout/`).then((response) => {
      access_token = undefined
      localStorage.removeItem(LOCALSTORARGE_TOKEN_KEY)
      localStorage.removeItem(LOCALSTORARGE_REFRESH_TOKEN_KEY)
      localStorage.removeItem(LOCALSTORAGE_TOKEN_TIMESTRAMP)
      user.value = undefined
      return response.data
    })
  },
  register(payload) {
    if (!payload.username || !payload.password1 || !payload.password2) {
      return Promise.reject("Username and password1 and password2 are required.")
    }

    return api.post(`dj-rest-auth/registration/`, payload).then((response) => {
      access_token = response.data.access_token
      user.value = response.data.user
      return response.data.user
    })
  },
  // allows to relogin with saved token
  getUser() {
    return api.get(`dj-rest-auth/user/`).then((response) => {
      user.value = response.data
      console.log(user.value)
    })
  },
  checkTokenExpiry() {
    const tokenTimestamp = parseInt(localStorage.getItem(LOCALSTORAGE_TOKEN_TIMESTRAMP))
    const refreshExpiryTime = 24 * 60 * 60 * 1000 // Refresh token lifetime

    if (Date.now() - tokenTimestamp > refreshExpiryTime) {
      // The tokens have expired, clear them
      localStorage.removeItem(LOCALSTORARGE_TOKEN_KEY)
      localStorage.removeItem(LOCALSTORARGE_REFRESH_TOKEN_KEY)
      localStorage.removeItem(LOCALSTORAGE_TOKEN_TIMESTRAMP)
    }
  }
}
