<template>
<div>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
    </div>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item mx-2">
          <RouterLink :to="{name:'login'}" v-if="!store.isLogin">Log in</RouterLink>
        </li>
        <li class="nav-item mx-2">
          <RouterLink :to="{name:'signup'}" v-if="!store.isLogin">Sign Up</RouterLink>
        </li>
        <li class="nav-item mx-2">
          <RouterLink :to="{name:'movies'}" v-if="store.isLogin">영화 추천 목록</RouterLink>
        </li>
        <li class="nav-item dropdown" v-if="store.isLogin">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            My Menu
          </a>
          <ul class="dropdown-menu">
            <li><RouterLink :to="{name:'wishmovies'}" class="dropdown-item">Wish Movie</RouterLink></li>
            <li><RouterLink :to="{name:'mynotelist'}" class="dropdown-item">Voca Note</RouterLink></li>
            <li><hr class="dropdown-divider"></li>
            <li><RouterLink :to="{name:'profile'}" class="dropdown-item">My Page</RouterLink></li>
            <li><hr class="dropdown-divider"></li>
            <li><button @click="store.logOut">Log out</button></li>
          </ul>
        </li>
      </ul>
    </div>
  </nav>
  <RouterView/>
  <footer>
    <div>
      <p>ⓒ 2024. </p>
    </div>
  </footer>
</div>
</template>

<script setup>
import { useMovieStore } from './stores/movie';

const store = useMovieStore()
</script>

<style scoped>

</style>