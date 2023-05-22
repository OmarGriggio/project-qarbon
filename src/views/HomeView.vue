<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-8 text-center">
        <h1 style="color: var(--main-color)">Welcome to our Students Events Platform!</h1>
        <p class="lead">
          We are dedicated to bringing you the latest and greatest events in town. Browse through our selection and find something that piques your interest.
        </p>
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-lg-6">
        <div id="carouselExampleCaptions" class="carousel slide">
          <div class="carousel-indicators">
            <button
              v-for="(event, index) in events"
              :key="event.id"
              type="button"
              data-bs-target="#carouselExampleCaptions"
              :data-bs-slide-to="index"
              :class="{ active: index === 0 }"
              :aria-label="'Slide ' + (index + 1)"
            ></button>
          </div>
          <div class="carousel-inner">
            <div
              v-for="(event, index) in events"
              :key="event.id"
              class="carousel-item"
              :class="{ active: index === 0 }"
            >
              <img :src="event.image" class="d-block w-100" :alt="event.name" />
              <div class="carousel-caption d-none d-md-block">
                <h5>{{ event.name }}</h5>
                <p>{{ event.description }}</p>
              </div>
            </div>
          </div>
          <button
            class="carousel-control-prev"
            type="button"
            data-bs-target="#carouselExampleCaptions"
            data-bs-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button
            class="carousel-control-next"
            type="button"
            data-bs-target="#carouselExampleCaptions"
            data-bs-slide="next"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
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
      events: []
      // other data properties
    }
  },
  async created() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/events/")
      this.events = response.data
      console.log(this.events)
    } catch (error) {
      console.error(error)
    }
  }
  // other methods
}
</script>
<style scoped>
.carousel-caption {
  background-color: rgba(0, 0, 0, 0.6);
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.carousel-caption h5 {
  font-size: 1.5rem;
}

.carousel-caption p {
  font-size: 1.25rem;
}
</style>
