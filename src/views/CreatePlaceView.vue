<template>
  <div id="content">
    <div class="create-place">
      <form>
        <h1>Ajouter un nouvel endroit</h1>
        <input type="text" placeholder="Nom" v-model="place.name" />
        <input type="text" placeholder="Rue" v-model="place.street" />
        <input type="number" placeholder="Numero" v-model="place.number" />
        <input type="number" placeholder="Code Postal" v-model="place.postal_code" />
        <input type="text" placeholder="Localité" v-model="place.locality" />

        <button type="submit" @click="submitForm">Create</button>
      </form>
    </div>
  </div>

  <div>
    <div v-for="place in places" :key="place.id" :value="place.id">
      {{ place }}
    </div>
  </div>
</template>
<script>
import axios from "axios"
export default {
  data() {
    return {
      place: {
        name: "",
        street: "",
        number: 0,
        postal_code: 0,
        locality: ""
      },
      places: []
    }
  },
  methods: {
    async submitForm() {
      try {
        const token = localStorage.getItem("access_token")
        const headers = { Authorization: `Bearer ${token}` }

        const formData = new FormData()
        for (let key in this.place) {
          formData.append(key, this.place[key])
        }

        console.log(this.place)
        await axios.post("http://127.0.0.1:8000/api/places/", formData, { headers })
        this.place = {
          name: "",
          street: "",
          number: 0,
          postal_code: 0,
          locality: ""
        }
        await this.fetchPlaces();
      } catch (error) {
        console.error(error.response.data)
      }
    },
    async fetchPlaces() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/places/")
        this.places = response.data
      } catch (error) {
        console.error(error)
      }
    },
  },

  async mounted() {
    await this.fetchPlaces();
    await this.fetchEvents();
  }
}
</script>
