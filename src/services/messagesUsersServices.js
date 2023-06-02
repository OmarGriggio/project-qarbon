import api from "@/services/api"

export default {
  fetchMessagesUsers() {
    return api.get(`messagesusers/`).then((response) => response.data)
  },
  async postMessage(token, id) {
    const headers = { Authorization: `Bearer ${token}` }
    try {
      await api.delete(`/messagesusers/${id}/send_message/`, { headers })
    } catch (err) {
      throw err.response.data
    }
  },
  fetchMessagesUsersDetail(id) {
    return api.get(`messagesusers/?sender=${id}/`).then((response) => response.data)
  }
}