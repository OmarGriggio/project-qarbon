<template>
  <div>
    <h1>My inbox</h1>
    <div>
      <select v-model="selectedUserId" @change="fetchConversation">
        <option v-for="user in users" :key="user.id" :value="user.id">{{ user.name }}</option>
      </select>
      <br />
      <br />
      <textarea v-model="message" placeholder="Enter your message"></textarea>
      <button @click="sendMessage">Send</button>
      <div v-for="message in conversation" :key="message.id">
        <p>{{ message.content }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [],
      selectedUserId: null,
      message: "",
      conversation: []
    }
  },
  computed: {},
  methods: {
    postMessage(){
        
    }

  },
  async mounted() {

  }
}
</script>

<style scoped></style>
