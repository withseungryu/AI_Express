<template>
<div>
  <div class="alert alert-primary" role="alert">
    <button type="button"  class="btn" v-on:click="leftNumber()"><</button>
    <button type="button"  class="btn" v-on:click="rightNumber()">></button>
  </div>
</div>
</template>

<script>
import { Vue, Component } from 'vue-property-decorator';

//@ts-ignore
@Component
export default class Footer extends Vue {
  rightNumber(){

    this.$store.commit('filteredStore/rightTurn');
    console.log(this.$store.state.filteredStore.chartAge);
  }
  leftNumber(){

    this.$store.commit('filteredStore/leftTurn');
    console.log(this.$store.state.filteredStore.idx);
  }
}
</script>

<style scoped>

</style>
