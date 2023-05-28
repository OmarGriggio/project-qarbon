<template>
  <div class="PlaceView">
    <div v-if="error">
      <p>Une erreur est survenue: {{ error }}</p>
    </div>
    <div v-else>
      <h2 style="padding-bottom: 30px;">PLACES</h2>
      <div class="container row-lg-4">
        <div class="card-display">
          <div v-for="place in places" :key="place.id">
            <div class="card" style="width: 18rem">
              <!-- <img src="..." class="card-img-top" alt="..." />-->
              <div class="card-body">
                <h5 class="card-title">{{ place.name }}</h5>
                <p class="card-text">
                  {{ place.street }} {{ place.number }} <br />
                  {{ place.postal_code }} {{ place.locality }}
                </p>
                <RouterLink :to="'/place-detail/' + place.id">
                  <button class="buttonSee">See more</button>
                </RouterLink>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import authService from "../services/authService"
import axios from "axios"

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
    components: {}
  }
}
</script>

<style scoped>
.card-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
}
.card-display {
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  gap: 25px;
}
.PlaceView{
  padding-top: 120px;
}
.buttonSee {
  padding: 0.9em 1em;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 500;
  color: #000;
  background-color: #fff;
  border: none;
  border-radius: 45px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
}

.buttonSee:hover {
  background-color: #23c483;
  box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4);
  color: #fff;
  transform: translateY(-7px);
}

.buttonSee:active {
  transform: translateY(-1px);
}
</style>
