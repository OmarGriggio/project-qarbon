<template>
  <div>
    <form @submit.prevent="createEvent">
      <input type="text" v-model="eventData.name" placeholder="Event Name" required />
      <input type="datetime-local" v-model="eventData.date" required />
      <input
        type="text"
        v-model="searchQuery"
        @input="searchPlaces"
        placeholder="Search for a place"
        required
      />
      <select v-model="selectedPlace">
        <option disabled value="">Please select a place</option>
        <option v-for="place in places" :key="place.id" :value="place">
          {{ place.name }}
        </option>
      </select>
      <button type="submit">Create Event</button>
    </form>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data() {
    return {
      searchQuery: "",
      places: [],
      selectedPlace: null,
      eventData: {
        name: "",
        date: ""
      }
    }
  },
  methods: {
    async searchPlaces() {
      const response = await axios.get("http://your-django-api-url.com/places/search", {
        params: {
          query: this.searchQuery
        }
      })
      this.places = response.data.results.slice(0, 10) // limit to 10 results
    },
    async createEvent() {
      if (!this.selectedPlace) return
      const placeResponse = await axios.post("http://your-django-api-url.com/places/", {
        name: this.selectedPlace.name,
        street: this.selectedPlace.formatted_address, // assuming the API returns a 'formatted_address' field
        locality: this.selectedPlace.vicinity // assuming the API returns a 'vicinity' field
      })
      const placeId = placeResponse.data.id // assuming the API returns the created place's id
      await axios.post("http://your-django-api-url.com/events/", {
        name: this.eventData.name,
        date: this.eventData.date,
        place: placeId
      })
      this.selectedPlace = null // reset selected place
      this.eventData = { name: "", date: "" } // reset event data
    }
  }
}
</script>
