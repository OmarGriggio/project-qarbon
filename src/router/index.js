import { createRouter, createWebHashHistory } from "vue-router"
import HomeView from "../views/HomeView.vue"
import { LOCALSTORAGE_TOKEN_KEY } from "../services/authService"

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView
  },
  // {
  //   path: "/messages",
  //   name: "messages",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ "../views/MessagesView.vue")
  // },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/LoginView.vue")
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../views/RegisterView.vue")
  },
  {
    path: "/create-place",
    name: "create-place",
    component: () => import("../views/CreatePlaceView.vue")
  },
  {
    path: "/event-create",
    name: "event-create",
    component: () => import("../views/EventCreateView.vue"),
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth)
  const isAuthenticated = localStorage.getItem(LOCALSTORAGE_TOKEN_KEY)
  console.log(isAuthenticated)

  if (requiresAuth && !isAuthenticated) {
    next("/login") // or wherever you want to redirect unauthenticated users
  } else {
    next()
  }
})

export default router
