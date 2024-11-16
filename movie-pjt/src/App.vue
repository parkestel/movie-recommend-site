<template>
<div>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
    </div>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item mx-2">
          <RouterLink :to="{name:'movies'}">영화 추천 목록</RouterLink>
        </li>
        <li class="nav-item mx-2">
          <a class="nav-link" href="#">Link</a>
        </li>
      </ul>
    </div>
  </nav>
  <RouterView/>
</div>
</template>

<script setup>

</script>

<style scoped>

</style>