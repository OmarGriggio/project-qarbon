<template>
  <div class="row justify-content-center">
    <div class="col-md-4">
      <div class="card">
        <img :src="event.image" alt="event image" class="card-img-top" />
        <div class="card-body">
          <ul class="list-group list-group-flush">
            <li class="list-group-item">
              <h5 class="card-title" style="color: var(--main-color)">
                {{ event.name }}
              </h5>
            </li>
            <br />
            <li class="list-group-item">
              <h5 class="card-subtitle">
                {{ event.description }}
              </h5>
              <br />
              <p class="subtitle-text"></p>
            </li>
            <li class="list-group-item" style="margin-top: 10px">
              <h5 class="card-subtitle">
                {{ getPlace(event.place).name }}
              </h5>
              <p class="subtitle-text">
                {{ getPlace(event.place).street }}, {{ getPlace(event.place).number }}
              </p>
              <p class="subtitle-text" style="margin-top: -15px">
                {{ getPlace(event.place).postal_code }}
                {{ getPlace(event.place).locality }}
              </p>
              <p class="subtitle-text" style="margin-top: 0px">
                {{ formatDate(event.date) }} -
                {{ formatTime(event.date) }}
              </p>
            </li>
            <li class="list-group-item" style="margin-top: 10px">
              <p class="card-subtitle">
                Number of participants : 
                {{ participants.length }} / 
                {{ event.capacity }}
              </p>
            </li>
            <div v-if="user">
              <li class="list-group-item" style="margin-top: 10px">
                <button
                  v-if="!isUserRegistered(participants) && !isEventFull(event, participants)"
                  @click="registerForEvent(event.id)"
                  class="buttonSee"
                >
                  Register
                </button>
                <p v-else-if="isUserRegistered(participants)" class="text">You are already registered</p>
                <p v-else class="text">The event is full</p>
              </li>
            </div>
            <div v-else class="text">
              <p>You need to be logged in to register</p>
            </div>
            <li class="list-group-item" style="margin-top: 10px">
              <div class="d-flex justify-content-evenly">
                <button class="transparent-button" @click="shareOnTwitter">
                  <span
                    ><font-awesome-icon icon="fa-brands fa-twitter" class="icon main-color"
                  /></span>
                </button>

                <button class="transparent-button" @click="shareOnFacebook">
                  <font-awesome-icon icon="fa-brands fa-facebook" class="icon main-color" />
                </button>

                <button
                  class="transparent-button"
                  style="margin-left: 10px"
                  @click="shareOnWhatsapp"
                >
                  <font-awesome-icon icon="fa-brands fa-whatsapp" class="icon main-color" />
                </button>
              </div>
            </li>
          </ul>
          <!-- Vous pouvez afficher plus d'informations sur l'événement ici -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import authService from "../services/authService"
import eventService from "../services/eventService"
import placeService from "../services/placeService"
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
      event: [],
      //place: [],
      places: [],
      userPublisher: "",
      userCo: "",
      participants: []
    }
  },
  async mounted() {
    const eventId = this.$route.params.id
    this.fetchEvent(eventId)
    const resp = await placeService.fetchPlaces()
    this.places = resp.data
  },
  computed: {
    user() {
      return authService.user.value ? authService.user.value : null
    }
  },
  methods: {
    logout() {
      authService.logout()
    },
    eventUrl(id) {
      return "http://localhost:8000/#/event-detail/" + id
    },
    eventUrlTitle(event) {
      return "Event : " + event.name
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
    isUserRegistered(participants) {
      for (let participant of participants) {
        if (participant.id === this.user.pk) {
          return true
        }
        return false
      }
    },
    async registerForEvent(id) {
      const token = localStorage.getItem("access_token")
      try {
        await eventService.registerForEvent(id, this.place, token)
      } catch (err) {
        this.error = err
      }
    },
    isEventFull(event, participants) {
      return participants.length >= event.capacity
    },
    async fetchEvent(eventId) {
      const response = await eventService.eventDetail(eventId)
      this.event = response.data
      //this.place = response.data.place
      this.userPublisher = response.data.user.username
      this.participants = response.data.participants
    },
    getPlace(placeId) {
      return this.places.find((place) => place.id === placeId) || {}
    },
    shareOnWhatsapp() {
      let message = `Check out this awesome place: ${this.event.name} - ${this.eventUrl(
        this.event.id
      )}`
      let whatsappUrl = `https://wa.me/?text=${encodeURIComponent(message)}`
      window.location.href = whatsappUrl
    },
    shareOnFacebook() {
      let url = this.eventUrl(this.event.id)
      let facebookUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`
      window.location.href = facebookUrl
    },
    shareOnTwitter() {
      let url = this.eventUrl(this.event.id)
      let text = `${this.event.name} - Check out this place!`
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

.text{
  margin-top: 10px;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 500;
  color: #000;
  background-color: #fff;

}

.transparent-button {
  background-color: transparent;
  border: none;
  cursor: pointer;
  outline: none;
}
.card:hover .card-img-top {
  transform: scale(1.05);
}

.card-img-top {
  transition: transform 0.2s; /* Animation */
}

.card-img-top {
  max-height: 250px;
  max-width: 100%;
  object-fit: cover;
}

.col-md-4 {
  padding-left: 15px;
  padding-right: 15px;
  margin-bottom: 30px;
}

.col-md-6 {
  padding-left: 15px;
  padding-right: 15px;
  /* margin-bottom: 30px; */
}

.card {
  overflow: hidden;
  justify-content: space-between;
  border-radius: 8px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
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
  /* margin-bottom: 10px; */
}

.card-subtitle {
  font-size: 17px;
  font-weight: bold;
  /* margin-bottom: 10px; */
  text-align: left;
}

.subtitle-text {
  text-align: left;
}
/* .no-padding {
  padding: 0 !important;
  margin: 0 !important;
} */

.w-100 {
  align-items: end;
  align-content: center;
}

.card-text {
  font-size: 16px;
}
.main-color {
  color: var(--main-color);
}

.icon {
  font-size: 30px;
  margin: 10px;
}

.buttonSee {
  padding: 0.9em 1em;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 500;
  color: #000;
  background-color: #fff;
  border: 0.5px solid gray;
  border-radius: 45px;
  /* box-shadow: 0px 8px 5px rgba(0, 0, 0, 0.1); */
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
}

.buttonSee:hover {
  background-color: var(--main-color);
  box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4);
  color: #fff;
  transform: translateY(-2px);
}

.buttonSee:active {
  transform: translateY(-1px);
}
</style>
