<template>
  <div class="row justify-content-center">
    <div class="col-md-6">
      <div class="card" style="width: auto">
        <div class="card-body">
          <p>ID de la event : {{ event.id }}</p>
          <h5 class="card-title">{{ event.name }}</h5>
          <p class="card-text"></p>
          <img :src="event.image" alt="event image" style="width: 50%; height: 50%" />
          <p>{{ event.description }}</p>
          <p>
            Place : {{ place.number }} {{ place.street }}, {{ place.postal_code }}
            {{ place.locality }}
          </p>
          <p>Price : CHF {{ event.price }}.-</p>
          <p>Date of the event : {{ formatDate(event.date) }}</p>
          <p>Hour of event : {{ formatTime(event.date) }} h</p>
          <hr />
          <p>Created by : {{ userPublisher }}</p>
          <!-- Vous pouvez afficher plus d'informations sur l'endroit ici -->

          <div v-if="user">
            <button
              v-if="!isUserRegistered(participants) && !isEventFull(event, participants)"
              @click="registerForEvent(event.id)"
            >
              Register
            </button>
            <p v-else-if="isUserRegistered(participants)">You are already registered</p>
            <p v-else>The event is full</p>
          </div>
          <div v-else>
            <p>You need to be logged in to register</p>
          </div>
          <div class="d-flex justify-content-evenly">
            <ShareNetwork
              network="twitter"
              :url="eventUrl(event.id)"
              :title="eventUrlTitle(event)"
              description="This is an awesome event !"
              twitter-user="qarbonEvent"
            >
              <font-awesome-icon icon="fa-brands fa-twitter" class="icon main-color" />
            </ShareNetwork>

            <ShareNetwork
              network="facebook"
              :url="eventUrl(event.id)"
              :title="eventUrlTitle(event)"
              description="This is an awesome event !"
            >
              <font-awesome-icon icon="fa-brands fa-facebook" class="icon main-color" />
            </ShareNetwork>

            <ShareNetwork
              network="whatsapp"
              :url="eventUrl(event.id)"
              :title="eventUrlTitle(event)"
              description="This is an awesome event !"
            >
              <font-awesome-icon icon="fa-brands fa-whatsapp" class="icon main-color" />
            </ShareNetwork>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import authService from "../services/authService"
import eventService from "../services/eventService"
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
      event: [],
      place: [],
      userPublisher: "",
      userCo: "",
      participants: []
    }
  },
  async mounted() {
    const eventId = this.$route.params.id
    this.fetchEvent(eventId)
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
      this.place = response.data.place
      this.userPublisher = response.data.user.username
      this.participants = response.data.participants
    }
  },
  components: {
    ShareNetwork,
    FontAwesomeIcon
  }
}
</script>

<style scoped>
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

.card-subtitle {
  font-size: 17px;
  font-weight: bold;
  margin-bottom: 10px;
  text-align: left;
}

.subtitle-text {
  text-align: left;
}

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
</style>
