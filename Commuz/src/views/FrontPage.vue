<script setup lang="ts">
import ContentBlockLeft from '@/components/ContentBlockLeftImage.vue'
import ContentBlockRight from '@/components/ContentBlockRightImage.vue'
import Partenaires from '@/components/Partenaires.vue'
import Reseaux from '@/components/Reseaux.vue'
import Popup from '@/components/Popup.vue'
import { ref, onMounted } from 'vue'

const contentBlocks = ref([
  {
    backgroundImage: 'front-bloc-1.jpg',
    title: 'Un voyage musical et artistique',
    paragraph1:
      'Chaque année la commuz réunis 1200 spectateurs pour vous proposer un spectacle à travers les âges.',
    paragraph2:
      'Au programme: histoire originale, chorégraphies, orchestre, danses, costumes et choeurs.'
  },
  {
    backgroundImage: 'pascal.jpg',
    title: "Pascal Ray - Directeur de l'Ecole Centrale de Lyon",
    paragraph:
      "Tout est parfaitement pensé et orchestré pour produire un spectacle unique et d'une qualité exceptionnelle. N'hésitez-pas à rejoindre l'aventure Commuz' en soutenant le talent de nos étudiant.e.s. Et n'oubliez-pas de venir les applaudir sur scène. Merci pour eux !"
  },
  {
    backgroundImage: 'front-bloc-2.jpg',
    title: "Un partenariat entre l'Ecole de Management de Lyon et l'Ecole Centrale de Lyon",
    paragraph1: "C'est plus de 80 étudiants qui viennent présenter leurs talents devant vous.",
    paragraph2:
      "Après plusieurs mois de préparation, les scénaristes, les chorégraphes, l'éclairage, la sonorisation, les costumiers, les décors et les acteurs prennent place pour donner vie à la scène, le temps d'une représenation."
  },
  {
    backgroundImage: 'debouk.jpg',
    title: "Frank Debouk - Ancien Directeur de l'Ecole Centrale de Lyon",
    paragraph:
      "J'ai pris hier soir un grand plaisir, le spectacle est de grande qualité, son, lumière, costumes magnifiques, décors, le tout au service d'artistes de talents : musiciens, danseurs, chanteurs, acteurs-chanteurs."
  }
])

const showPopup = ref(false)

onMounted(() => {
  // Check if the popup has been displayed before
  const popupClosed = sessionStorage.getItem('popupClosed')
  if (!popupClosed) {
    // If not displayed before, show the popup and update the local storage
    showPopup.value = true
  }
})
</script>

<template>
  <div class="video-container">
    <div class="overlay"></div>
    <video class="video" muted loop autoplay>
      <source src="@/assets/video/video-intro.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
  </div>

  <template v-for="(block, index) in contentBlocks" :key="index">
    <component
      v-if="index % 2 === 0"
      :is="ContentBlockLeft"
      :background-image="block.backgroundImage"
      :title="block.title"
      :paragraph1="block.paragraph1"
      :paragraph2="block.paragraph2"
    />
    <component
      v-else
      :is="ContentBlockRight"
      :background-image="block.backgroundImage"
      :title="block.title"
      :paragraph="block.paragraph"
    />
  </template>

  <Partenaires />
  <Reseaux />
  <template v-if="showPopup">
    <Popup />
  </template>
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
