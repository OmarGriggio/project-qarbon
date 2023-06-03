import api from "@/services/api"

export default {
  fetchUserByUsername(username) {
    return api.get(`users/get_user/?username=${username}`).then((response) => response.data)
  }
}
