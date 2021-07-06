import Vue from "vue"
import VueRouter from "vue-router"

// 뷰 어플리케이션에 라우터 플러그인을 추가한다.
Vue.use(VueRouter)

const Home = { template: "<div>Home</div>" }
const NotFound = { template: "<div>Not Found</div>" }

/* 생략 */
const router = new VueRouter({
  mode: "history",
  routes: [
    { path: "/bar", component: Home },
    { path: "*", component: NotFound },
  ],
})

export default router
