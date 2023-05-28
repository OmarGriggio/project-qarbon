import axios from "axios"

const api = axios.create({
  baseURL: "http://localhost:8000/api",
  timeout: 5000,
  headers: {
    "Content-Type": "application/json"
  }
  // withCredentials: true
})

const apiImage = axios.create({
  baseURL: "http://localhost:8000/api",
  timeout: 5000,
  headers: {
    "Content-Type": "multipart/form-data"
  }
  // withCredentials: true
})

export { apiImage }
export default api
