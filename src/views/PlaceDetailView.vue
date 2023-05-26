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
          <!-- Vous pouvez afficher plus d'informations sur l'endroit ici -->
        </div>
      </div>
      <button>
        <font-awesome-icon icon="fa-brands fa-twitter" />
        <ShareNetwork
          network="twitter"
          :url="placeURL(place.id)"
          :title="place.name"
          description="Check out this place!"
          twitter-user="qarbon"
        >
          <span>Share on Twitter</span>
        </ShareNetwork>
      </button>
      <br />
      <button>
        <font-awesome-icon icon="fa-brands fa-facebook" />
        <ShareNetwork
          network="facebook"
          :url="placeURL(place.id)"
          :title="place.name"
          description="This is an awesome event !"
        >
          <span>Share on Facebook</span>
        </ShareNetwork>
      </button>
      <br />
      <button>
        <font-awesome-icon icon="fa-brands fa-whatsapp" />
        <ShareNetwork
          network="whatsapp"
          :url="placeURL(place.id)"
          :title="place.name"
          description="This is an awesome event !"
        >
          <span>Share on WhatsApp</span>
        </ShareNetwork>
      </button>
    </div>
  </div>
</template>

<script>
import authService from "../services/authService"
// import api from "../services/api"
import axios from "axios"
import { ShareNetwork } from "vue-social-sharing"

export default {
  data() {
    return {
      error: null,
      places: [],
      place: []
    }
  },
  async mounted() {
    const placeId = this.$route.params.id // Supposons que vous récupérez l'ID de la place à partir des paramètres d'URL
    try {
      const response = await axios.get(`http://localhost:8000/api/places/${placeId}/`)
      this.place = response.data
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
      return "http://localhost:8000/#/place-detail/" + id
    }
  },
  components: {
    ShareNetwork
  }
}
</script>

<style>
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
}

.w-100 {
  align-items: end;
  align-content: center;
}

.card-text {
  font-size: 16px;
}
</style>
