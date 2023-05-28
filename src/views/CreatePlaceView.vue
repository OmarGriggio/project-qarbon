<template>
  <div id="content">
    <div class="create-place">
      <form @submit.prevent="submitForm">
        <h1>Ajouter un nouvel endroit</h1>
        <div class="col-lg-6">
          <input class="form-control" type="text" placeholder="Nom du lieu" v-model="place.name" />
          <span class="input-group">
            <input class="form-control" type="text" placeholder="Rue" v-model="place.street" />
            <input class="form-control" type="number" placeholder="N° rue" v-model="place.number" />
          </span>
          <input
            class="form-control"
            type="number"
            placeholder="Code Postal"
            v-model="place.postal_code"
          />
          <input class="form-control" type="text" placeholder="Localité" v-model="place.locality" />
        </div>
        <button type="submit" id="CreateButton" @click="submitForm">Create</button>
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
        number: "",
        postal_code: "",
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

#CreateButton {
  padding: 1.3em 3em;
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
  margin: 15px;
}

#CreateButton:hover {
  background-color: #23c483;
  box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4);
  color: #fff;
  transform: translateY(-7px);
}

#CreateButton:active {
  transform: translateY(-1px);
}
.form-control {
  margin: 5px;
}
.create-place {
  padding-top: 130px;
}
</style>
