import api from "@/services/api"

export default {
  async postCommentOnPlace(id, comment, token) {
    const headers = { Authorization: `Bearer ${token}` }
    try {
      await api.post(`/places/${id}/comments/`, { text: comment }, { headers })
    } catch (err) {
      throw err.response.data
    }
  },
  fetchPlaces() {
    return api.get(`places/`)
  },
  fetchPlaceDetail(id) {
    return api.get(`/places/${id}/`)
  }
}
