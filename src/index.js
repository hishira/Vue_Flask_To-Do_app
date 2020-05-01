import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
	state:{
		allTask: [],
		modalAppear: false,
		updateModalAppear: false,
		taskLength: 0
	}
})
