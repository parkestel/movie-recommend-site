<template>
  <div class="home-container">
    <!-- 히어로 섹션: 웹사이트 메인 소개 -->
    <section class="hero-section">
      <div class="hero-content">
        <h1 class="main-title">Movie Language</h1>
        <p class="sub-title">영화로 배우는 새로운 언어 학습 경험</p>
        <button class="start-button" @click="navigateToLogin">시작하기</button>
      </div>
    </section>

    <!-- 주요 기능 소개 섹션 -->
    <section class="features-section">
      <h2>주요 기능</h2>
      <div class="features-grid">
        <div class="feature-card">
          <i class="feature-icon">🎬</i>
          <h3>영화 기반 학습</h3>
          <p>실제 영화 속 대사로 자연스러운 언어를 배워보세요</p>
        </div>
        <div class="feature-card">
          <i class="feature-icon">💬</i>
          <h3>학습 커뮤니티</h3>
          <p>다른 학습자들과 학습 방법을 공유하고 토론해보세요</p>
        </div>
        <div class="feature-card">
          <i class="feature-icon">📝</i>
          <h3>맞춤형 학습</h3>
          <p>자신만의 학습 방법을 기록하고 공유할 수 있습니다</p>
        </div>
      </div>
    </section>

    <!-- 사용 방법 튜토리얼 섹션 -->
    <section class="tutorial-section">
      <h2>이용 방법</h2>
      <div class="tutorial-steps">
        <div class="step">
          <div class="step-number">1</div>
          <h3>회원가입</h3>
          <p>간단한 정보로 가입하고 시작하세요</p>
        </div>
        <div class="step">
          <div class="step-number">2</div>
          <h3>영화 선택</h3>
          <p>학습하고 싶은 영화를 찾아보세요</p>
        </div>
        <div class="step">
          <div class="step-number">3</div>
          <h3>학습 방법 확인</h3>
          <p>다른 사용자들의 학습 방법을 참고해보세요</p>
        </div>
        <div class="step">
          <div class="step-number">4</div>
          <h3>나만의 학습</h3>
          <p>자신만의 학습 방법을 만들고 공유하세요</p>
        </div>
      </div>
    </section>

    <!-- 시작하기 섹션 -->
    <section class="start-section">
      <h2>지금 바로 시작하세요</h2>
      <p>Movie Language와 함께 즐거운 언어 학습을 시작해보세요</p>
      <button class="start-button" @click="navigateToLogin">시작하기</button>
    </section>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const navigateToLogin = () => {
  router.push({name:'login'})
}
</script>

<style scoped>
.home-container {
  width: 100%;
  min-height: 100vh;
  background: var(--main-dark);
  color: white;
}

/* 히어로 섹션 스타일 */
.hero-section {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
              url('@/assets/hero-background.jpg') center/cover;
}

.hero-content {
  max-width: 800px;
  padding: 2rem;
}

.main-title {
  font-size: 4rem;
  margin-bottom: 1rem;
  color: var(--point-peach);
}

.sub-title {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  color: rgba(255, 255, 255, 0.9);
}

/* 기능 소개 섹션 스타일 */
.features-section {
  padding: 5rem 2rem;
  text-align: center;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 3rem auto;
}

.feature-card {
  padding: 2rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 1rem;
  backdrop-filter: blur(10px);
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-10px);
}

.feature-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

/* 튜토리얼 섹션 스타일 */
.tutorial-section {
  padding: 5rem 2rem;
  background: rgba(0, 0, 0, 0.3);
}

.tutorial-steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 3rem auto;
}

.step {
  text-align: center;
  padding: 2rem;
}

.step-number {
  width: 40px;
  height: 40px;
  background: var(--point-peach);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
  font-weight: bold;
}

/* 시작하기 섹션 스타일 */
.start-section {
  padding: 5rem 2rem;
  text-align: center;
  background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
              url('@/assets/start-background.jpg') center/cover;
}

.start-button {
  padding: 1rem 3rem;
  font-size: 1.2rem;
  background: var(--point-peach);
  border: none;
  border-radius: 2rem;
  color: white;
  cursor: pointer;
  transition: all 0.3s ease;
}

.start-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(255, 103, 103, 0.4);
}

/* 반응형 디자인을 위한 미디어 쿼리 */
@media (max-width: 768px) {
  .main-title {
    font-size: 3rem;
  }

  .sub-title {
    font-size: 1.2rem;
  }

  .features-grid,
  .tutorial-steps {
    grid-template-columns: 1fr;
  }
}
</style>