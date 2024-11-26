<template>
  <div class="home-container">
    <section class="hero-section">
      <!-- 글래스모피즘 배경 -->
      <div class="glass-background"></div>
      
      <div class="hero-content"
           v-motion
           :initial="{ opacity: 0 }"
           :enter="{ opacity: 1, transition: { delay: 800 } }">
        <h1 class="main-title">Movie Language</h1>
        <p class="sub-title">영화로 배우는 새로운 언어 학습 경험</p>
        <button class="start-button" 
                @click="navigateToLogin"
                v-motion
                :initial="{ opacity: 0, scale: 0.5 }"
                :enter="{ opacity: 1, scale: 1, transition: { delay: 1000 } }">
          시작하기
          <span class="arrow">→</span>
        </button>
      </div>

      <!-- 맥OS 스타일 브라우저 창 -->
      <div class="browser-window"
           v-motion
           :initial="{ opacity: 0, y: 100 }"
           :enter="{ opacity: 1, y: 0, transition: { duration: 1500, ease: 'easeOut' } }">
        <div class="browser-header">
          <div class="browser-buttons">
            <span class="close"></span>
            <span class="minimize"></span>
            <span class="maximize"></span>
          </div>
          <div class="browser-address-bar">
            <span class="browser-url">MoviENg.com</span>
          </div>
        </div>
        <div class="browser-content">
          <swiper
            :modules="heroModules"
            :effect="'creative'"
            :creative-effect="creativeEffect"
            :autoplay="heroAutoplayOptions"
            :loop="true"
            class="hero-swiper">
            <swiper-slide v-for="(image, index) in heroImages" :key="index">
              <img :src="image.src" :alt="image.alt">
            </swiper-slide>
          </swiper>
        </div>
      </div>
    </section>

    <!-- 주요 기능 섹션을 스크롤 애니메이션으로 변경 -->
    <section class="features-section">
      <h2 class="section-title"
          v-motion
          :initial="{ opacity: 0, y: 50 }"
          :visible="{ opacity: 1, y: 0 }">
        주요 기능
      </h2>
      
      <div class="features-container">
        <div class="feature-item"
             v-for="(feature, index) in features" 
             :key="index"
             v-motion
             :initial="{ opacity: 0, y: 100 }"
             :visible="{ 
               opacity: 1, 
               y: 0, 
               transition: { 
                 delay: index * 200 
               }
             }"
             :visibleOnce="false"
             :leave="{ 
               opacity: 0, 
               y: -100,
               transition: { 
                 delay: index * 200 
               }
             }">
          <div class="feature-content">
            <i class="feature-icon">{{ feature.icon }}</i>
            <h3>{{ feature.title }}</h3>
            <p>{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 기대 효과 섹션을 Swiper로 변경 -->
    <section class="benefits-section">
      <h2 class="section-title"
          v-motion
          :initial="{ opacity: 0, y: 50 }"
          :enter="{ opacity: 1, y: 0 }">
        기대 효과
      </h2>
      
      <swiper
        :modules="modules"
        v-bind="swiperOptions"
        class="benefits-swiper">
        <swiper-slide v-for="(index) in 4" :key="index">
          <div class="benefit-card">
            <span class="benefit-number">0{{ index }}</span>
            <h3>{{ getBenefitTitle(index) }}</h3>
            <p>{{ getBenefitDescription(index) }}</p>
          </div>
        </swiper-slide>
      </swiper>
    </section>

    <!-- 기존 섹션들 아래에 추가 -->
    <section class="cta-section">
      <div class="cta-content"
           v-motion
           :initial="{ opacity: 0, y: 50 }"
           :visible="{ opacity: 1, y: 0 }">
        <h2>지금 바로 시작하세요</h2>
        <p>영화와 함께하는 새로운 언어 학습을 경험해보세요</p>
        <button class="cta-button" 
                @click="navigateToSignup"
                v-motion
                :initial="{ opacity: 0, scale: 0.5 }"
                :visible="{ opacity: 1, scale: 1, transition: { delay: 200 } }">
          시작하기
          <span class="arrow">→</span>
        </button>
        <p class="login-text">이미 계정이 있으신가요? <a @click="navigateToLogin" class="login-link">로그인</a></p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Autoplay, EffectCreative } from 'swiper/modules'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

