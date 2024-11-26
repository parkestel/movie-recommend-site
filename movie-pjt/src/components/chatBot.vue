<template>
  <div>
    <!-- 오른쪽 아래에 고정된 Open Chat 버튼 -->
    <button @click="toggleModal" class="open-chat-btn">
      <font-awesome-icon :icon="['fas', 'person-chalkboard']" id="chatbot-icon"/>
      <br>
      <span>AI Teacher</span>
    </button>

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
  right: 0;
  width: 450px;
  height: 100%;
  background: linear-gradient(
    to right,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.2) 15%,
    rgba(0, 0, 0, 0.3) 100%
  );
  display: flex;
  justify-content: flex-end;
  align-items: center;
  z-index: 1000;
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
}

/* 모달 콘텐츠 스타일 */
.modal-content {
  background: rgba(255, 255, 255, 0.95);
  padding: 25px;
  border-radius: 25px;
  width: 80%;
  max-width: 600px;
  box-shadow: 0 8px 32px rgba(255, 103, 103, 0.15);
  border: 1.5px solid rgba(82, 82, 82, 0.884);
  animation: fadeIn 0.3s ease-out;
  margin-right: 40px;
  max-width: 400px;
}

/* 채팅 창 스타일 */
.chat-container {
  width: 100%;
  max-width: 600px;
  margin: 10px auto;
  padding: 20px;
  border: 1px solid rgba(255, 103, 103, 0.2);
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.8);
  box-shadow: 0 4px 15px rgba(255, 103, 103, 0.08);
}

.chat-box {
  max-height: 400px;
  overflow-y: auto;
  margin-bottom: 20px;
  padding: 10px;
}

/* 스크롤바 스타일링 */
.chat-box::-webkit-scrollbar {
  width: 6px;
}

.chat-box::-webkit-scrollbar-track {
  background: rgba(255, 103, 103, 0.05);
  border-radius: 10px;
}

.chat-box::-webkit-scrollbar-thumb {
  background: rgba(255, 103, 103, 0.3);
  border-radius: 10px;
}

.message {
  padding: 12px 16px;
  border-radius: 15px;
  margin-bottom: 12px;
  max-width: 80%;
  line-height: 1.5;
  position: relative;
  transition: all 0.3s ease;
}

.message p {
  color: #434040;
  font-size: 0.95rem;
  margin: 0;
}

.message.user {
  background: rgba(255, 103, 103, 0.15);
  margin-left: auto;
  border-bottom-right-radius: 5px;
}

.message.assistant {
  background: rgba(255, 255, 255, 0.9);
  margin-right: auto;
  border-bottom-left-radius: 5px;
  box-shadow: 0 2px 8px rgba(255, 103, 103, 0.08);
}

.input-container {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  padding: 10px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  box-shadow: 0 2px 10px rgba(255, 103, 103, 0.1);
}

input {
  width: 100%;
  padding: 12px 16px;
  border-radius: 12px;
  border: 1px solid rgba(255, 103, 103, 0.2);
  background: rgba(255, 255, 255, 0.9);
  font-size: 0.95rem;
  color: #434040;
  transition: all 0.3s ease;
}

input:focus {
  outline: none;
  border-color: rgba(255, 103, 103, 0.5);
  box-shadow: 0 0 0 3px rgba(255, 103, 103, 0.1);
}

input::placeholder {
  color: rgba(67, 64, 64, 0.6);
}

button {
  padding: 12px 20px;
  border: none;
  background: rgba(255, 103, 103, 0.7);
  color: white;
  border-radius: 12px;
  cursor: pointer;
  font-size: 0.95rem;
  font-weight: 500;
  transition: all 0.3s ease;
  white-space: nowrap;
}

button:hover {
  background: rgba(255, 103, 103, 0.85);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 103, 103, 0.2);
}

/* Open Chat 버튼 스타일 */
.open-chat-btn {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 14px 25px;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(8px);
  color: #434040;
  border: 1px solid rgba(255, 103, 103, 0.3);
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(255, 103, 103, 0.15);
  z-index: 1001;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 8px;
}

.open-chat-btn:hover {
  background: rgba(255, 103, 103, 0.1);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 103, 103, 0.2);
}

#chatbot-icon {
  color: rgba(255, 103, 103, 0.8);
  font-size: 16px;
}

/* 애니메이션 */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>