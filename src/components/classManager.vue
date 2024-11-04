<script>
import axios from 'axios';  

  export default {  
    data() {  
      return {  
        files:[],
        selectedFile:'',
        filename: '',  

        absentNames: '',  

        pkNum: '',  

        classNumber: '',  

        groupNumber: '',  

        resetFilename: '',  

        resultHtml: ''  
      };  
    },  
    methods: {
      fetchFiles(){
        axios.get('http://127.0.0.1:5000/find_files')  
          .then(response => {  
            this.files=response.data;
          })  
          .catch(error => {  
             console.log('获取文件列表失败')
          });  
      },  
      loadClass() {  
        axios.post('http://127.0.0.1:5000/load_class', { filename: this.selectedFile })  
          .then(response => {  
            alert(response.data.message);  
          })  
          .catch(error => {  
            alert(error.response.data.error);  
          });  
      },  
      markAbsent() {  
        const names = this.absentNames.split('，').map(name => name.trim()); 
        console.log(names) 
        axios.post('http://127.0.0.1:5000/mark_absent', {  
          names: names  
        }, {  
          headers: {  
            'Content-Type': 'application/json'  
          }  
        })  
        .then(response => {  
          alert(response.data.message);  
        })  
        .catch(error => {  
          if (error.response) {  
            alert(error.response.data.error);  
          } else {  
            // 处理网络错误等  
            alert('请求失败，请检查网络连接');  
          }  
        });  
      },
      generatePk() {  
        axios.post('http://127.0.0.1:5000/generate_pk', {  
          pk_num: this.pkNum,  
          class_number: this.classNumber,  
          filename: this.filename,  
          names_to_mark: [] // 根据需要传递  
        }, {  
          headers: {  
            'Content-Type': 'application/json'  
          }  
        })  
        .then(response => {  
          alert(response.data.message);  
        })  
        .catch(error => {  
          alert(error.response.data.error);  
        });  
      },  
      resetStudents() {  
        axios.post('http://127.0.0.1:5000/reset_students', { filename: this.resetFilename }, {  
          headers: {  
            'Content-Type': 'application/json'  
          }  
        })  
        .then(response => {  
          alert(response.data.message);  
        })  
        .catch(error => {  
          alert(error.response.data.error);  
        });  
      },  
      queryStatus() {  
        axios.post('http://127.0.0.1:5000/query_student_status', { group_number: this.groupNumber }, {  
          headers: {  
            'Content-Type': 'application/json'  
          }  
        })  
        .then(response => {  
          this.resultHtml = `<h3>学生状态</h3><ul>`;  
          response.data.forEach(student => {  
            this.resultHtml += `<li>${student.name}: ${student.program_status}, ${student.shoot_status}, 缺席次数: ${student.absent_times}</li>`;  
          });  
          this.resultHtml += '</ul>';  
        })  
        .catch(error => {  
          alert(error.response.data.error);  
        });  
      }  
    },  
    mounted() {  
      //this.fetchFiles();
      //this.loadClass();
      // 可以在这里执行任何需要在组件挂载后运行的代码  
    }  
  };  

</script>
<template>
    <h1>班级管理系统</h1>
    <div>
        <h2>加载班级数据</h2>
        <!--input type="text" id="filename" placeholder="输入班级文件名 (如 data.json)"-->
        <select if="file-selector" v-model="selectedFile">
          <option v-for="file in files" :key="file">{{ file }}</option>
        </select>
        <h5>调试*current files list:{{ files }}</h5>
        <h5>调试*chosen class:{{ selectedFile }}</h5>
        <button @click="loadClass">加载班级</button>
    </div>

    <div>
        <h2>标记缺席学生</h2>
        <input type="text" id="absent-names" v-model="absentNames" placeholder="输入缺席学生姓名(用逗号分隔)">

        <button @click="markAbsent">标记缺席</button>
    </div>

    <div>
        <h2>生成小组 PK</h2>
        <input type="text" id="pk-num" placeholder="输入第几次 PK">
        <input type="text" id="class-number" placeholder="输入班级号">
        <button @click="generatePk">生成 PK</button>
    </div>

    <div>
        <h2>查询学生状态</h2>
        <input type="text" id="group-number" placeholder="输入组号">
        <button @click="queryStatus">查询状态</button>
    </div>

    <div>
        <h2>重置学生状态</h2>
        <input type="text" id="reset-filename" placeholder="输入班级文件名 (如 data.json)">
        <button @click="resetStudents">重置状态</button>
    </div>


    <div id="result"></div>
</template>
<style>

</style>