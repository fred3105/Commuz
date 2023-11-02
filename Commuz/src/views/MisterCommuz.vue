<template>
  <div class="container">
    <div class="profile">
      <img src="@/assets/photo/mister-commuz.jpg" alt="mister-commuz" class="profile-picture"/>
    </div>
    <div class="output-area">{{ outputText }}</div>
    <div class="input-container">
      <input v-model="inputText" @keyup.enter="sendText" class="input-field" placeholder="Que veux tu savoir sur la commuz?">
      <button @click="sendText" class="send-button">Demander</button>
    </div>
  </div>
</template>
  
<script setup lang="ts">
import { ref } from 'vue';

const inputText = ref('');
const outputText = ref('');
const intermediateResponse = ref('');

const sendText = async () => {
  // Reset outputText to blank at the beginning of the function
  outputText.value = '...';
  intermediateResponse.value = '';

  try {
    const response = await fetch('http://127.0.0.1:8000/MisterCommuz', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input: inputText.value }),
    });

    const reader = response.body.getReader();

    const read = async () => {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        intermediateResponse.value += new TextDecoder().decode(value);
        // Update outputText whenever new data is received
        outputText.value = intermediateResponse.value;
      }
    };

    // Start reading the response in chunks
    await read();
  } catch (error) {
    // Handle error
  }
};
</script>


  
<style scoped>
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
.container {
  position: relative;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.output-area {
  padding: 30px;
  background-color: black;
  flex-grow: 1;
  overflow-y: auto;
  color: whitesmoke;
  text-align: center;
  font-family: 'Courier New', Courier, monospace;
  font-size: 20px;
}

.input-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #000000;
  width: 100%;
}

.input-field {
  flex-grow: 1;
  padding: 10px;
  margin-right: 10px;
  margin-left: 20px;
  border-radius: 5px;
  font-family: 'Courier New', Courier, monospace;
}

.send-button {
  padding: 10px 20px;
  background-color: rgb(255, 255, 255);
  color: #000000;
  border: none;
  border-radius: 5px;
  font-family: 'Courier New', Courier, monospace;
}

.send-button:hover {
  background-color: black;
  color: whitesmoke;
}
</style>