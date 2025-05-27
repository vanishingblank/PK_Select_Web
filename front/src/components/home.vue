<script>
import { RouterView, RouterLink } from 'vue-router';
</script>
<template>
    <div class="homeContainer">
        <aside class="sidebar">
            <router-link to="/init">添加班级</router-link>
            <router-link to="/classManager">班级管理</router-link>
            <RouterLink to="/test">TEST</RouterLink>
        </aside>
        <main class="main-content">
            <header class="navbar">
                <img alt="Vue logo" class="logo" src="@/assets/logo.svg" />
                <span style="color:black; padding: 10px 20px; font-size:25px"><strong>班级管理系统</strong></span>
            </header>
            <section class="content">
                <RouterView />
            </section>
        </main>
    </div>
</template>

<style>
.homeContainer {
    display: flex;
    height: 100vh;
    /* position: fixed; */
    margin: 0;

    box-sizing: content-box;
}

.sidebar {
    width: 200px;
    background-color: #2b2b2bd4;
    /* color: rgb(193, 49, 49); */
    padding: 20px;
    height: 100%;

}

.sidebar a {
    color: white;
    padding: 20px 0;
    text-decoration: none;
    display: block;
    text-align: center;
}

.sidebar a:hover {
    background-color: #33333365;
    border-radius: 5%;
    transition: 0.1s;
}

.main-content {
    flex-grow: 1;
    /* padding: 20px; */
    display: block;
    flex-direction: column;
}

.navbar {
    background-color: #5b5a5a8a;
    color: white;
    /* width: 100vh; */
    padding: 10px 20px;
    margin-top: 0;
    display: flex;
}

.navbar-icon {
    height: 30px;
    margin-right: 10px;

}

.content {
    flex-grow: 1;
    padding: 20px;
}

.logo {
    width: 50px;
    height: 50px;
    position: relative;
    display: block;
    margin-right: 0px;
    margin-top: auto;
    margin-bottom: auto;

}
</style>
