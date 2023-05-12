<template>
  <div>
    <h1>Page d'inscription</h1>
    <div>
      <label for="username">Username :</label>
      <input type="text" id="firstName" v-model="username"/>
    </div>
    <div>
      <label for="password">Mot de passe:</label>
      <input type="password" id="password" v-model="password" />
    </div>
    <div>
      <label for="confirmPassword">Confirmer le mot de passe:</label>
      <input type="password" id="confirmPassword" v-model="confirmPassword" />
    </div>
    <button v-if="!user" @click="register">S'inscrire</button>
    <p v-if="passwordMismatch">Password do not match</p>
    <p v-if="loginError">{{ loginError }}</p>
    <p v-if="!user">
      Vous avez déjà un compte ? <router-link to="/login">Se connecter</router-link>
    </p>
  </div>
</template>

<script>
import authService from "../services/authService"

export default {
  data() {
    return {
      username: "",
      password: "",
      confirmPassword: "",
      passwordMismatch: false,
      loginError: ""
    }
  },
  methods: {
    validatePassword(password, confirmPassword) {
      this.passwordMismatch = password !== confirmPassword
    },
    register() {
      if (this.password !== this.confirmPassword) {
        this.loginError = "Les mots de passe ne correspondent pas"
        return
      }

      authService
        .register({
          username: this.username,
          password1: this.password,
          password2: this.password
        })
        .catch((err) => {
          this.loginError = err.response.data
        })
    },
    Error() {
      return this.loginError
    }
  },
  watch: {
    password(newPassword) {
      this.validatePassword(newPassword, this.confirmPassword)
    },
    confirmPassword(newConfirmPassword) {
      this.validatePassword(this.password, newConfirmPassword)
    }
  },
  computed: {
    user() {
      return authService.user.value
    }
  }
}
</script>
