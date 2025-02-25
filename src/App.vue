<script setup>
import { RouterLink,RouterView } from 'vue-router';
// import { ref } from 'vue'
// import axios from 'axios'
// import * as XLSX from 'xlsx'
//import classManager from './components/classManager.vue';
// import interAct from './components/interAct.vue'
// import login from './components/login.vue';

/*const ip='http://192.168.1.239:5000'
const uploadInput = ref(null)
const classManagerRef = ref(null)
const ExcelToJson = (e) => {
  let fileObj = e.target.files[0]
  const fileReader = new FileReader();
  const fileNamesTMP = e.target.files[0].name
  //console.log(fileNamesTMP)
  fileReader.readAsArrayBuffer(fileObj);
  fileReader.onload = (event) => {
    const fileData = event.target.result;

    const workbook = XLSX.read(fileData, {
      type: 'binary',
    })

    /* 读取特定的表*/
    /*
    const wsname = workbook.SheetNames.find(name => name === '分组');
    const stdID= workbook.SheetNames.find(name => name === '班级名单');
    
    
    /*const wsname = workbook.SheetNames[0];
    //分组状况

    const stdID = workbook.SheetNames[3];
    //学号sheet,如表格变动可能要手动调整*/
/*
    const sheetJsonNameGroup = XLSX.utils.sheet_to_json(workbook.Sheets[wsname]);
    const sheetJsonNameID = XLSX.utils.sheet_to_json(workbook.Sheets[stdID]);
    console.log(sheetJsonNameGroup, sheetJsonNameID);
    const sheetJson = {
      filename: fileNamesTMP,
      sheetJsonNameGroup: sheetJsonNameGroup,
      sheetJsonNameID: sheetJsonNameID
    }

    //使用ajax来等文件处理之后通过axios发送给flask
    axios.post(`api/app/endpoint`, sheetJson)
      .then(response => {
        //在文件发送成功之后才让子组件的检测文件功能启用
        if (classManagerRef.value && classManagerRef.value.fetchFiles) {
          classManagerRef.value.fetchFiles();
        }
        console.log("成功:", response.data);
      })
      .catch(error => {
        console.error("Error:", error);
      })
  }


}*/

/*const uploadJson=(e)=>{
  axios.post('http://127.0.0.1:5000/api/endpoint', )
      .then(response => {
        //在文件发送成功之后才让子组件的检测文件功能启用
        if(classManagerRef.value && classManagerRef.value.fetchFiles)
        {
          classManagerRef.value.fetchFiles(); 
        }
        console.log("成功:", response.data);
      })
      .catch(error => {
        console.error("Error:", error);
      })

}*/


 

/*
添加预览全班学生名字

*/
</script>

<template>
  <div class="container">
    <aside class="sidebar">
      <router-link to="/">初始化</router-link>
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
  <!-- <interAct></interAct>
  <login></login> -->
  <!-- <class="top-section">
    <h1>初始</h1>
    <h3>首次使用,请上传学生分组信息的Excel表格</h3>
    <input ref="uploadInput" type="file" class="excelBox" @change="ExcelToJson" />
    <h3>上传上次生成的学生信息.json文件</h3>
    <input ref="uploadJson" type="file" class="excelBox" @change="" />
    <br>
  </div>
  
  <div class="class-manager-container">
    <classManager ref="classManagerRef"></classManager>
  </div> -->
  <!-- <live2D></?live2D> -->

</template>


<style scoped>
.container {
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
  height:100%;

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
<!-- <style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
}

/* 容器样式 */
.container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

/* 顶部板块样式 */
.top-section {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  background-color: #f0f0f0;
  /* 更浅的背景色 */
}

.top-section h1 {
  color: #333;
  /* 更深的文本色 */
  margin-bottom: 10px;
}

.top-section .excelBox {
  margin-bottom: 10px;
}

/* 导航栏样式 */
.navbar {
  margin-top: 20px;
}

/* 卡片样式 */
.card {
  margin-top: 20px;
  background-color: #fff;
  /* 保持白色背景 */
}

.card-title,
.card-text {
  color: #333;
  /* 更深的文本色 */
}

/* classManager 组件样式 */
.class-manager-container {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  background-color: #fff;
  margin-top: 20px;
}

/* 自定义按钮样式 */
input{
  display: inline-block;
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  opacity: 0.9;
}

.btn-primary {
  background-color: #0056b3;
  /* 更深的蓝色 */
  color: white;
}

.btn-secondary {
  background-color: #5a6268;
  /* 更深的灰色 */
  color: white;
}

.btn:hover {
  opacity: 0.9;
}
</style> -->
