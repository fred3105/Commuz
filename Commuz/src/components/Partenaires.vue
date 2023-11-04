<template>
  <div class="partenaires-container">
    <h1 class="main-title">Merci à nos partenaires</h1>
    <p class="paragraph">
      Le spectacle de la commuz n'aurait pas été possible sans eux, n'hésitez pas à soutenir le
      spectacle <a href="pdf/plaquette2023.pdf" download="plaquette2023.pdf" class="link">ici</a>.
    </p>
    <div class="logos-container">
      <img src="@/assets/photo/ecl.svg" alt="Ecole Centrale de Lyon" class="partner-logo" />
      <img
        src="@/assets/photo/em_corpo.svg"
        alt="Ecole de Management de Lyon"
        class="partner-logo"
      />
      <img src="@/assets/photo/crous.png" alt="Crous" class="partner-logo" />
      <img src="@/assets/photo/udl.svg" alt="Université de Lyon" class="partner-logo" />
    </div>
  </div>
</template>

<style scoped>
h1 {
  color: black;
  font-family: 'Courier New', Courier, monospace;
}

.link {
  color: black;
}

.partenaires-container {
  text-align: center;
  padding: 20px;
  background-color: gray;
}

.main-title {
  font-size: 24px;
  margin-bottom: 10px;
}

.paragraph {
  font-size: 16px;
  margin-bottom: 20px;
  color: black;
  font-family: 'Courier New', Courier, monospace;
}

.partner-logo {
  height: 100px;
  margin: 20px;
}
</style>
