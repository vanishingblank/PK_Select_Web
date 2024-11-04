<script setup>
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
    axios.post('http://127.0.0.1:5000/api/endpoint', sheetJson)
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
  



</script>

<template>
  <h1>请上传学生分组信息的Excel表格</h1>
  <h3>（上传文件以载入学生数据）</h3>
  <input ref="uploadInput" type="file" class="excelBox" @change="ExcelToJson" />
  <br>
  <classManager ref="classManagerRef"></classManager>
</template>

<style scoped></style>
