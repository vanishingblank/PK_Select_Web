import { createRouter, createWebHistory } from 'vue-router'

import interAct from '@/components/interAct.vue'
import classManager from '@/components/classManagerNgx.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component:interAct
    },
    // {
    //   path: '/about',
    //   name: 'About',
    //   component:()=>import('')
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //  // component: () => import('../views/AboutView.vue')
    // },
    {
      path:'/classManager',
      name:'classManagerPage',
      component:classManager
    },
  ]
})

export default router
