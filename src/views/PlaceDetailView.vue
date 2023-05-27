<template>
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
              <button @click="postComment()">Envoyer</button>
            </form>

            <ul>
              <li v-for="comment in comments" :key="comment.id">
                {{ comment.text }}
              </li>
            </ul>
          </div>
          <div v-else>
            <p>Need to be logged to post a comment</p>
          </div>
          <!-- Formulaire d'évaluation -->

          <!-- Vous pouvez afficher plus d'informations sur l'endroit ici -->
          <ShareNetwork
            network="twitter"
            :url="placeURL(place.id)"
            :title="place.name"
            description="Check out this place!"
            twitter-user="qarbon"
          >
            <button class="btn btn-primary" style="margin-left: 10px">
              <span><font-awesome-icon icon="fa-brands fa-twitter" /></span>
            </button>
          </ShareNetwork>
          <br />
          <br />
          <ShareNetwork
            network="facebook"
            :url="placeURL(place.id)"
            :title="place.name"
            description="This is an awesome event !"
          >
            <button class="btn btn-primary" style="margin-left: 10px">
              <span><font-awesome-icon icon="fa-brands fa-facebook" class="text" /></span>
            </button>
          </ShareNetwork>
          <br />
          <br />
          <ShareNetwork
            network="whatsapp"
            :url="placeURL(place.id)"
            :title="place.name"
            description="This is an awesome event !"
          >
            <button class="btn btn-primary" style="margin-left: 10px">
              <span><font-awesome-icon icon="fa-brands fa-whatsapp" /></span>
            </button>
          </ShareNetwork>
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
import { ShareNetwork } from "vue-social-sharing"
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
      comments: []
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
    }
  },
  components: {
    ShareNetwork,
    FontAwesomeIcon
  }
}
</script>

<style>
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
</style>
