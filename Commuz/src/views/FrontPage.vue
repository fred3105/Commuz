<script setup lang="ts">
import ContentBlock from '../components/ContentBlockLeft.vue';

const contentBlocks = [
  {
    backgroundImage: 'front-bloc-1.jpg',
    title: 'Une comédie musicale 100% étudiante',
    paragraph: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
  }
];
</script>

<template>
  <div class="video-container">
    <div class="overlay"></div>
    <video class="video" muted loop autoplay>
      <source src="@/assets/video/video-intro.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
  <content-block
      v-for="(block, index) in contentBlocks"
      :key="index"
      :background-image="block.backgroundImage"
      :title="block.title"
      :paragraph="block.paragraph"
    />
</template>

<style>
.video-container {
  position: relative;
  width: 100%;
  height: 100%;
}

.overlay {
  position: absolute;
  top: 40%;
  left: 28%;
  width: 42%;
  height: 19%;
  background: url('@/assets/photo/titre-commuz.svg') no-repeat center center;
  background-size: cover;
  opacity: 1;
}

.video {
  width: 100%;
  height: 100%;
}
</style>
