import Vuex from 'vuex'
import Vue from 'vue'
import filteredModule from '~/store/filteredStore'

Vue.use(Vuex);

// @ts-ignore
export const store = new Vuex.Store({
  modules: {

    filteredModule,
  },
})
