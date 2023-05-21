<template>
  <div class="Login">
    <div class="container text-center col-lg-4">
      <h1>Se connecter</h1>
      <br />
      <div class="container col-lg-8">
        <div class="container row-1">
          <input
            class="form-control"
            type="text"
            placeholder="Nom d'utilisateur"
            aria-label="default input example"
            v-model="username"
          />
          <input
            class="form-control"
            type="password"
            placeholder="Mot de passe"
            aria-label="default input example"
            v-model="password"
          />
        </div>
      </div>
      <br />
      <button type="button" class="btn btn-primary col-lg" @click="login">Se connecter</button>
    </div>
    <br />
    <p v-if="!user">
      Vous n'avez pas de compte ? <router-link to="/register">S'inscrire</router-link>
    </p>
  </div>
  <div v-if="user">
    Logged in user data:
    <pre>{{ user }}</pre>
    <input type="submit" value="Logout" @click="logout" /> <br />
  </div>
</template>

<script>
import authService from "../services/authService"
import { LOCALSTORAGE_TOKEN_KEY } from "../services/authService"

export default {
  data() {
    return {
      username: "",
      password: "",
      error: "",
      hasAccount: true
    }
  },
  computed: {
    user() {
      return authService.user.value
    }
  },
  methods: {
    login() {
      this.loginError = ""
      authService
        .login({
          username: this.username,
          password: this.password
        })
        .catch((err) => {
          this.loginError = err.response && err.response.data ? err.response.data : err
          console.error(this.loginError)
        })

      this.username = ""
      this.password = ""
    },
    logout() {
      authService.logout()
    }
  },
  async mounted() {
    // authService.getUser()
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
.form-control {
  margin: 5px;
}
.Login {
  padding-top: 130px;
}
</style>
