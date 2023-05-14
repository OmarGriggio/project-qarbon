<template>
  <div class="create-place">
    <h1>Ajouter un nouvel endroit</h1>
    <input type="text" placeholder="Nom" v-model="name"/>
    <input type="text" placeholder="Rue" v-model="street"/>
    <input type="number" placeholder="Numero" v-model="number" />
    <input type="number" placeholder="Code Postal" v-model="postal_code"/>
    <input type="text" placeholder="Localité" v-model="locality"/>
  </div>
</template>
<script>
export default {
  data() {
    return {
      name: "",
      street: "",
      number: 0,
      postal_code: 0,
      locality: ""
    }
  },
}
</script>
