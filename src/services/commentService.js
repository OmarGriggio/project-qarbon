import api from "@/services/api"

export default {
  fetchComments() {
    return api.get(`comments/`).then((response) => response.data)
  },
  async postComments(placeId, userId, token, commentText) {
    const headers = { Authorization: `Bearer ${token}` }
    const commentData = {
      place: placeId, 
      user: userId, 
      text: commentText 
    }
    try {
      await api.post("comments/", commentData, { headers })
    } catch (err) {
      throw err.response.data
    }
  },
  async fetchCommentsByPlaceId(placeId) {
    return api.get(`comments/?place=${placeId}`).then((response) => response.data)
  }
}

