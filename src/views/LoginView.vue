<template>
  <div class="Login">
    <div class="container text-center col-lg-4">
      <h1 style="color: var(--main-color)">Welcome back</h1>
      <br />
      <div class="container col-lg-8">
        <div class="container row-1">
          <input
            class="form-control"
            type="text"
            placeholder="Username"
            aria-label="default input example"
            v-model="username"
          />
          <input
            class="form-control"
            type="password"
            placeholder="Password"
            aria-label="default input example"
            v-model="password"
          />
        </div>
      </div>
      <br />
      <button type="button" class="btn btn-success col-lg" @click="login">Sign in</button>
    </div>
    <br />
    <p v-if="!user">
      No account ?
      <router-link style="color: var(--main-color)" to="/register">Sign up</router-link>
    </p>
  </div>
  <div v-if="user">
    Logged in user data:
    <pre>{{ user }}</pre>
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
    async login() {
      this.loginError = ""
      await authService
        .login({
          username: this.username,
          password: this.password
        })
        .catch((err) => {
          this.loginError = err.response && err.response.data ? err.response.data : err
          console.error(this.loginError)
        })
      this.$router.push("/event-list")
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

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
