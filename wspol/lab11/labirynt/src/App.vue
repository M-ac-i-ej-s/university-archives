<template>
  <div class="App">
    <router-view/>
  </div>
</template>

<script setup>
import { useItemStore } from "@/stores/item";
import { useConnectionStore } from "@/stores/connection";
import { socket } from "@/socket";

const itemStore = useItemStore();
const connectionStore = useConnectionStore();

// remove any existing listeners (after a hot module replacement)
socket.off();

itemStore.bindEvents();
connectionStore.bindEvents();
</script>

<style>
.App {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
