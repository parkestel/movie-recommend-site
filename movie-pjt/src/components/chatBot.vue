<template>
  <div>
    <!-- 오른쪽 아래에 고정된 Open Chat 버튼 -->
    <button @click="toggleModal" class="open-chat-btn">Open Chat</button>

    <!-- 모달 창 -->
    <div v-if="isModalOpen" class="modal-overlay">
      <div class="modal-content">
        <div class="chat-container">
          <div class="chat-box" ref="chatBox">
            <div v-for="(message, index) in messages" :key="index" class="message" :class="message.role">
              <p>{{ message.content }}</p>
            </div>
          </div>

          <div class="input-container">
            <input v-model="userMessage" @keyup.enter="sendMessage" placeholder="Type your message..." />
            <button @click="sendMessage">Send</button>
          </div>
        </div>

        <!-- 모달 닫기 버튼 -->
        <!-- <button @click="toggleModal">Close</button> -->
      </div>
    </div>
  </div>
</template>

  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  
  const API_key = import.meta.env.VITE_GPT_API_KEY;
  const API_URL = 'https://api.openai.com/v1/chat/completions';
  
  const userMessage = ref('');
  const messages = ref([
    { role: 'assistant', content: 'Hello! I am your English writing and conversation assistant. How can I help you today?' }
  ]);
  
  const isModalOpen = ref(false); // 모달 창 상태
  
  // 모달 열기 함수
  function toggleModal() {
    isModalOpen.value = !isModalOpen.value;
  }
  
  // API 요청 함수
  async function fetchData(message) {
    try {
      const response = await axios({
        method: 'post',
        url: API_URL,
        headers: {
          Authorization: `Bearer ${API_key}`,
          "Content-Type": "application/json",
        },
        data: {
          model: "gpt-3.5-turbo",
          messages: [
            ...messages.value,
            { role: 'user', content: message }
          ]
        }
      });
  
      // AI 응답을 messages에 추가
      messages.value.push({ role: 'assistant', content: response.data.choices[0].message.content });
  
    } catch (err) {
      console.log(err)
      let values = Object.values(err.response.data.error);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    }
  }
  
  // 메시지 전송 함수
  function sendMessage() {
    if (userMessage.value.trim()) {
      // 사용자 메시지 추가
      messages.value.push({ role: 'user', content: userMessage.value });
      // API 호출
      fetchData(userMessage.value);
      // 입력창 초기화
      userMessage.value = '';
    }
  }
  </script>

<style scoped>
/* 모달 오버레이 스타일 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; /* 모달이 다른 콘텐츠 위에 오도록 */
}

/* 모달 콘텐츠 스타일 */
.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  width: 80%;
  max-width: 600px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* 채팅 창 스타일 */
.chat-container {
  width: 100%;
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #f9f9f9;
}

.chat-box {
  max-height: 400px;
  overflow-y: auto;
  margin-bottom: 20px;
}

.message {
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 10px;
  max-width: 80%;
}

.message.user {
  background-color: #d1f7d1;
  align-self: flex-end;
}

.message.assistant {
  background-color: #e1e1e1;
  align-self: flex-start;
}

.input-container {
  display: flex;
  justify-content: space-between;
}

input {
  width: 80%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  margin-right: 10px;
}

button {
  padding: 10px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

/* Open Chat 버튼 고정 위치 */
.open-chat-btn {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  font-size: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  z-index: 1001; /* 모달보다 위에 있도록 설정 */
}

.open-chat-btn:hover {
  background-color: #0056b3;
}
</style>

