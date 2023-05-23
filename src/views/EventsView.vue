<template>
    <div>
      
      <div v-if="error">
        <p>Une erreur est survenue: {{ error }}</p>
      </div>
      <div v-else>
        <h2 style="margin-bottom: 30px;padding-top: 30px;">EVENTS</h2>
        <input v-model="searchEvent" placeholder="> Cherchez un événement par nom..." style="margin-right: 10px;width:40% ;margin-bottom: 30px;text-align: center;border-radius: 9px;text-emphasis-color: white;">
        <input v-model="searchPlace" placeholder="> Cherchez un événement par lieu..." style="margin-right: 10px;width:40% ;margin-bottom: 30px;text-align: center;border-radius: 9px;text-emphasis-color: white;">

        <button @click="filterEvents">Chercher</button>
        <div class="row justify-content-center">
          <div v-for="event in events" :key="event.id" class="col-md-4">
            <div class="card" style="width: auto;">
              <div class="card-body">
                <h5 class="card-title">{{ event.name }}</h5>
                <p class="card-text">{{ event.description }}</p>
  
                <!-- Vous pouvez afficher plus d'informations sur l'événement ici -->
              </div>
            </div>
          </div>       
        </div>
      </div>
    </div>
  
    <br/>
  
  
  <div>
    <div v-if="error">
      <p>Une erreur est survenue: {{ error }}</p>
    </div>
  <div v-else>
  <h2 style="margin-bottom: 30px;margin-top: 30px;">PLACES</h2>
  <div class="row justify-content-center">
  
  <div v-for="place in places" :key="place.id" class="col-md-6">
  <div class="card" style="width: auto;">
    <div class="card-body">
      <h5 class="card-title">{{ place.name }}</h5>
  <p class="card-text">
   {{ place.street }} {{ place.number }} <br/> {{ place.postal_code }} {{ place.locality }}
  </p>
  <!-- Vous pouvez afficher plus d'informations sur l'endroit ici -->
  </div>
  </div>
  </div>
  </div>
  </div>
  </div>
  

    
  
 
  </template>
  
  <script>
  import authService from "../services/authService"
  import axios from "axios"
  
  export default {
    name: "createEvents",
    data() {
      return {
        searchEvent:'',
        searchPlace:'',
        error: null,
        events: [],
        places: [],
      }
    },
    async mounted() {
      authService.getUser()
      try {
        this.events = await axios.get("http://localhost:8000/api/events/").then((response) => response.data)
        this.places = await axios.get("http://localhost:8000/api/places/").then((response) => response.data)
      } catch (err) {
        this.error = err.response.data
      }
    },
    computed: {
      user() {
        return authService.user.value
      }
    },
    methods: {
      logout() {
        authService.logout()
      },
      async filterEvents(){
        this.events = await axios.get("http://localhost:8000/api/events/?name="+this.searchEvent+"&place_name="+this.searchPlace).then((response) => response.data)
      }
      
    }
  }
  </script>
  
  
  <style>
    
    .col-md-4 {
      padding-left: 15px;
      padding-right: 15px; 
      margin-bottom: 30px;
    }
  
    .col-md-6 {
      padding-left: 15px;
      padding-right: 15px; 
      margin-bottom: 30px;
    }
  
    .card {
      height: 100%;
      display: flex;
      flex-direction:row;
      justify-content: space-between;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      background-color: #ffffff;
      transition: box-shadow 0.5s;
      width:auto;
    }
  
    .card:hover {
      box-shadow: 0 4px 8px  grey;
    }
  
    .card-body {
      flex-grow: 1;
    }
  
    .card-title {
      font-size: 20px;
      font-weight: bold;
      margin-bottom: 10px;
    }
  
    .w-100 {
      align-items: end;
      align-content: center;
    }
  
    .card-text {
      font-size: 16px;
    }
  </style>
  