// Swiper CSS
import 'swiper/css'
import 'swiper/css/autoplay'
import 'swiper/css/effect-creative'

const router = useRouter()

const modules = [Autoplay]
const autoplayOptions = {
  delay: 3000,
  disableOnInteraction: false,
  pauseOnMouseEnter: true
}

const heroModules = [Autoplay, EffectCreative]
const heroAutoplayOptions = {
  delay: 4000,
  disableOnInteraction: false
}

const effects = [
  {
    prev: {
      translate: ['-100%', 0, 0],
      opacity: 0
    },
    next: {
      translate: ['100%', 0, 0],
      opacity: 0
    }
  },
  {
    prev: {
      translate: ['100%', 0, 0],
      opacity: 0
    },
    next: {
      translate: ['-100%', 0, 0],
      opacity: 0
    }
  },
  {
    prev: {
      translate: ['-100%', 0, 0],
      opacity: 0
    },
    next: {
      translate: ['100%', 0, 0],
      opacity: 0,
      scale: 1.2
    }
  },
  {
    prev: {
      translate: ['-100%', 0, 0],
      rotate: [0, -10, 0],
      opacity: 0
    },
    next: {
      translate: ['100%', 0, 0],
      rotate: [0, 10, 0],
      opacity: 0
    }
  }
]

let currentEffectIndex = 0
const creativeEffect = {
  prev: effects[0].prev,
  next: effects[0].next,
  limitProgress: 3,
  shadowPerProgress: false,
  progressMultiplier: 1,
  perspective: 1000,
}

setInterval(() => {
  currentEffectIndex = (currentEffectIndex + 1) % effects.length
  creativeEffect.prev = effects[currentEffectIndex].prev
  creativeEffect.next = effects[currentEffectIndex].next
}, 4000)

// 이미지 import 추가
import heroBackground from '@/assets/styles/hero-background.png'
import movieDetail from '@/assets/styles/detail.png'
import movieComment from '@/assets/styles/comments.png'
import myPage from '@/assets/styles/mypage.png'

// heroImages 배열 수정
const heroImages = [
  {
    src: heroBackground,
    alt: '메인 스크린샷'
  },
  {
    src: movieDetail,
    alt: '영화 디테일'
  },
  {
    src: movieComment,
    alt: '영화 코멘트 댓글'
  },
  {
    src: myPage,
    alt: '마이페이지'
  }
]

const features = [
  {
    icon: '🎬',
    title: '영화 장면 학습',
    description: '실제 영화 속 대사와 상황을 통해 자연스러운 언어 표현을 배웁니다.'
  },
  {
    icon: '🎯',
    title: '맞춤형 학습',
    description: '사용자의 수준과 관심사에 맞는 영화 콘텐츠를 추천받습니다.'
  },
  {
    icon: '📝',
    title: '단어장 관리',
    description: '영화에서 학습한 새로운 단어와 표현을 체계적으로 관리할 수 있습니다.'
  },
  {
    icon: '🗣️',
    title: '발음 연습',
    description: '영화 속 원어민의 발음을 따라하며 실전 회화 능력을 향상시킵니다.'
  },
  {
    icon: '📊',
    title: '학습 분석',
    description: '개인별 학습 진행 상황과 성취 한에 확인할 수 있습니다.'
  },
  {
    icon: '👥',
    title: '커뮤니티',
    description: '다른 학습자들과 함께 영화와 언어에 대한 의견을 나눌 수 있습니다.'
  }
]

