<template>
  <div class="row justify-content-center">
    <div class="col-md-6">
      <div class="card" style="width: auto">
        <div class="card-body">
          <p>ID de la event : {{ event.id }}</p>
          <h5 class="card-title">{{ event.name }}</h5>
          <p class="card-text">
            
          </p>
          <!-- Vous pouvez afficher plus d'informations sur l'endroit ici -->
          <ShareNetwork
            network="twitter"
            :url="placeURL(event.id)"
            :title="event.name"
            description="Check out this event!"
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
            :url="placeURL(event.id)"
            :title="event.name"
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
            :url="placeURL(event.id)"
            :title="event.name"
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
// import api from "../services/api"
import axios from "axios"
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
      events: [],
      event: []
    }
  },
  async mounted() {
    const eventId = this.$route.params.id // Supposons que vous récupérez l'ID de la place à partir des paramètres d'URL
    try {
      const response = await axios.get(`http://localhost:8000/api/events/${eventId}/`)
      this.event = response.data
    } catch (err) {
      this.error = err.response.data
    }
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
      return "http://localhost:8000/#/event-detail/" + id
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
