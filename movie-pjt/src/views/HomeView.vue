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
        :slides-per-view="'auto'"
        :centered-slides="true"
        :space-between="30"
        :grab-cursor="true"
        :autoplay="autoplayOptions"
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
  disableOnInteraction: false
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
    title: '영화 기반 학습',
    description: '실제 영화 속 대사로 자연스러운 언어를 배워보세요',
    color: '#FF6B6B'
  },
  {
    icon: '💬',
    title: '학습 커뮤니티',
    description: '다른 학습자들과 학습 방법을 공유하고 토론해보세요',
    color: '#4ECDC4'
  },
  {
    icon: '📝',
    title: '맞춤형 학습',
    description: '자신만의 학습 방법을 기록하고 공유할 수 있습니다',
    color: '#45B7D1'
  },
  {
    icon: '🎯',
    title: '목표 설정',
    description: '개인별 학습 목표를 설정하고 달성해보세요',
    color: '#FF9F43'
  }
]

const navigateToLogin = () => {
  router.push({name:'login'})
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
</script>

<style scoped>
.home-container {
  background: var(--main-dark);
  color: white;
}

.hero-section {
  height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding: 2rem;
}

.glass-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(10px);
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  margin-bottom: 3rem;
}

.main-title {
  font-size: 4.5rem;
  font-weight: 800;
  margin-bottom: 1rem;
  background: linear-gradient(45deg, var(--point-peach), #ff9a9e);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.sub-title {
  font-size: 1.5rem;
  color: rgba(255, 255, 255, 0.9);
}

/* 주요 기능 스타일 수정 */
.features-container {
  max-width: 800px;
  width: 100%;
  margin: 4rem auto;
}

.feature-item {
  margin-bottom: 8rem;
}

.feature-content {
  background: rgba(255, 255, 255, 0.12);
  border-radius: 20px;
  padding: 3rem;
  position: relative;
  border: 1px solid rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
  color: white;
  transition: all 0.3s ease;
}

.feature-content:hover {
  transform: translateY(-5px);
  background: rgba(255, 255, 255, 0.15);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
}

.feature-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  display: block;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
}

.feature-content h3 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
  color: var(--point-peach);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
  font-weight: 600;
}

.feature-content p {
  font-size: 1.1rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 1);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  font-weight: 500;
}

/* 기대 효과 Swiper 스타일 */
.benefits-swiper {
  width: 100%;
  padding: 2rem 0;
}

.benefits-swiper :deep(.swiper-slide) {
  width: 300px;
  height: auto;
}

.benefit-card {
  background: linear-gradient(135deg, var(--point-peach), rgba(255, 255, 255, 0.1));
  border-radius: 20px;
  padding: 2rem;
  height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  text-align: center;
  transition: transform 0.3s ease;
  position: relative;
}

.benefit-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(255, 255, 255, 0.2);
}

.benefit-number {
  font-size: 3rem;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.3);
  margin-bottom: 1rem;
}

/* 반응형 디자인 수정 */
@media (max-width: 768px) {
  .feature-item {
    margin-bottom: 6rem;
  }

  .feature-content {
    padding: 2rem;
  }
}

/* 맥OS 스타일 브라우저 창 */
.browser-window {
  position: relative;
  z-index: 2;
  width: 80%;
  max-width: 900px;
  background: black;
  border-radius: 10px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  overflow: hidden;
  margin: 2rem auto;
  aspect-ratio: 16/9;
}

.browser-header {
  background: #f0f0f0;
  padding: 0.8rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  height: 5%;
  min-height: 40px;
}

.browser-buttons {
  display: flex;
  gap: 8px;
}

.browser-buttons span {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.close {
  background: #ff5f57;
}

.minimize {
  background: #ffbd2e;
}

.maximize {
  background: #28c940;
}

.browser-address-bar {
  flex: 1;
  background: #ffffff;
  border-radius: 5px;
  padding: 0.3rem 1rem;
  margin: 0 1rem;
  display: flex;
  align-items: center;
}

.browser-url {
  color: #333;
  font-size: 0.9rem;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.browser-content {
  width: 100%;
  height: 95%;
  background: transparent;
  overflow: hidden;
}

.browser-content img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.browser-window:hover .browser-content img {
  transform: none;
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .hero-section {
    padding: 1rem;
  }

  .browser-window {
    width: 95%;
    margin: 1rem auto;
  }

  .browser-content {
    height: 400px;
  }

  .browser-header {
    padding: 0.5rem;
    min-height: 35px;
  }

  .browser-buttons span {
    width: 10px;
    height: 10px;
  }

  .browser-url {
    font-size: 0.8rem;
  }
}

@media (min-width: 1200px) {
  .browser-window {
    width: 70%;
  }
}

.start-button {
  margin-top: 2rem;
  padding: 1rem 3rem;
  font-size: 1.2rem;
  background: var(--point-peach);
  border: none;
  border-radius: 2rem;
  color: white;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.start-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent,
    rgba(255, 255, 255, 0.3),
    transparent
  );
  transition: 0.5s;
}

.start-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4);
}

.start-button:hover::before {
  left: 100%;
}

.start-button .arrow {
  display: inline-block;
  margin-left: 8px;
  transition: transform 0.3s ease;
}

.start-button:hover .arrow {
  transform: translateX(5px);
}

/* 반응형에서 버튼 크기 조정 */
@media (max-width: 768px) {
  .start-button {
    padding: 0.8rem 2rem;
    font-size: 1rem;
  }
}

/* features-section 스타일 수정 */
.features-section {
  position: relative;
  padding: 8rem 2rem;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: hidden;
  background: #000;
}

/* 배경 이미지 수정 */
.features-section::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  height: 100%;
  background: url('@/assets/styles/movielist.png') no-repeat center center;
  background-size: contain;
  opacity: 0.7;
  filter: blur(2px);
  z-index: -1;
}

/* 배경 오버레이 */
.features-section::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: -1;
}

/* 섹션 타이틀 스타일 */
.features-section .section-title {
  color: white;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6);
  margin-bottom: 3rem;
  z-index: 1;
  font-size: 2.5rem;
  font-weight: 700;
}

/* 카드 컨테이너 */
.features-container {
  max-width: 800px;
  width: 100%;
  margin: 4rem auto;
  z-index: 1;
}

/* 반응형 디자인 수정 */
@media (min-width: 1200px) {
  .features-section::before {
    background-size: 100% 100%;
  }
}

@media (max-width: 768px) {
  .features-section::before {
    background-size: 100% 100%;
  }
}

/* hero-swiper 클래스 추가 */
.hero-swiper {
  width: 100%;
  height: 100%;
}

:deep(.hero-swiper .swiper-slide) {
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
}
</style>