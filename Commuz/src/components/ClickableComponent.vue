<template>
  <div class="clickable-component">
    <div class="image-container">
      <img :src="imageSrc" alt="Image" />
    </div>
    <div class="title">{{ title }}</div>
    <div class="expanded-content">
      {{ expandedContent }}
      <div class="image-container-teammate">
        <img :src="imageSrcTeamMember" alt="Image" />
      </div>
      <div class="teammateName">{{ teammateName }}</div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  imageSrc: String,
  title: String,
  expandedContent: String,
  imageSrcTeamMember: String,
  teammateName: String
})
</script>

<style scoped>
.clickable-component {
  position: relative;
  height: 160px;
  overflow: hidden;
  background-color: white;
  transition:
    width 0.3s ease,
    height 0.3s ease;
  text-align: center;
  margin-top: 5px;
  margin-left: 10px;
  margin-bottom: 5px;
}

.clickable-component:hover {
  height: 450px;
}

.teammateName {
  font-weight: bold;
}

.image-container {
  width: 100px;
  height: 100px;
  overflow: hidden;
  margin-top: 5px;
  margin-left: auto;
  margin-right: auto;
}

.image-container-teammate img {
  width: 150px;
  height: 150px;
  margin-top: 40px;
  border-radius: 50%;
  margin-left: auto;
  margin-right: auto;
}
.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.title {
  margin-top: 20px;
  font-weight: bold;
  font-size: 30px;
  font-family: 'Courier New', Courier, monospace;
}

.expanded-content {
  margin-top: 10px;
  font-family: 'Courier New', Courier, monospace;
  font-size: 20px;
}
</style>
