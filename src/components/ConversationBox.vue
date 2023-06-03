<template>
  <div>
    <h2>Conversation avec {{ conversation.user.username }}</h2>

    <ul>
      <li v-for="message in conversation.messages" :key="message.id">
        <p>
          {{ message.content }}
          (Sender -- {{ message.sender.username }}) (Receiver -- {{ message.receiver.username }})
        </p>
      </li>
    </ul>

    <input v-model="newMessage" type="text" placeholder="Type your message..." />
    <button @click="emitSendMessage">Send message</button>
  </div>
</template>

<script>
export default {
  props: {
    conversation: Object
  },
  data() {
    return {
      newMessage: ""
    }
  },
  methods: {
    emitSendMessage() {
      this.$emit("sendMessage", this.conversation.user, this.newMessage)
      this.newMessage = ""
    }
  }
}
</script>
