import Vue from 'vue'
import App from './App.vue'
import './../node_modules/bulma/css/bulma.css'
import store from './index.js'
Vue.config.productionTip = false
new Vue({
    render: h => h(App),
    store
}).$mount('#app')