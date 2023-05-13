<template>
  <div class="register">
    <div class="container">
      <form class="register-form">
        <h2>Page d'inscription</h2>
        <div>
          <div class="p-1">
            <div class="container col-lg-4">
              <input
                type="text"
                id="firstName"
                class="form-control"
                placeholder="Nom d'utilisateur"
                aria-label="default input example"
                v-model="username"
              />
            </div>
          </div>
          <div class="p-1">
            <div class="container col-lg-4">
              <input
                type="password"
                id="password"
                class="form-control"
                aria-label="default input example"
                placeholder="Mot de passe"
                v-model="password"
              />
            </div>
          </div>
          <div class="p-1">
            <div class="container col-lg-4">
              <input
                type="password"
                id="confirmPassword"
                class="form-control"
                aria-label="default input example"
                placeholder="Confirmer le mot de passe"
                v-model="confirmPassword"
              />
            </div>
          </div>
          <button class="btn btn-primary" v-if="!user" @click="register">S'inscrire</button>
          <p v-if="passwordMismatch">Password do not match</p>
          <p v-if="loginError">{{ loginError }}</p>
          <p v-if="!user">
            Vous avez déjà un compte ? <router-link to="/login">Se connecter</router-link>
          </p>
        </div>
      </form>
    </div>
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
        .then(() => {
          this.$router.push({ name: "home" })
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
<style>
.register .btn {
  margin: 2rem;
}
.register {
  padding-top: 130px;
}
</style>
