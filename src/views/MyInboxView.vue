<template>
  <div>
    <input type="text" v-model="username" placeholder="Search user...">
    <button @click="searchUser">Search</button>

    <div>
      <h2>Results:</h2>
      <p>Username: {{ userId }}</p>
      <p>User id connected {{ this.user.pk }}</p>
      <!-- Display other user properties here -->
    </div>

    <button @click="postMessage">Send message</button>

    <div v-if="errorMessage">
      <h2>Error:</h2>
      <p>{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
import userService from "../services/userService"
import authService from "../services/authService"
import messagesUsersServices from "../services/messagesUsersServices"

export default {
  data() {
    return {
      username: '',
      userId: null,
      errorMessage: '',
    }
  },
  computed: {
    user() {
      return authService.user.value
    }
  },
  methods: {
    async postMessage() {
      const token = localStorage.getItem("access_token")
      const receiver = this.userId[0].id
      const content = "Hello"
      await messagesUsersServices.postMessage(token, receiver, content)
    },
    async searchUser() {
      try {
        const resp = await userService.fetchUserByUsername(this.username)
        this.userId = resp.data
      } catch (error) {
        this.errorMessage = error.message
      }
    },
  },
  async mounted() {

  }
}
</script>

<style scoped></style>
