import Vue from 'vue'
import SetBuilder from './SetBuilder.vue'
import './plugins/element.js'

Vue.config.productionTip = false

new Vue({
  render: h => h(SetBuilder)
}).$mount('#app')
