<script setup lang="ts">
import ContentBlockLeft from '@/components/ContentBlockLeftImage.vue';
import ContentBlockRight from '@/components/ContentBlockRightImage.vue';
import Partenaires from '@/components/Partenaires.vue';
import Reseaux from '@/components/Reseaux.vue';
import { ref } from 'vue';

const contentBlocks = ref([
      {
        backgroundImage: 'front-bloc-1.jpg',
        title: 'Un voyage musical et artistique',
        paragraph: 'Lorem Ipsum'
      },
      {
        backgroundImage: 'front-bloc-2.jpg',
        title: "L'Ecole de Management de Lyon et L'Ecole Centrale de Lyon",
        paragraph: 'Lorem Ipsum'
      }
]);
</script>

<template>
  <div class="video-container">
    <div class="overlay"></div>
    <video class="video" muted loop autoplay>
      <source src="@/assets/video/video-intro.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>

  <template v-for="(block, index) in contentBlocks" :key="index">
      <component v-if="index % 2 === 0" :is="ContentBlockLeft" :background-image="block.backgroundImage" :title="block.title" :paragraph="block.paragraph" />
      <component v-else :is="ContentBlockRight" :background-image="block.backgroundImage" :title="block.title" :paragraph="block.paragraph" />
  </template>

  <Partenaires/>
  <Reseaux/>
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

