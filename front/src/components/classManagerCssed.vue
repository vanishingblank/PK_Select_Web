<script>
import axios from 'axios';

export default {
  data() {
    return {
      files: [],
      selectedFile: '',//要加载的班级名称
      filename: '',  //发送到后端的文件名变量

      absentNames: '',  //缺席学生

      pkNum: '',  //pk的次数

      classNumber: '',  //pk的班级

      groupNumber: '', //查询学生状态的组数

      resultTxtHref: null,//下载结果的链接

      resultTxtName: '',//结果文件名

      resDownloaded:false,

      dlfilename: '',

      resetFilename: '',

      resultHtml: ''  //显示查询结果的变量

    };
  },
  methods: {
    fetchFiles() {
      axios.get('http://192.168.1.235:5000/find_files')
        .then(response => {
          this.files = response.data;
        })
        .catch(error => {
          console.log('获取文件列表失败')
        });
    },
    loadClass() {
      axios.post('http://192.168.1.235:5000/load_class', { filename: this.selectedFile })
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
      axios.post('http://192.168.1.235:5000/mark_absent', {   //原本是127.0.0.1：5000，现在更改成控制台显示的与前端的相同
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
      axios.post('http://192.168.1.235:5000/generate_pk', {
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
          //console.log('result:'+response.data.filename)
          this.resultTxtName = response.data.filename
          alert(response.data.message);
        })
        .catch(error => {
          alert(error.response.data.error);
        });
      /*axios.get('http://192.168.1.235:5000/generate_pk')  
        .then(response => {  
          this.resultTxtName=response.data.name;
        })  
        .catch(error => {  
           console.log('获取文件列表失败')
        });  */

    },
    downloadFile() {
      axios.get('http://192.168.1.235:5000/download_pkResult')
        .then(Response=> {
          const blob =new Blob([Response.data],{type:'text/plain'});
          this.resultTxtHref = URL.createObjectURL(blob);
          this.resDownloaded=true;
        })
        .catch(error => {
          console.log('获取文件列表失败')
        });
        
    },

    /* async generatePk() {  
     try {  
       const response = await axios.post('http://192.168.1.235:5000/generate_pk', {  
         pk_num: this.pkNum,  
         class_number: this.classNumber,  
         filename: this.filename,  
         names_to_mark: [] // 根据需要传递  
       }, {  
         headers: {  
           'Content-Type': 'application/json'  
         }  
       });  
       const { message, filename } = response.data;  
       alert(message);  
   
         // 下载文件  
       window.location.href=`http://192.168.1.235:5000/download_pkResult`;  
      
     } catch (error) {  
       alert('生成或下载过程中出错: ' + error.response.data.error);  
     }  
   },*/
    resetStudents() {
      axios.post('http://192.168.1.235:5000/reset_students', { filename: this.resetFilename }, {
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
      axios.post('http://192.168.1.235:5000/query_student_status', { group_number: this.groupNumber }, {
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
          this.$refs.resultContainer.innerHTML = this.resultHtml;
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
  },
  beforeDestroy() {
    // Clean up the URL object when the component is destroyed  
    if (this.resultTxtHref) {
      URL.revokeObjectURL(this.resultTxtHref);
    }
  },
};

</script>

<template>
  <div>
    <div class="local-student-info">
      <h2>读取本地学生信息</h2>
      <input type="file" @change="handleFileUpload" class="file-input" style="display:none;" ref="fileInput">
      <button @click="triggerFileUpload" class="upload-button">读取本地</button>
      
    </div>

    

    <!-- 分隔线 -->
    <div class="separator"></div>

    <!-- 班级管理系统板块 -->
    <div class="class-management-section">
      <h1>班级管理系统</h1>
      <div>
        <h2>加载班级数据</h2>
        <select v-model="selectedFile">
          <option v-for="file in files" :key="file">{{ file }}</option>
        </select>
        <h5>调试*current files list:{{ files }}</h5>
        <h5>调试*chosen class:{{ selectedFile }}</h5>
        <button @click="loadClass">加载班级</button>
      </div>
      <br>
      <div>
        <h2>标记缺席学生</h2>
        <input type="text" id="absent-names" v-model="absentNames" placeholder="输入缺席学生姓名(用逗号分隔)">
        <button @click="markAbsent">标记缺席</button>
      </div>
      <br>
      <div>
        <h2>生成小组 PK</h2>
        <input type="text" id="pk-num" placeholder="输入第几次 PK" v-model="pkNum">
        <input type="text" id="class-number" placeholder="输入备注" v-model="classNumber">
        <button @click="generatePk">生成 PK</button>
        <a :href="resultTxtHref" :download="resultTxtName" @click.prevent="downloadFile">点击此处下载结果:{{ resultTxtName }}</a>
      </div>
      <br>  
      <div>
        <h2>查询学生状态</h2>
        <input type="text" id="group-number" placeholder="输入组号" v-model="groupNumber">
        <button @click="queryStatus">查询状态</button>
      </div>
      <div ref="resultContainer"></div> <!--显示学生状态-->
      <br>
      <div>
        <h2>*调试*重置学生状态</h2>
        <input type="text" id="reset-filename" placeholder="输入班级文件名 (如 data.json)">
        <button @click="resetStudents">重置状态</button>
      </div>
    </div>

    <div id="result"></div>
  </div>
</template>


<style scoped>
  /* 分隔线样式 */
  .separator {
    height: 20px;
    width: 100%;
    background-color: #f0f0f0;
    border-bottom: 1px solid #ccc;
    margin-bottom: 20px;
  }

  /* 班级管理系统板块的样式 */
  .class-management-section {
    padding: 20px;
    background-color: #f9f9f9; /* 稍浅的背景色，但保持柔和 */
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
  }

  /* 内部的标题和输入框样式 */
  .class-management-section h1,
  .class-management-section h2 {
    color: #212529; /* 更深的标题颜色，提高对比度 */
  }

  .class-management-section input,
  .class-management-section select,
  .class-management-section button,
  .class-management-section a {
    margin: 5px 0;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
    color: #212529; /* 确保所有输入元素的文本颜色都具有足够的对比度 */
  }

  .class-management-section button {
    background-color: #007bff;
    color: white; /* 按钮文字保持白色，因为背景色较深 */
    cursor: pointer;
  }

  .class-management-section button:hover {
    background-color: #0056b3; /* 悬停时背景色变深，但文字仍为白色 */
  }

  /* 下载链接样式 */
  .class-management-section a {
    color: #007bff; /* 链接颜色保持蓝色，但确保与背景有足够的对比度 */
    text-decoration: none;
    margin-left: 10px;
  }

  .class-management-section a:hover {
    text-decoration: underline;
  }

  /* 调试信息的样式，确保清晰可见 */
  .class-management-section h5 {
    color: #6c757d; /* 使用灰色，但确保与背景有足够的对比度 */
  }

  /* 结果容器的样式（如果需要） */
  .class-management-section #resultContainer {
    margin-top: 20px;
    padding: 10px;
    background-color: #fff; /* 如果需要显示内容，可以使用白色背景 */
    border: 1px solid #ddd;
    border-radius: 4px;
  }

  .local-student-info {
    margin-bottom: 20px; /* 增加底部间距，与其他部分分隔 */
  }
 
  .local-student-info h2 {
    color: #212529; /* 与其他标题颜色一致 */
  }
 
  .upload-button {
    margin-top: 10px; /* 增加顶部间距，使布局更美观 */
    padding: 8px 16px; /* 与其他按钮的间距一致 */
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
    color: white;
    background-color: #007bff;
    cursor: pointer;
  }
 
  .upload-button:hover {
    background-color: #0056b3; /* 悬停时背景色变深 */
  }
 
  .file-input {
    display: none; /* 隐藏文件输入框 */
  }
 
  .student-data-preview {
    margin-top: 10px; /* 增加顶部间距 */
    padding: 10px;
    background-color: #f9f9f9; /* 与班级管理系统板块背景色一致 */
    border: 1px solid #ddd;
    border-radius: 4px;
    max-height: 200px; /* 限制预览区域的高度，避免内容过多 */
    overflow-y: auto; /* 允许垂直滚动 */
  }
 
  .student-data-preview pre {
    font-size: 14px; /* 与其他输入元素的字体大小一致 */
    color: #212529; /* 与其他文本颜色一致 */
    margin: 0; /* 移除默认的内外边距 */
  }
</style>