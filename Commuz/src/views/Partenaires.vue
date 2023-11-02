<script setup lang="ts">
import Partenaires from '@/components/Partenaires.vue';
import Reseaux from '@/components/Reseaux.vue';
</script>

<template>
    <h2>
        Nos responsables partenaires sont à votre écoute, si vous voulez soutenir la Commuz' 
        <a href="mailto:commuzlyon@gmail.com?subject=Partenariats%20Commuz" class="link">
            écrivez
    </a>
    ou appelez les!
    </h2>
    <div class="profile-page">
    <div class="profile">
      <img src="@/assets/photo/KS.png" alt="Aleksandra Krivokapic" class="profile-picture">
      <div class="profile-text">
        <h2>Aleksandra Krivokapic </h2>
        <p>07 63 14 07 77</p>
      </div>
    </div>
    <div class="profile">
      <img src="@/assets/photo/PE.png" alt="Paul-Etienne Clément" class="profile-picture">
      <div class="profile-text">
        <h2>Paul-Etienne Clément </h2>
        <p>06 80 45 72 32</p>
      </div>
    </div>
  </div>
    <Partenaires/>
    <Reseaux/>
</template>

<style scoped>
.link{
    color:white;
}
.profile-page {
  display: flex;
  justify-content:center;
}

.profile {
  text-align: center;
  padding: 100px;
}

.profile-picture {
  width: 300px;
  height: 300px;
  object-fit: cover;
  border-radius: 50%;
}

.profile-text {
  margin-top: 10px;
  color:white;
  font-family: 'Courier New', Courier, monospace;
}

h2{
    margin-top: 80px;
    color: white;
    text-align: center;
    font-family: 'Courier New', Courier, monospace;
}
</style>
