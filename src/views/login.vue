<template>
  <div>
    <h1>Page de connexion</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">Nom d'utilisateur:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div>
        <label for="password">Mot de passe:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Se connecter</button>
    </form>
    <p v-if="!user">
      Vous n'avez pas de compte ? <router-link to="/register">S'inscrire</router-link>
    </p>
  </div>

  <div v-if="user">
    Logged in user data:
    <pre>{{ user }}</pre>
    <input type="submit" value="Logout" @click="logout"/>
    <br />
  </div>
</template>

<script>
import authService from "../services/authService";

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

      this.username = "";
      this.password = "";
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
