<template>
    <div class="container">
        <div class="output">{{ outputText }}</div>
        <input v-model="inputText" placeholder="Mister Commuz' à ton écoute">
        <button @click="sendText">Send</button>
    </div>
</template>
  
<script setup lang="ts">
import { ref } from 'vue';

const inputText = ref('');
const outputText = ref('');

const sendText = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/Response', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input: inputText.value }),
    });
    console.log(response)
    const reader = response.body.getReader();

    let result = '';
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      result += new TextDecoder().decode(value);
    }

    outputText.value = result;
  } catch (error) {
    // Handle error
  }
};
</script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
  }
  
  .output {
    margin-top: 20px;
    font-weight: bold;
    color: white;
  }
  </style>
  