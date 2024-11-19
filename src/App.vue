<script setup>
import { ref } from 'vue'
import axios from 'axios'
import * as XLSX from 'xlsx'
import classManager from './components/classManager.vue';
const ip='http://192.168.1.239:5000'
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
    const wsname = workbook.SheetNames.find(name => name === '分组');
    const stdID= workbook.SheetNames.find(name => name === '班级名单');
    
    
    /*const wsname = workbook.SheetNames[0];
    //分组状况

    const stdID = workbook.SheetNames[3];
    //学号sheet,如表格变动可能要手动调整*/

    const sheetJsonNameGroup = XLSX.utils.sheet_to_json(workbook.Sheets[wsname]);
    const sheetJsonNameID = XLSX.utils.sheet_to_json(workbook.Sheets[stdID]);
    console.log(sheetJsonNameGroup, sheetJsonNameID);
    const sheetJson = {
      filename: fileNamesTMP,
      sheetJsonNameGroup: sheetJsonNameGroup,
      sheetJsonNameID: sheetJsonNameID
    }

    //使用ajax来等文件处理之后通过axios发送给flask
    axios.post(`${ip}/app/endpoint`, sheetJson)
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


}

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


</script>

<template>
  <div class="top-section">
    <h2>首次使用,请上传学生分组信息的Excel表格</h2>
    <input ref="uploadInput" type="file" class="excelBox" @change="ExcelToJson" />
    <h2>上传上次生成的学生信息.json文件</h2>
    <input ref="uploadJson" type="file" class="excelBox" @change="" />
    <br>
  </div>

  <div class="class-manager-container">
    <classManager ref="classManagerRef"></classManager>
  </div>

</template>

<style scoped>
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
</style>
