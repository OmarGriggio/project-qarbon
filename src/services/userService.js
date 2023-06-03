import api from "@/services/api"

export default {
  fetchUserByUsername(username) {
    return api.get(`users/?username=${username}`)
  }
}
