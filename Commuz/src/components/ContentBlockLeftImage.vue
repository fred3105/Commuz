<template>
  <div class="content-block">
    <div class="image-container">
      <img :src="'image/' + backgroundImage" alt="Background" class="background-image">
    </div>
    <div class="text-container">
      <h2>{{ title }}</h2>
      <p>{{ paragraph }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  backgroundImage: String,
  title: String,
  paragraph: String
});
</script>
  
<style scoped>
.content-block {
  display: flex;
  align-items: center;
  background-color: black;
  color: white;
  font-family: 'Courier New', Courier, monospace;
  font-size: 20px;
}

.image-container {
  flex: 1;
  text-align: right;
}

.background-image {
  width: 100%;
  height: auto;
}

.text-container {
  flex: 1;
  padding: 20px;
  background-color: rgba(0, 0, 0, 1); /* Semi-transparent white background for text */
}

h2 {
  font-size: 34px;
  margin-bottom: 10px;
}
</style>