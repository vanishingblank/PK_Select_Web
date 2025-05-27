import { createRouter, createWebHistory } from 'vue-router'

import uploadFile from '@/components/uploadFile.vue'
import classManager from '@/components/classManagerNgx.vue'
import home from '@/components/home.vue'
import login from '@/components/login.vue'
import loginWindow from '@/components/loginWindow.vue'
import registWindow from '@/components/registWindow.vue'
import TheWelcome from '@/components/TheWelcome.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name:'loginPage',
      component:login,
      children:[
      {
        path:'',
        name:'loginWindow',
        component:loginWindow
      },
      {
        path:'/regist',
        name:'registWindow',
        component:registWindow
      }
      ]
    },
    {
      path:'/home',
      name:'home',
      component:home,
      children:[
        {
          path: '/init',
          name: 'initUploadFile',
          component:uploadFile
        },
        {
          path:'/classManager',
          name:'classManagerPage',
          component:classManager
        },
        {
          path:'/test',
          name:'test',
          component:TheWelcome
        }
      ]
    },


    // {
    //   path: '/init',
    //   name: 'initUploadFile',
    //   component:uploadFile
    // },
    // {
    //   path: '/about',
    //   name: 'About',
    //   component:()=>import('')
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //  // component: () => import('../views/AboutView.vue')
    // },
    // {
    //   path:'/classManager',
    //   name:'classManagerPage',
    //   component:classManager
    // },
  ]
})

export default router
