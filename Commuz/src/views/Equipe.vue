<script setup lang="ts">
import Partenaires from '@/components/Partenaires.vue'
import Reseaux from '@/components/Reseaux.vue'
import ClickableComponent from '@/components/ClickableComponent.vue'
</script>

<template>
  <div class="team-presenation">
    <ClickableComponent
      imageSrc="/image/laptop.png"
      title="Webmaster"
      expandedContent="Le webmaster manie l'informatique pour assurer la billetterie du spectacle et maintenir le site internet de la commuz. "
      imageSrcTeamMember="/image/antoine.png"
      teammateName="Antoine"
    />
    <ClickableComponent
      imageSrc="/image/heart.png"
      title="VP amour"
      expandedContent="Les VP amours sont les petites fourmis de la commuz, nourriture, petites attention, et réconfort sont de mise."
      imageSrcTeamMember="/image/baptiste.png"
      teammateName="Baptiste"
    />
  </div>
  <Partenaires />
  <Reseaux />
</template>

<style>
.team-presentation {
  color: white;
  font-family: 'Courier New', Courier, monospace;
}
</style>
