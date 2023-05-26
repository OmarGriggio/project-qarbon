<template>
  <div>
    <div v-if="error">
      <p>Une erreur est survenue: {{ error }}</p>
    </div>
    <div v-else>
      <h2 style="margin-bottom: 30px; padding-top: 30px">EVENTS</h2>
      <input
        v-model="searchEvent"
        placeholder="> Search events by name"
        style="
          margin-right: 10px;
          width: 20%;
          margin-bottom: 30px;
          text-align: center;
          border-radius: 9px;
          text-emphasis-color: white;
        "
      />
      <input
        v-model="searchPlace"
        placeholder="> search events by place name"
        style="
          margin-right: 10px;
          width: 20%;
          margin-bottom: 30px;
          text-align: center;
          border-radius: 9px;
          text-emphasis-color: white;
        "
      />

      <input
        v-model="searchUser"
        placeholder="> search by username"
        style="
          margin-right: 10px;
          width: 10%;
          margin-bottom: 30px;
          text-align: center;
          border-radius: 9px;
          text-emphasis-color: white;
        "
      />

      <button class="btn btn-primary" style="margin-left: 10px" @click="filterEvents">
        FILTER
      </button>

      <button class="btn btn-primary" style="margin-left: 10px" @click="resetFilters">RESET</button>

      <div class="row justify-content-center">
        <div v-for="event in events" :key="event.id" class="col-md-4">
          <div class="card" style="width: auto">
            <div class="card-body">
              <ul class="list-group list-group-flush">
                <li class="list-group-item">
                  <p>User connect id : {{ user.pk }}</p>
                  <p v-for="part in event.participants" :key="part.id">
                    User ID registered to the events : {{ part.id }}
                  </p>
                  <p>{{ event.participants }}</p>
                  <p>Capacity : {{ event.capacity }}</p>
                  <p>Available place : {{ event.participants.length }} / {{ event.capacity }}</p>
                  <div v-if="event.participants.length">
                    <p>Participants inscrits :</p>
                    <select v-model="selectedParticipantId">
                      <option
                        v-for="participant in event.participants"
                        :key="participant.id"
                        :value="participant.id"
                      >
                        {{ participant.username }}
                      </option>
                    </select>
                  </div>
                  <div v-else>
                    <p>Aucun participant inscrit</p>
                  </div>

                  <h5 class="card-title">{{ event.name }}</h5>
                  <p class="card-text">{{ event.description }}</p>
                </li>
                <li class="list-group-item">
                  <br />
                  <h5 class="card-subtitle">
                    {{ this.places[event.place].name }}
                  </h5>
                  <p class="subtitle-text">
                    {{ this.places[event.place].street }}
                    {{ this.places[event.place].number }}
                    <br />
                    {{ this.places[event.place].postal_code }}
                    {{ this.places[event.place].locality }}
                  </p>
                  <img :src="event.image" alt="event image" style="width: 50%; height: 50%" />
                  <br />
                  <br />

                  <div v-if="user">
                    <button
                      v-if="!isUserRegistered(event) && !isEventFull(event)"
                      @click="registerForEvent(event.id)"
                    >
                      Register
                    </button>
                    <p v-else-if="isUserRegistered(event)">You are already registered</p>
                    <p v-else>The event is full</p>
                  </div>
                  <div v-else>
                    <p>You need to be logged in to register</p>
                  </div>
                </li>
                <p>Posted by {{ event.user.username }}</p>
                <br />
              </ul>
              <!-- Vous pouvez afficher plus d'informations sur l'événement ici -->

              <button>
                <font-awesome-icon icon="fa-brands fa-twitter" />
                <ShareNetwork
                  network="twitter"
                  :url="eventUrl(event.id)"
                  :title="eventUrlTitle(event)"
                  description="This is an awesome event !"
                  twitter-user="qarbonEvent"
                >
                  <span>Share on Twitter</span>
                </ShareNetwork>
              </button>
              <br />
              <button>
                <font-awesome-icon icon="fa-brands fa-facebook" />
                <ShareNetwork
                  network="facebook"
                  :url="eventUrl(event.id)"
                  :title="eventUrlTitle(event)"
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
                  :url="eventUrl(event.id)"
                  :title="eventUrlTitle(event)"
                  description="This is an awesome event !"
                >
                  <span>Share on WhatsApp</span>
                </ShareNetwork>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <br />
</template>

<script>
import authService from "../services/authService"
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
  name: "createEvents",
  data() {
    return {
      searchEvent: "",
      searchPlace: "",
      searchUser: "",
      error: null,
      userFind: null,
      events: [],
      places: [],
      users: []
    }
  },
  async mounted() {
    authService.getUser()
    this.fetchPlaces()
    if (!this.searchEvent && !this.searchPlace && !this.searchUser) {
      this.fetchEvents()
    } else {
      this.filterEvents()
    }
  },
  computed: {
    user() {
      return authService.user.value
    }
  },
  methods: {
    isEventFull(event) {
      return event.participants.length >= event.capacity
    },
    logout() {
      authService.logout()
    },
    async filterEvents() {
      let url = "http://localhost:8000/api/events/?"
      if (this.searchEvent) {
        url += `name=${this.searchEvent}&`
      }
      if (this.searchPlace) {
        url += `place_name=${this.searchPlace}&`
      }
      if (this.searchUser) {
        url += `user=${this.searchUser}`
      }
      try {
        const events = await axios.get(url)
        this.events = events.data
      } catch (err) {
        this.error = err.response.data
      }
    },
    async fetchPlaces() {
      try {
        this.places = await axios
          .get("http://localhost:8000/api/places/")
          .then((response) => response.data)
      } catch (err) {
        this.error = err.response.data
      }
    },
    async fetchEvents() {
      try {
        this.events = await axios
          .get("http://localhost:8000/api/events/")
          .then((response) => response.data)
      } catch (err) {
        this.error = err.response.data
      }
    },
    resetFilters() {
      this.searchEvent = ""
      this.searchPlace = ""
      this.searchUser = ""
      this.fetchEvents()
    },
    eventUrl(index) {
      return `http://localhost:5173/#/events/${index}`
    },
    eventUrlTitle(Event) {
      return `Check out ${Event.name} on our plateform !`
    },
    async registerForEvent(id) {
      const token = localStorage.getItem("access_token")
      const headers = { Authorization: `Bearer ${token}` }
      const formData = new FormData()
      for (let key in this.place) {
        formData.append(key, this.place[key])
      }
      await axios.post(`http://127.0.0.1:8000/api/events/${id}/register/`, formData, { headers })
      await this.fetchEvents()
    },
    isUserRegistered(event) {
      for (let participant of event.participants) {
        if (participant.id === this.user.pk) {
          return true
        }
        return false
      }
    }
  },
  components: {
    ShareNetwork,
    FontAwesomeIcon
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
</style>
