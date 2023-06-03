<template>
  <div>
    <input type="text" v-model="username" placeholder="Search user..." />
    <button @click="searchUser">Search</button>

    <div>
      <h2>Results:</h2>
      <p>Username:</p>
      <p>User id connected {{ this.user.pk }}</p>
      <!-- Display other user properties here -->
      <p>{{ messages }}</p>
      <p>{{ messages2 }}</p>
      <br />
      <p></p>
      <p></p>
    </div>

    <button @click="postMessage">Send message</button>

    <div v-if="errorMessage">
      <h2>Error:</h2>
      <p>{{ errorMessage }}</p>
    </div>

    <div>
      <!-- ... -->
      <h2>Conversation avec {{ userId }}</h2>
      <ul>
        <li v-for="msg in messages" :key="msg.id">
          {{ msg.content }}
          {{ msg.sender }}
          {{ msg.receiver }}
        </li>
      </ul>
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
      username: "",
      userId: null,
      errorMessage: "",
      messages: {},
      messages2: {}
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
    async loadMessages() {
      try {
        const token = localStorage.getItem("access_token")
        const resp = await userService.fetchMessages(token, this.user.pk)
        this.messages = resp.data
      } catch (error) {
        this.errorMessage = error.message
      }
    },
    async loadMessages2() {
      try {
        const token = localStorage.getItem("access_token")
        const resp = await messagesUsersServices.fetchUsersMessages(token)
        this.messages2 = resp.data
      } catch (error) {
        this.errorMessage = error.message
      }
    },
    async fetchUser(id) {
      const token = localStorage.getItem("access_token")
      const resp = await userService.fetchUserDetail(token, id)
      this.user = resp.data
    }
  },
  async mounted() {
    this.loadMessages()
    this.loadMessages2()
  },
  components: {
  }
}
</script>

<style scoped></style>
