import api, { apiImage } from "./api"

export default {
  async postCommentOnPlace(id, comment, token) {
    const headers = { Authorization: `Bearer ${token}` }
    try {
      await api.post(`places/${id}/add_comment/`, { text: comment }, { headers })
    } catch (err) {
      throw err.response.data
    }
  },
  fetchPlaces() {
    return api.get(`places/`)
  },
  fetchPlaceDetail(id) {
    return api.get(`/places/${id}/`)
  },

  async createPlace(place, token) {
    const headers = { Authorization: `Bearer ${token}` }
    const formData = new FormData()
    for (let key in place) {
      formData.append(key, place[key])
    }
    try {
      await apiImage.post("/places/", formData, { headers })
    } catch (err) {
      throw err.response.data
    }
  },
}