// 회원가입 페이지로 이동하는 메서드
const navigateToSignup = () => {
  router.push('/signup')
}

// 로그인 페이지로 이동하는 메서드
const navigateToLogin = () => {
  router.push('/login')
}

// 기대 효과 데이터 함수 추가
const getBenefitTitle = (index) => {
  const titles = [
    '빠른 언어 습득',
    '맞춤형 학습',
    '문화적 이해',
    '커뮤니티 학습'
  ]
  return titles[index - 1]
}

const getBenefitDescription = (index) => {
  const descriptions = [
    '실제 영화 속 대화를 통해 자연스러운 언어를 빠르게 습득할 수 있습니다',
    '개인의 수준과 관심사에 맞는 최적화된 학습 경험을 제공합니다',
    '영화를 통해 언어뿐만 아니라 문화적 맥락까지 자연스럽게 이해할 수 있습니다',
    '다른 학습자들과 함께 동기부여를 받으며 성장할 수 있습니다'
  ]
  return descriptions[index - 1]
}

// Swiper 브레이크포인트 설정 추가
const swiperOptions = {
  slidesPerView: 'auto',
  centeredSlides: true,
  spaceBetween: 30,
  grabCursor: true,
  autoplay: autoplayOptions,
  breakpoints: {
    1440: {
      spaceBetween: 40
    },
    1920: {
      spaceBetween: 50
    }
  }
}
</script>

<style scoped>
.home-container {
  background: var(--main-dark);
  color: white;
}

.hero-section {
  position: relative;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  overflow: hidden;
}

.glass-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(10px);
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  margin-bottom: 3rem;
  width: 100%;
  max-width: 1200px;
}

