<template>
  <div id="content">
    <div class="container py-5">
      <div class="row justify-content-center">
        <div class="col-lg-8">
          <div class="card shadow-lg p-3 mb-5 bg-white rounded">
            <div class="card-body">
              <form @submit.prevent="submitForm" class="event-form">
                <h2 class="mb-4 text-center">Create Event</h2>
                <div class="mb-3">
                  <label for="name" class="form-label">Event Name:</label>
                  <input
                    type="text"
                    id="name"
                    v-model="event.name"
                    class="form-control"
                    placeholder="Enter event name"
                  />
                </div>
                <div class="mb-3">
                  <label for="description" class="form-label">Description:</label>
                  <textarea
                    id="description"
                    v-model="event.description"
                    class="form-control"
                    rows="3"
                    placeholder="Describe the event"
                  ></textarea>
                </div>
                <div class="mb-3">
                  <label for="price" class="form-label">Price:</label>
                  <input
                    type="number"
                    id="price"
                    v-model="event.price"
                    class="form-control"
                    placeholder="0.00"
                  />
                </div>
                <div class="mb-3">
                  <label for="date" class="form-label">Date:</label>
                  <input
                    type="datetime-local"
                    id="date"
                    v-model="event.date"
                    class="form-control"
                  />
                </div>
                <div class="mb-3">
                  <label for="place" class="form-label">Place:</label>
                  <select id="place" v-model="event.place" @change="checkPlace" class="form-select">
                    <option value="new">Add a new place</option>
                    <option v-for="place in places" :key="place.id" :value="place.id">
                      {{ place.name }}
                    </option>
                  </select>
                </div>
                <div class="mb-3">
                  <label for="image" class="form-label">Image for the event:</label>
                  <input type="file" id="image" @change="handleFileUpload($event)" />
                </div>
                <button type="submit" class="btn btn-submit btn-lg btn-block">Create Event</button>
              </form>
              <!-- Place Modal -->
              <!-- <place-modal v-if="showPlaceModal" @close="showPlaceModal = false"></place-modal> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios"
export default {
  data() {
    return {
      event: {
        name: "",
        description: "",
        price: 0,
        date: "",
        place: 0
      },
      places: [],
      newPlace: {
        name: ""
        // Add other fields for the new place here
      },
      newPlaceForm: false
    }
  },
  methods: {
    checkPlace() {
      if (this.event.place === "new") {
        this.$router.push("/create-place")
      }
    },
    handleFileUpload(event) {
      this.event.image = event.target.files[0]
    },
    async submitForm() {
      try {
        const token = localStorage.getItem("access_token")
        const headers = { Authorization: `Bearer ${token}` }

        const formData = new FormData()
        for (let key in this.event) {
          formData.append(key, this.event[key])
        }

        console.log(this.event)
        await axios.post("http://127.0.0.1:8000/api/events/", formData, { headers })
        this.event = {
          name: "",
          description: "",
          price: 0,
          date: "",
          image: null,
          place: ""
        }
      } catch (error) {
        console.error(error.response.data)
      }
    }
  },
  async created() {
    try {
      // this.user = await authService.getUser()
      // this.event.user = this.user.pk
      const response = await axios.get("http://127.0.0.1:8000/api/places/")
      this.places = response.data
    } catch (error) {
      console.error(error)
    }
  }
}
</script>
<style scoped>
h2 {
  color: #34495e;
  font-weight: 700;
}

.event-form .form-label {
  color: #34495e;
  font-weight: 500;
}

.event-form .form-control {
  border-color: #34495e;
  border-radius: 10px;
  transition: all 0.3s ease-in-out;
}

.event-form .form-control:focus {
  border-color: #3498db;
  box-shadow: 0 0 0 0.2rem rgba(52, 152, 219, 0.25);
}

.btn-submit {
  background: linear-gradient(90deg, #3498db, #9b59b6);
  border: none;
  color: white;
  border-radius: 10px;
  transition: all 0.3s ease-in-out;
}

.btn-submit:hover {
  background: linear-gradient(90deg, #9b59b6, #3498db);
}

.card {
  border-radius: 10px;
}

.card-body {
  padding: 20px;
}
</style>
