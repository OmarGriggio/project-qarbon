<template>
  <div class="Login">
    <div class="container text-center col-lg-4">
      <h1>Se connecter</h1>
      <br />
      <form class="Login-Form" @submit.prevent="login">
        <div class="container col-lg-8">
          <div class="container row-1">
            <input
              class="form-control"
              type="text"
              placeholder="Nom d'utilisateur"
              aria-label="default input example"
              v-model="username"
              required
            />
            <input
              class="form-control"
              type="password"
              placeholder="Mot de passe"
              aria-label="default input example"
              v-model="password"
              required
            />
          </div>
        </div>
        <br />
        <button type="button" class="btn btn-primary col-lg">Se connecter</button>
      </form>
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
          this.loginError = err.response.data
        })

      this.username = ""
      this.password = ""
    },
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
.form-control {
  margin: 5px;
}
.Login {
  padding-top: 130px;
}
</style>
