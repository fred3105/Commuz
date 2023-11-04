<template>
  <div class="content-block">
    <div class="image-container">
      <img :src="'image/' + backgroundImage" alt="Background" class="background-image" />
    </div>
    <div class="text-container">
      <h2>{{ title }}</h2>
      <p>{{ paragraph1 }}</p>
      <br />
      <p>{{ paragraph2 }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  backgroundImage: String,
  title: String,
  paragraph1: String,
  paragraph2: String
})
</script>

<style scoped>
.content-block {
  position: relative;
  height: 600px;
  overflow: hidden;
  justify-content: center;
}

.text-container {
  font-family: 'Courier New', Courier, monospace;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: whitesmoke; /* Background color for text container */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transition: 0.4s ease;
  font-size: 20px;
  text-align: center;
  margin-left: 20px;
}

.content-block:hover .text-container {
  opacity: 1; /* Show the text container on hover */
}

.image-container {
  flex: 1;
  text-align: right;
}

.background-image {
  position: absolute;
  left: -5%;
  top: -40%;
  width: 100%;
}

h2 {
  font-size: 34px;
  margin-bottom: 10px;
}
</style>
