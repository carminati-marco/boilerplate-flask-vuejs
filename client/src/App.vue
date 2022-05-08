<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <n-loading-bar-provider>
  <n-message-provider>
    <n-notification-provider>
      <n-dialog-provider>
  <HelloWorld msg="Welcome to Your Vue.js App" />
      </n-dialog-provider>
    </n-notification-provider>
  </n-message-provider>
</n-loading-bar-provider>
    <n-button>naive-ui</n-button>
 
</template>

<script>

// General Font
// Monospace Font
import 'vfonts/FiraCode.css'
import HelloWorld from './components/HelloWorld.vue'
import { getHttp } from './http/fetchApi';


export default {
  name: 'App',
  components: {
    HelloWorld
  },
  setup() {
    console.log(`${process.env.VUE_APP_REST_URL}/toldyou`)
    getHttp(`${process.env.VUE_APP_REST_URL}/toldyou`, 'json').then((response) => { console.log("response", response); })
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
