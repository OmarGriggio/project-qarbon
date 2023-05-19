<template>
  <div id="nav">
    <router-link :to="{ name: 'home' }">Home</router-link> |
    <!-- <router-link :to="{ name: 'messages' }">Django Rest</router-link> | -->
    <router-link :to="{ name: 'create-place' }">Creer un endroit</router-link> |
    <router-link :to="{ name: 'event-create' }">Ajouter un événement</router-link> |

    <div v-if="!user"><RouterLink :to="{ name: 'login' }">Login</RouterLink> |</div>
    <div v-else>
      <p>Logged in as {{ user.username }}</p>
      <button @click="logout">Logout</button>
    </div>
  </div>
  <router-view />
</template>

<script>
import authService from "../src/services/authService"
import { LOCALSTORARGE_TOKEN_KEY } from "../src/services/authService"


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
    // authService
    authService.checkTokenExpiry()
    if (localStorage.getItem(LOCALSTORARGE_TOKEN_KEY)) {
      try {
        await authService.getUser()
        // this.messages = await messageService.fetchMessages()
      } catch (error) {
        console.log("Error fetching user", error)
      }
    }
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
  display: flex;
  padding: 20px;
  justify-content: center;
  gap: 10px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
