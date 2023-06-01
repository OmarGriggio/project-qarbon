<template>
  <div id="content">
    <h1>My Events</h1>
    <div v-if="error">
      <p>An error occurred: {{ error }}</p>
    </div>
    <div v-else>
      <div class="row justify-content-center">
        <div v-for="event in events" :key="event.id" class="col-md-4">
          <div class="card mb-3">
            <img :src="event.image" alt="event image" class="card-img-top" />
            <div class="card-body">
              <ul class="list-group list-group-flush">
                <li class="list-group-item">
                  <h5 class="card-title">{{ event.name }}</h5>
                </li>
                <li class="list-group-item">
                  <h6 class="card-subtitle">
                    {{ getPlace(event.place).name }}
                  </h6>
                  <p class="card-text">
                    {{ getPlace(event.place).address }}
                    {{ getPlace(event.place).postal_code }}
                    {{ getPlace(event.place).locality }},
                    <br />
                    Number of participants: {{ event.participants.length }}
                  </p>
                  <p class="card-text">
                    {{ formatDate(event.date) }} -
                    {{ formatTime(event.date) }}
                  </p>
                </li>
                <li class="list-group-item">
                  <div>
                    <router-link :to="'/event-detail/' + event.id">
                      <button class="buttonSee">See more</button>
                    </router-link>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import eventService from "../services/eventService"
import placeService from "../services/placeService"

export default {
  name: "MyEvents",
  data() {
    return {
      error: null,
      events: [],
      places: []
    }
  },
  async mounted() {
    const token = localStorage.getItem("access_token")
    try {
      const response_events = await eventService.fetchMyevents(token)
      this.events = response_events.data
      console.log(this.events)
      const response_places = await placeService.fetchPlaces()
      this.places = response_places.data
    } catch (error) {
      this.error = error.message
    }
  },
  methods: {
    getPlace(placeId) {
      return this.places.find((place) => place.id === placeId) || {}
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
    }
  }
}
</script>

<style scoped>
h1 {
  font-size: 30px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: bold;
  margin-bottom: 30px;
  color: var(--main-color);
}

.card {
  border-radius: 8px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  transition: box-shadow 0.5s;
}

.card:hover {
  box-shadow: 0 4px 8px grey;
}

.card-img-top {
  max-height: 250px;
  object-fit: cover;
}

.card-body {
  flex-grow: 1;
}

.card-title {
  font-size: 20px;
  font-weight: bold;
}

.card-subtitle {
  font-size: 17px;
  font-weight: bold;
}

.card-text {
  font-size: 16px;
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
