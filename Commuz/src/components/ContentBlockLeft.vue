<template>
    <div class="content-block">
      <div class="image-container">
        <img :src="'@/assets/photo/' + backgroundImage" alt="Background" class="background-image">
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
    paragraph: String,
  });
  </script>
  
  <style scoped>
  .content-block {
    display: flex;
    align-items: center;
    margin-bottom: 40px;
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
    background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white background for text */
  }
  
  h2 {
    font-size: 24px;
    margin-bottom: 10px;
  }
  </style>
  