import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import '@/assets/styles/main.css'

import App from './App.vue'
import router from './router'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faLock, faLockOpen, faTrashCan, faThumbsUp, faPersonChalkboard } from '@fortawesome/free-solid-svg-icons'
import { faThumbsUp as farThumbsUp  } from '@fortawesome/free-regular-svg-icons'

/* add icons to the library */
library.add(faLock, faLockOpen, faTrashCan, faThumbsUp, farThumbsUp, faPersonChalkboard)

const app = createApp(App)
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

app.component('font-awesome-icon', FontAwesomeIcon)
// app.use(createPinia())
app.use(pinia)
app.use(router)
app.mount('#app')