.main-title {
  font-size: 4.5rem;
  font-weight: 800;
  background: linear-gradient(45deg, var(--point-peach), #ff9a9e);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 1.5rem;
}

.sub-title {
  font-size: 1.5rem;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 3rem;
}

/* 주요 기능 스타일 수정 */
.features-container {
  width: 100%;
  max-width: 1400px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2.5rem;
  padding: 2rem;
  margin: 0 auto;
}

.feature-item {
  margin-bottom: 8rem;
}

.feature-content {
  background: linear-gradient(135deg,
    rgba(255, 255, 255, 0.15) 0%,
    rgba(255, 255, 255, 0.08) 50%,
    rgba(255, 255, 255, 0.05) 100%
  );
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  padding: 2.5rem 2rem;
  height: 100%;
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: 
    0 8px 32px rgba(0, 0, 0, 0.3),
    inset 0 2px 15px rgba(255, 255, 255, 0.1);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.feature-content:hover {
  transform: translateY(-5px);
  background: linear-gradient(135deg,
    rgba(255, 255, 255, 0.2) 0%,
    rgba(255, 255, 255, 0.12) 50%,
    rgba(255, 255, 255, 0.08) 100%
  );
  box-shadow: 
    0 15px 40px rgba(0, 0, 0, 0.4),
    inset 0 2px 20px rgba(255, 255, 255, 0.15);
}

.feature-icon {
  font-size: 3.2rem;
  margin-bottom: 1.5rem;
  display: block;
  background: linear-gradient(45deg, var(--point-peach), #ff9a9e);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: none;
}

.feature-content h3 {
  font-size: 1.8rem;
  margin-bottom: 1.2rem;
  background: linear-gradient(45deg, #ffffff, rgba(255, 255, 255, 0.9));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
  letter-spacing: -0.5px;
}

.feature-content p {
  font-size: 1.1rem;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.7);
  font-weight: 400;
}

/* 유리 테두리 효과 */
.feature-content::before {
  content: '';
  position: absolute;
  inset: -1px;
  border-radius: 20px;
  padding: 1px;
  background: linear-gradient(135deg,
    rgba(255, 255, 255, 0.4) 0%,
    rgba(255, 255, 255, 0.1) 50%,
    rgba(255, 255, 255, 0.2) 100%
  );
  -webkit-mask: 
    linear-gradient(#fff 0 0) content-box, 
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: 0.5;
  transition: opacity 0.4s ease;
}

.feature-content:hover::before {
  opacity: 1;
}

/* 반응형 디자인 */
@media (max-width: 1200px) {
  .features-container {
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
    padding: 1.5rem;
  }
}

@media (max-width: 768px) {
  .features-container {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    padding: 1rem;
  }

  .feature-content {
    padding: 2rem 1.5rem;
  }
}

/* 섹션 타이틀 여백 조정 */
.features-section .section-title {
  margin-bottom: 4rem;
}

@media (max-width: 768px) {
  .features-section .section-title {
    margin-bottom: 3rem;
  }
}

/* 기대 효과 Swiper 스타일 */
.benefits-swiper {
  width: 100%;
  padding: 4rem 0;
  margin-top: 3rem;
  background: radial-gradient(
    circle at center,
    rgba(255, 103, 103, 0.03) 0%,
    transparent 70%
  );
}

.benefits-swiper :deep(.swiper-slide) {
  width: 350px;
  height: auto;
  transition: transform 0.3s ease;
}

.benefit-card {
  background: linear-gradient(135deg, 
    rgba(255, 255, 255, 0.15) 0%,
    rgba(255, 255, 255, 0.08) 50%,
    rgba(255, 255, 255, 0.05) 100%
  );
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  padding: 3rem 2rem;
  height: 450px;
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: 
    0 8px 32px rgba(0, 0, 0, 0.3),
    inset 0 2px 15px rgba(255, 255, 255, 0.1),
    inset 0 -1px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.benefit-card::before {
  content: '';
  position: absolute;
  inset: -1px;
  border-radius: 20px;
  padding: 1px;
  background: linear-gradient(135deg,
    rgba(255, 255, 255, 0.4) 0%,
    rgba(255, 255, 255, 0.1) 50%,
    rgba(255, 255, 255, 0.2) 100%
  );
  -webkit-mask: 
    linear-gradient(#fff 0 0) content-box, 
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: 0.5;
  transition: opacity 0.4s ease;
}

.benefit-card:hover {
  transform: translateY(-5px) scale(1.02);
  background: linear-gradient(135deg, 
    rgba(255, 255, 255, 0.2) 0%,
    rgba(255, 255, 255, 0.12) 50%,
    rgba(255, 255, 255, 0.08) 100%
  );
  border: 1px solid rgba(255, 255, 255, 0.25);
  box-shadow: 
    0 15px 40px rgba(0, 0, 0, 0.4),
    inset 0 0 80px rgba(255, 255, 255, 0.08);
}

.benefit-number {
  font-size: 3rem;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.3);
  margin-bottom: 1rem;
}

/* 반응형 디자인 수정 */
@media (max-width: 768px) {
  .benefits-section {
    padding: 6rem 1rem;
  }

  .benefits-section .section-title {
    font-size: 2.5rem;
    margin-top: -3rem;
    margin-bottom: 3rem;
  }

  .benefit-card {
    height: 400px;
    padding: 2rem 1.5rem;
  }

  .benefit-number {
    font-size: 3rem;
  }
}

/* Swiper 슬라이드 크기 조정 */
:deep(.benefits-swiper .swiper-slide) {
  width: 350px;
  height: auto;
  transition: transform 0.3s ease;
}

/* 활성 슬라이드 효과 */
:deep(.benefits-swiper .swiper-slide-active) {
  transform: scale(1.05);
}

/* 큰 화면에서의 Swiper 설정 */
@media (min-width: 1440px) {
  :deep(.benefits-swiper .swiper-slide) {
    width: 400px; /* 더 큰 화면에서는 카드 크기 증가 */
  }

  .benefit-card {
    height: 500px; /* 카드 높이 증가 */
    padding: 4rem 3rem; /* 여백 증가 */
  }

  .benefit-number {
    font-size: 4.5rem; /* 번호 크기 증가 */
    margin-bottom: 2.5rem;
  }

  .benefit-card h3 {
    font-size: 2.2rem; /* 제목 크기 증가 */
    margin-bottom: 2rem;
  }

  .benefit-card p {
    font-size: 1.3rem; /* 본문 크기 증가 */
    line-height: 1.9;
  }
}

/* 더 큰 화면에서의 설정 */
@media (min-width: 1920px) {
  :deep(.benefits-swiper .swiper-slide) {
    width: 450px; /* 더 큰 화면에서는 카드 크기 추가 증가 */
  }

  .benefit-card {
    height: 550px; /* 카드 높이 추가 증가 */
    padding: 4.5rem 3.5rem;
  }

  .benefit-number {
    font-size: 5rem;
    margin-bottom: 3rem;
  }

  .benefit-card h3 {
    font-size: 2.5rem;
    margin-bottom: 2.5rem;
  }

  .benefit-card p {
    font-size: 1.4rem;
    line-height: 2;
  }

  .benefits-section .section-title {
    font-size: 4rem; /* 섹션 제목 크기 증가 */
    margin-bottom: 6rem;
  }
}

/* CTA 섹션 스타일 수정 */
.cta-section {
  padding: 0 2rem 10rem;
  background: linear-gradient(to bottom,
    rgba(0, 0, 0, 0.98) 0%,
    rgba(0, 0, 0, 0.95) 40%,
    rgba(255, 103, 103, 0.1) 100%
  );
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  min-height: 60vh;
  position: relative;
  overflow: hidden;
  box-shadow: 
    inset 0 0 150px rgba(255, 103, 103, 0.05);
}

.cta-content {
  max-width: 800px;
  position: relative;
  z-index: 2;
}

.cta-content h2 {
  font-size: 3.5rem;
  font-weight: 800;
  color: white;
  margin-bottom: 1.5rem;
  background: linear-gradient(45deg, var(--point-peach), #ff9a9e);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .cta-section {
    padding: 0 1rem 6rem;
  }
}

@media (min-width: 1440px) {
  .cta-section {
    padding: 0 2rem 12rem;
  }
}

.login-text {
  margin-top: 1.5rem;
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.7);
}

.login-link {
  color: var(--point-peach);
  text-decoration: none;
  cursor: pointer;
  font-weight: 600;
  transition: color 0.3s ease;
}

.login-link:hover {
  color: var(--point-rose);
}

/* 반응형 디자인에 추가 */
@media (max-width: 768px) {
  .login-text {
    font-size: 0.9rem;
  }
}

@media (min-width: 1440px) {
  .login-text {
    font-size: 1.1rem;
    margin-top: 2rem;
  }
}

/* 빛나는 효과 추가 */
.benefit-card::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(
    circle,
    rgba(255, 255, 255, 0.1) 0%,
    transparent 50%
  );
  transform: scale(0);
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.benefit-card:hover::before {
  transform: scale(1);
}

/* 테두리 빛나는 효과 */
.benefit-card::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 20px;
  padding: 1px;
  background: linear-gradient(
    135deg,
    transparent 0%,
    rgba(255, 255, 255, 0.1) 50%,
    transparent 100%
  );
  -webkit-mask: 
    linear-gradient(#fff 0 0) content-
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: 0;
  transition: opacity 0.4s ease;
}

.benefit-card:hover::after {
  opacity: 1;
}

/* Features 섹션 */
.features-section {
  position: relative;
  padding: 8rem 2rem 10rem;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: hidden;
  background: linear-gradient(to bottom,
    rgba(116, 78, 78, 0.637) 0%,
    rgba(19, 19, 19, 0.336) 40%,
    rgba(0, 0, 0, 0.95) 100%
  );
  z-index: 1;
  border-top: 1px solid rgba(255, 255, 255, 0.15);
}

/* Benefits 션 */
.benefits-section {
  padding: 10rem 2rem 0;
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: linear-gradient(to bottom,
    rgba(0, 0, 0, 0.95) 0%,
    #000 70%,
    rgba(0, 0, 0, 0.98) 100%
  );
  box-shadow: 
    inset 0 0 150px rgba(255, 103, 103, 0.05),
    inset 0 0 50px rgba(0, 0, 0, 0.8);
}

/* CTA 섹션 */
.cta-section {
  padding: 0 2rem 10rem;
  background: linear-gradient(to bottom,
    rgba(0, 0, 0, 0.98) 0%,
    rgba(0, 0, 0, 0.95) 40%,
    rgba(255, 103, 103, 0.1) 100%
  );
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  min-height: 60vh;
  position: relative;
  overflow: hidden;
  box-shadow: 
    inset 0 0 150px rgba(255, 103, 103, 0.05);
}

/* 맥OS 스타일 브라우저 창 */
.browser-window {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;
  background: #ffffff;
  border-radius: 10px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
  overflow: hidden;
}

.browser-header {
  padding: 0.8rem 1.2rem;
  background: #f0f0f0;
  border-bottom: 1px solid #e0e0e0;
  display: flex;
  align-items: center;
}

.browser-buttons {
  display: flex;
  gap: 8px;
}

.browser-buttons span {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.close {
  background: #ff5f56;
}

.minimize {
  background: #ffbd2e;
}

.maximize {
  background: #27c93f;
}

.browser-address-bar {
  margin-left: 1rem;
  padding: 0.3rem 1rem;
  background: #ffffff;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  flex-grow: 1;
  max-width: 500px;
  margin: 0 auto;
}

.browser-url {
  color: #666;
  font-size: 0.9rem;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.browser-content {
  height: 500px;
  background: #ffffff;
  overflow: hidden;
  padding: 0;
}

.browser-content img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 0;
  display: block;
}

/* 반응형 디자인 유지 */
@media (max-width: 768px) {
  .browser-window {
    margin: 1rem;
  }

  .browser-content {
    height: 300px;
  }
}

@media (min-width: 1440px) {
  .browser-content {
    height: 600px;
  }
}

/* 시작하기 버튼 스타일 복원 */
.start-button {
  padding: 1.2rem 3rem;
  font-size: 1.2rem;
  font-weight: 700;
  color: white;
  background: linear-gradient(45deg, var(--point-coral), var(--point-rose));
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 0.8rem;
  box-shadow: 0 10px 20px rgba(255, 103, 103, 0.3);
  position: relative;
  z-index: 2;
}

.start-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 30px rgba(255, 103, 103, 0.4);
  background: linear-gradient(45deg, var(--point-rose), var(--point-coral));
}

.start-button .arrow {
  transition: transform 0.3s ease;
}

.start-button:hover .arrow {
  transform: translateX(5px);
}


/* CTA 버튼 스타일 복원 */
.cta-button {
  padding: 1.2rem 3rem;
  font-size: 1.2rem;
  font-weight: 700;
  color: white;
  background: linear-gradient(45deg, var(--point-coral), var(--point-rose));
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 0.8rem;
  box-shadow: 0 10px 20px rgba(255, 103, 103, 0.3);
  margin-top: 2rem;
}

.cta-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 30px rgba(255, 103, 103, 0.4);
  background: linear-gradient(45deg, var(--point-rose), var(--point-coral));
}

.cta-button .arrow {
  transition: transform 0.3s ease;
}

.cta-button:hover .arrow {
  transform: translateX(5px);
}

/* CTA 섹션의 로그인 텍스트 스타일 */
.login-text {
  margin-top: 1.5rem;
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.8);
}

.login-link {
  color: var(--point-peach);
  text-decoration: none;
  cursor: pointer;
  transition: color 0.3s ease;
}

.login-link:hover {
  color: var(--point-rose);
}
</style>