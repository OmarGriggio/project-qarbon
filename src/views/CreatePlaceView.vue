<template>
  <div id="content">
    <div class="create-place">
      <form @submit.prevent="submitForm">
        <h1>Ajouter un nouvel endroit</h1>
        <label class="lbl">Nom du lieu</label>
        <input class="inpt" type="text" placeholder="Nom" v-model="place.name" /><br />
        <label class="lbl">Rue</label>
        <input class="inpt" type="text" placeholder="Rue" v-model="place.street" /><br />
        <label class="lbl">n°</label>
        <input class="inpt" type="number" placeholder="Numero" v-model="place.number" /><br />
        <label class="lbl">Code postal</label>
        <input
          class="inpt"
          type="number"
          placeholder="Code Postal"
          v-model="place.postal_code"
        /><br />
        <label class="lbl">Localité</label>
        <input class="inpt" type="text" placeholder="Localité" v-model="place.locality" /><br />
        <button type="submit">Create</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import { useRouter } from "vue-router"

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
        await this.fetchPlaces()

        // Navigate to PlaceView
        this.$router.push({ name: "place-list" })
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
    }
  },
  async mounted() {
    await this.fetchPlaces()
  }
}
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 50px;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

.lbl {
  font-weight: bold;
  margin-bottom: 5px;
}

.inpt {
  width: 300px;
  height: 30px;
  margin-bottom: 10px;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  width: 150px;
  height: 40px;
  background-color: #4caf50;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>
