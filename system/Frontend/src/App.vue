<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2022-11-20 18:21:36
 * @LastEditTime: 2023-01-10 16:36:27
-->
<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div>
    <RouterView />
  </div>
</template>

<style>
@import './common/font.css';
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  width: 100%;
}

</style>
