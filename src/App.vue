<template>
  <div id="nav">
    <router-link :to="{ name: 'home' }">Home</router-link> |
    <router-link :to="{ name: 'messages' }">Django Rest</router-link> |

    <div v-if="!user">
      <RouterLink :to="{ name: 'login' }">Login</RouterLink> |
      <router-link :to="{ name: 'create-place' }">Creer un endroit</router-link>
    </div>
    <div v-else>
      <p>Logged in as {{ user.username }}</p>
      <button @click="logout">Logout</button>
    </div>
  </div>
  <router-view />
</template>

<script>
import authService from "../src/services/authService"

export default {
  data() {
    return {}
  },
  computed: {
    user() {
      return authService.user.value
    }
  },
  methods: {
    logout() {
      authService.logout()
    }
  },
  async mounted() {
    authService.getUser()
    // this.messages = await messageService.fetchMessages()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
