<template>
  <div id="content">
    <nav class="navbar navbar-expand-lg navbar-light">
      <div id="nav" class="container-fluid">
        <router-link class="navbar-brand ms-3 fs-2 p-0" to="/">Qarbon</router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'create-place' }"
                >Create a place</router-link
              >
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'event-create' }"
                >Add an event</router-link
              >
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'event-list' }">See events</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'place-list' }">See places</router-link>
            </li>
          </ul>
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item" v-if="!user">
              <router-link class="nav-link" :to="{ name: 'login' }">Login</router-link>
            </li>
            <li class="nav-item" v-else>
              <span class="navbar-text mr-3">Logged in as {{ user.username }}</span>
              <button class="btn btn-outline-success" @click="logout">Sign out</button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
  <router-view />
</template>

<script>
import authService from "../src/services/authService"
import { LOCALSTORAGE_TOKEN_KEY } from "../src/services/authService"

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
    if (localStorage.getItem(LOCALSTORAGE_TOKEN_KEY)) {
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

#background {
  position: fixed;
  z-index: -1;
  width: 100vw;
  height: 100vh;
  background-color: #fbfbfd;
}

#content {
  margin-left: 10%;
  margin-right: 10%;
}

#nav {
  display: flex;
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
