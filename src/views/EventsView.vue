<template>
  <div id="content">
    <div v-if="error">
      <p>Une erreur est survenue: {{ error }}</p>
    </div>
    <div v-else>
      <h2 style="margin-bottom: 30px; padding-top: 30px; color: var(--main-color)">Events</h2>
      <input
        v-model="searchEvent"
        @input="filterEventsDebounced"
        placeholder="Search events by name"
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
        @input="filterEventsDebounced"
        placeholder="Search events by place name"
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
        @input="filterEventsDebounced"
        placeholder="Search events by username"
        style="
          margin-right: 10px;
          width: 10%;
          margin-bottom: 30px;
          text-align: center;
          border-radius: 9px;
          text-emphasis-color: white;
        "
      />
      <select v-model="filterStatus" @change="filterEvents">
        <option value="all">All</option>
        <option value="registered">Registered</option>
        <option value="unregistered">Unregistered</option>
      </select>

      <!-- <button class="btn btn-success" style="margin-left: 10px" @click="filterEvents">
        FILTER
      </button> -->

      <button class="btn btn-success" style="margin-left: 10px" @click="resetFilters">RESET</button>

      <div class="row justify-content-center">
        <div v-for="event in events" :key="event.id" class="col-md-4">
          <div class="card">
            <img :src="event.image" alt="event image" class="card-img-top" />
            <div class="card-body">
              <ul class="list-group list-group-flush">
                <li class="list-group-item">
                  <h5 class="card-title" style="color: var(--main-color)">{{ event.name }}</h5>
                </li>
                <br />
                <li class="list-group-item">
                  <h5 class="card-subtitle">
                    {{ getPlace(event.place).name }}
                  </h5>
                  <p class="subtitle-text">
                    {{ getPlace(event.place).address }}
                    {{ getPlace(event.place).postal_code }}
                    {{ getPlace(event.place).locality }},
                    <br />
                    Number of participants : {{ event.participants.length }}
                  </p>
                </li>
                <li class="list-group-item">
                  <div>
                    <RouterLink :to="'/event-detail/' + event.id">
                      <button class="buttonSee">See more</button>
                    </RouterLink>
                  </div>
                </li>
              </ul>
              <!-- Vous pouvez afficher plus d'informations sur l'événement ici -->
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
import eventService from "../services/eventService"
import placeService from "../services/placeService"
import _ from "lodash"
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
      users: [],
      filterStatus: "all"
    }
  },
  async mounted() {
    const response = await placeService.fetchPlaces()
    this.places = response.data
    this.filterEvents()
  },
  computed: {
    user() {
      return authService.user.value ? authService.user.value : null
    }
  },
  methods: {
    filterEventsDebounced: _.debounce(function () {
      this.filterEvents()
    }, 300),

    getPlace(placeId) {
      return this.places.find((place) => place.id === placeId) || {}
    },
    isEventFull(event) {
      return event.participants.length >= event.capacity
    },
    logout() {
      authService.logout()
    },
    async filterEvents() {
      try {
        this.events = await eventService.filterEvents({
          name: this.searchEvent,
          place_name: this.searchPlace,
          user: this.searchUser
        })

        if (this.filterStatus === "registered") {
          this.events = this.events.filter((event) => this.isUserRegistered(event))
        } else if (this.filterStatus === "unregistered") {
          this.events = this.events.filter((event) => !this.isUserRegistered(event))
        }
      } catch (err) {
        this.error = err
      }
    },
    resetFilters() {
      this.searchEvent = ""
      this.searchPlace = ""
      this.searchUser = ""
      this.filterEvents()
    },
    eventUrl(index) {
      return `http://localhost:5173/#/events/${index}`
    },
    eventUrlTitle(Event) {
      return `Check out ${Event.name} on our plateform !`
    },
    async registerForEvent(id) {
      const token = localStorage.getItem("access_token")
      try {
        await eventService.registerForEvent(id, this.place, token)
        await this.filterEvents()
      } catch (err) {
        this.error = err
      }
    },
    isUserRegistered(event) {
      return event.participants.some((participant) => participant.id === this.user.pk)
    }
  },
  components: {}
}
</script>

<style scoped>
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
  margin-top: 10px;
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
