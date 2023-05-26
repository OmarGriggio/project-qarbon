<template>
  <div>
    <div v-if="error">
      <p>Une erreur est survenue: {{ error }}</p>
    </div>
    <div v-else>
      <h2 style="margin-bottom: 30px; margin-top: 30px">PLACES</h2>
      <div class="row justify-content-center">
        <div v-for="place in places" :key="place.id" class="col-md-6">
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
            <div>
              <RouterLink :to="'/place-detail/' + place.id">
                <button class="btn btn-primary" @click="storePlace(place)">See more</button>
              </RouterLink>
            </div>
          </div>
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
      places: []
    }
  },
  async mounted() {
    try {
      this.places = await axios
        .get("http://localhost:8000/api/places/")
        .then((response) => response.data)
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
    storeEvent(event) {
      sessionStorage.setItem("place", JSON.stringify(event))
    },
    components: {
      ShareNetwork,
      FontAwesomeIcon
    }
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
