<template>
  <div class="PlaceDetailView">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card" style="width: auto">
          <div class="card-body">
            <p>ID de la place : {{ place.id }}</p>
            <h5 class="card-title">{{ place.name }}</h5>
            <p class="card-text">
              {{ place.street }} {{ place.number }} <br />
              {{ place.postal_code }} {{ place.locality }}
            </p>
            <div v-if="user">
              <p>Vous êtes connecté en tant que {{ user.username }}</p>
              <p>{{ this.user.pk }}</p>
              <h2>Comment on this post</h2>
              <form>
                <textarea v-model="newComment"></textarea>
                <br />
                <button @click="postComment()">Envoyer</button>
              </form>

              <ul>
                <li v-for="comment in comments" :key="comment.id">
                  "{{ comment.text }}" Posted by : {{ comment.user.username }}
                  <br />
                  {{ formatDate(comment.created_at) }}
                  {{ formatTime(comment.created_at) }}
                </li>
              </ul>

              <h2>Rate this place</h2>
              <form>
                <input type="number" v-model="rating" min="0" max="5" step="0.1" />
                <br />
                <button @click="postRating()" :disabled="alreadyRated">Submit rating</button>
              </form>
            </div>
            <div v-else>
              <p>Need to be logged to post a comment</p>
            </div>
            <!-- Formulaire d'évaluation -->

            <!-- Vous pouvez afficher plus d'informations sur l'endroit ici -->
            <button class="transparent-button" style="margin-left: 10px" @click="shareOnTwitter">
              <span><font-awesome-icon icon="fa-brands fa-twitter" class="icon main-color"/></span>
            </button>

            <br />
            <br />
            <button class="transparent-button" style="margin-left: 10px" @click="shareOnFacebook">
              <font-awesome-icon icon="fa-brands fa-facebook" class="icon main-color" />
            </button>

            <br />
            <br />
            <button class="transparent-button" style="margin-left: 10px" @click="shareOnWhatsapp">
              <font-awesome-icon icon="fa-brands fa-whatsapp" class="icon main-color" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import authService from "../services/authService"
import placeService from "../services/placeService"
import commmentService from "../services/commentService"
// import api from "../services/api"
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome"
import { library } from "@fortawesome/fontawesome-svg-core"
import { faUserSecret } from "@fortawesome/free-solid-svg-icons"
import { faTwitter } from "@fortawesome/free-brands-svg-icons"
import { faFacebook } from "@fortawesome/free-brands-svg-icons"
import { faWhatsapp } from "@fortawesome/free-brands-svg-icons"
library.add(faUserSecret, faTwitter, faFacebook, faWhatsapp)

export default {
  data() {
    return {
      error: null,
      places: [],
      place: "",
      newComment: "",
      placeId: "",
      userId: "",
      token: "",
      comments: [],
      postedby: "",
      rating: "",
      alreadyRated: false
    }
  },
  async mounted() {
    this.placeId = this.$route.params.id
    this.fetchPlace(this.placeId)
    this.userId = this.user.pk
    this.token = localStorage.getItem("access_token")
    this.comments = await commmentService.fetchCommentsByPlaceId(this.placeId)
  },
  computed: {
    user() {
      return authService.user.value
    }
  },
  methods: {
    logout() {
      authService.logout()
    },
    placeURL(id) {
      return "http://localhost:8000/#/place-detail/" + id
    },
    async fetchPlace(id) {
      const response = await placeService.fetchPlaceDetail(id)
      this.place = response.data
    },
    async postComment() {
      await placeService.postCommentOnPlace(this.placeId, this.newComment, this.token)
      this.newComment = ""
      this.comments = await commmentService.fetchCommentsByPlaceId(this.placeId)
    },
    formatDate(date) {
      return new Date(date).toLocaleDateString("fr-CH", {
        year: "numeric",
        month: "long",
        day: "numeric"
      })
    },
    formatTime(date) {
      return new Date(date).toLocaleTimeString("fr-CH", {
        hour: "numeric",
        minute: "numeric"
      })
    },
    shareOnWhatsapp() {
      let message = `Check out this awesome place: ${this.place.name} - ${this.placeURL(
        this.place.id
      )}`
      let whatsappUrl = `https://wa.me/?text=${encodeURIComponent(message)}`
      window.location.href = whatsappUrl
    },
    shareOnFacebook() {
      let url = this.placeURL(this.place.id)
      let facebookUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`
      window.location.href = facebookUrl
    },
    shareOnTwitter() {
      let url = this.placeURL(this.place.id)
      let text = `${this.place.name} - Check out this place!`
      let twitterUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(
        url
      )}&text=${encodeURIComponent(text)}&via=qarbon`
      window.location.href = twitterUrl
    }
  },
  components: {
    FontAwesomeIcon
  }
}
</script>

<style scoped>
.transparent-button {
  background: none;
  border: none;
  padding: 0;
  margin: 0;
}

.transparent-button:focus {
  outline: none;
}

.text {
  color: #ffffff;
}

.col-md-4 {
  padding-left: 15px;
  padding-right: 15px;
  margin-bottom: 30px;
}

.col-md-6 {
  padding-left: 15px;
  padding-right: 15px;
  margin-bottom: 30px;
}

.card {
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  transition: box-shadow 0.5s;
  width: auto;
}

.card:hover {
  box-shadow: 0 4px 8px grey;
}

.card-body {
  flex-grow: 1;
}

.card-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
  padding: 10px;
}

.w-100 {
  align-items: end;
  align-content: center;
}

.card-text {
  font-size: 16px;
}

.PlaceDetailView {
  padding-top: 110px;
}

.main-color {
  color: var(--main-color);
}

.icon {
  font-size: 30px;
  margin: 10px;
}
</style>
