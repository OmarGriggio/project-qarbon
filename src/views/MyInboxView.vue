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

    <div v-for="conversation in conversations" :key="conversation">
      <p>{{ conversation.groupedMessages }}</p>
    </div>

    <div v-for="conversation in conversations" :key="conversation.user.id">
      <ConversationBox :conversation="conversation" @sendMessage="postMessage" />
    </div>
  </div>
</template>

<script>
import userService from "../services/userService"
import authService from "../services/authService"
import messagesUsersServices from "../services/messagesUsersServices"
import ConversationBox from "../components/ConversationBox.vue"

export default {
  data() {
    return {
      username: "",
      userId: null,
      errorMessage: "",
      messages: {},
      messages2: {},
      conversations: []
    }
  },
  computed: {
    user() {
      return authService.user.value
    }
  },
  methods: {
    deleteEmptyMessages() {
      const emptyConversationIndex = this.conversations.findIndex(c => c.messages.length === 0)
      if (emptyConversationIndex !== -1) {
        this.conversations.splice(emptyConversationIndex, 1)
      }
    },
    async postMessage(user, content) {
      const token = localStorage.getItem("access_token")
      const receiver = user.id
      await messagesUsersServices.postMessage(token, receiver, content)
      this.loadMessages()
      this.loadMessages2()
    },
    async searchUser() {
      try {
        const resp = await userService.fetchUserByUsername(this.username)
        this.userId = resp.data

        // Vérifier si une conversation avec cet utilisateur existe déjà
        const existingConversation = this.conversations.find((c) => c.user.id === this.userId[0].id)
        if (!existingConversation) {
          // Si aucune conversation n'existe, en créer une nouvelle
          this.conversations.unshift({
            user: this.userId[0],
            messages: []
          })
        }
        this.deleteEmptyMessages()
      } catch (error) {
        this.errorMessage = error.message
      }
    },
    async loadMessages() {
      try {
        const token = localStorage.getItem("access_token")
        const resp = await userService.fetchMessages(token, this.user.pk)
        this.conversations = this.groupMessgagesbyUser(resp.data)
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
    },
    groupMessgagesbyUser(messages) {
      let groupedMessages = {}
      messages.forEach((msg) => {
        let otherUser = msg.sender.id === this.user.pk ? msg.receiver : msg.sender
        if (!groupedMessages[otherUser.id]) {
          groupedMessages[otherUser.id] = {
            user: otherUser,
            messages: []
          }
        }
        groupedMessages[otherUser.id].messages.push(msg)
      })

      // Convertir l'objet en tableau
      return Object.values(groupedMessages)
    }
  },
  async mounted() {
    this.loadMessages()
    this.loadMessages2()
  },
  components: {
    ConversationBox
  }
}
</script>

<style scoped></style>
