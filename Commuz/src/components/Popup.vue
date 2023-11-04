<template>
  <div class="popup" v-show="showPopup">
    <div class="popup-content">
      <span class="close" @click="closePopup">&times;</span>
      <h2>Les nouvelles de la Commuz'!</h2>
      <p>Les castings pour le spectacle 2024 sont ouverts!</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const showPopup = ref(true)

const closePopup = () => {
  showPopup.value = false
  sessionStorage.setItem('popupClosed', 'true')
}
</script>

<style scoped>
.popup {
  font-family: 'Courier New', Courier, monospace;
  display: flex;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  justify-content: center;
  align-items: center;
}

.popup-content {
  background: #fff;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
  position: relative;
}

.close {
  top: 5px;
  right: 10px;
  position: absolute;
  font-size: 30px;
  cursor: pointer;
}
</style>
