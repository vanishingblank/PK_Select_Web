
<!-- <script setup>
import { ref } from 'vue'
import axios from 'axios'
import * as XLSX from 'xlsx'
import classManager from './components/classManager.vue';

const uploadInput=ref(null)
const classManagerRef=ref(null)
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

    const wsname = workbook.SheetNames[0];
    //分组状况

    const stdID = workbook.SheetNames[3];
    //学号sheet,如表格变动可能要手动调整

    const sheetJsonNameGroup = XLSX.utils.sheet_to_json(workbook.Sheets[wsname]);
    const sheetJsonNameID = XLSX.utils.sheet_to_json(workbook.Sheets[stdID]);
    console.log(sheetJsonNameGroup, sheetJsonNameID);
    const sheetJson = {
      filename: fileNamesTMP,
      sheetJsonNameGroup: sheetJsonNameGroup,
      sheetJsonNameID: sheetJsonNameID
    }

    //使用ajax来等文件处理之后通过axios发送给flask
    axios.post('http://192.168.1.235:5000/app/endpoint', sheetJson)
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
  <h1>首次使用,请上传学生分组信息的Excel表格</h1>
  <input ref="uploadInput" type="file" class="excelBox" @change="ExcelToJson" />
  <h1>*已使用,请上传上次生成的学生信息.json文件</h1>
  <input ref="uploadJson" type="file" class="excelBox" @change="" />
  <br>
  <classManager ref="classManagerRef"></classManager>
</template>

<style scoped></style>
<template>
  <div>
    <button class="btn btn-primary">Primary Button</button>
    <button class="btn btn-secondary">Secondary Button</button>
  </div>
</template>

<script>
export default {
  name: 'ButtonExample',
};
</script>
<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavbarExample',
};
</script>
<template>
  <div class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">Card title</h5>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CardExample',
};
</script> -->

<template>
  <div class="container">
    <div class="top-section">
      <h1>首次使用,请上传学生分组信息的Excel表格</h1>
      <input ref="uploadInput" type="file" class="excelBox" @change="ExcelToJson" />
      <h1>*已使用,请上传上次生成的学生信息.json文件</h1>
      <input ref="uploadJson" type="file" class="excelBox" />
      <br>

      <div>
        <button class="btn btn-primary">Primary Button</button>
        <button class="btn btn-secondary">Secondary Button</button>
      </div>

      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item active">
              <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Features</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Pricing</a>
            </li>
          </ul>
        </div>
      </nav>

      <div class="card" style="width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
      </div>
    </div>

    <div class="class-manager-container">
      <classManager ref="classManagerRef"></classManager>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue'
import axios from 'axios'
import * as XLSX from 'xlsx'
import classManager from './components/classManager.vue';

const uploadInput = ref(null)
const classManagerRef = ref(null)

const ExcelToJson = (e) => {
  let fileObj = e.target.files[0]
  const fileReader = new FileReader();
  const fileNamesTMP = e.target.files[0].name
  fileReader.readAsArrayBuffer(fileObj);
  fileReader.onload = (event) => {
    const fileData = event.target.result;
    const workbook = XLSX.read(fileData, { type: 'binary' })
    const wsname = workbook.SheetNames[0];
    const stdID = workbook.SheetNames[3];
    const sheetJsonNameGroup = XLSX.utils.sheet_to_json(workbook.Sheets[wsname]);
    const sheetJsonNameID = XLSX.utils.sheet_to_json(workbook.Sheets[stdID]);
    const sheetJson = {
      filename: fileNamesTMP,
      sheetJsonNameGroup: sheetJsonNameGroup,
      sheetJsonNameID: sheetJsonNameID
    }

    axios.post('http://192.168.1.235:5000/app/endpoint', sheetJson)
      .then(response => {
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
</script>


<style scoped>
/* 样式重置 */
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
  background-color: #f0f0f0; /* 更浅的背景色 */
}

.top-section h1 {
  color: #333; /* 更深的文本色 */
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
  background-color: #fff; /* 保持白色背景 */
}

.card-title, .card-text {
  color: #333; /* 更深的文本色 */
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
.btn {
  display: inline-block;
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
}

.btn-primary {
  background-color: #0056b3; /* 更深的蓝色 */
  color: white;
}

.btn-secondary {
  background-color: #5a6268; /* 更深的灰色 */
  color: white;
}

.btn:hover {
  opacity: 0.9;
}
</style>


