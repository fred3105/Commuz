<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

const isSidebarExtended = ref(false);

const toggleSidebar = () => {
  isSidebarExtended.value = !isSidebarExtended.value;
};

function extendSidebar() {
  if (!isSidebarExtended.value) {
    isSidebarExtended.value = true;
  }
}

function retractSidebar() {
  if (isSidebarExtended.value) {
    isSidebarExtended.value = false;
  }
}
</script>

<template>
  <div id="app">
    <div class="sidebar" :style="{ width: isSidebarExtended ? '12%' : '4%' }" @mouseover="extendSidebar" @mouseleave="retractSidebar">
      <div class="logo" @click="toggleSidebar">
      </div>
      <RouterLink to="/" v-show="isSidebarExtended">Commuz</RouterLink>
      <RouterLink to="/Partenaires" v-show="isSidebarExtended">Partenaires</RouterLink>
      <RouterLink to="/MisterCommuz" v-show="isSidebarExtended">Mister Commuz'</RouterLink>
    </div>
    <div class="content">
      <RouterView />
    </div>
  </div>
</template>

<style>

.sidebar {
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  background: #000000;
  color: #ffffff;
  padding: 1rem;
  transition: width 0.3s ease;
  z-index: 999;
}

.logo {
  height: 50px;
  background: url('./assets/photo/logo.svg') no-repeat center center;
  background-size: contain;
  margin-bottom: 40px;
}

.sidebar a {
  display: block;
  margin-bottom: 1rem;
  text-decoration: none;
  text-align: center;
  font-family: 'Courier New', Courier, monospace;
  font-size: 100%;
  color: #ffffff;
  transition: opacity 0.3s ease;
}

.sidebar a:hover {
  opacity: 0.6;
}

.content {
  float: fixed;
  margin-left: 5%;
  width: 95%;
}

body, html {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background-color: black;
}

</style>