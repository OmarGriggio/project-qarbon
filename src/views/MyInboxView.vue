<template>
  <div>
    <input type="text" v-model="username" placeholder="Search user...">
    <button @click="searchUser">Search</button>

    <div v-if="user">
      <h2>Results:</h2>
      <p>Username: {{ user }}</p>
      <!-- Display other user properties here -->
    </div>

    <div v-if="errorMessage">
      <h2>Error:</h2>
      <p>{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import userService from "../services/userService"

export default {
  data() {
    return {
      username: '',
      user: null,
      errorMessage: '',
    }
  },
  computed: {},
  methods: {
    postMessage() {},
    async searchUser() {
      try {
        this.user = await userService.fetchUserByUsername(this.username)
      } catch (error) {
        this.errorMessage = error.message
      }
    },
  },
  async mounted() {}
}
</script>

<style scoped></style>
