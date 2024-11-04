from flask import Flask, Blueprint,request,jsonify,redirect, url_for, render_template, flash, send_from_directory  
from flask_cors import CORS
import json
import re
from datetime import datetime
import random
import os

global_filename=''
global_backup_path='./backupFile'
# global global_pkResult_name
# global_process_file
# global global_pkResult
global_pkResult_path=os.getcwd()




#设置全局变量

##########################
# 使用前确保终端在正确pwd
##########################

app=Flask(__name__)

CORS(app, origins=['http://localhost:5173'])  #指定前端地址以允许数据传递


#########################
# 接收并处理文件
# 接收文件的变量filenameAC
#########################

@app.route('/api/endpoint',methods=['POST'])
def api_endpoint():
    
    combined_data = request.json  
      
    # 分别获取两个 JSON 数据集  
    sheet_json_name_group = combined_data.get('sheetJsonNameGroup')  
    sheet_json_name_id = combined_data.get('sheetJsonNameID')  
    filenameAC=combined_data.get('filename')
    #tiaoshi  
    #print(sheet_json_name_group)  
    #print(sheet_json_name_id)  
    print(filenameAC)
    # 将数据保存到文件
    fpath1='stdData/sheet_json_name_group.json' 
    fpath2='stdData/sheet_json_name_id.json' 
    with open(fpath1, 'w', encoding='utf-8') as file:  
        json.dump(sheet_json_name_group, file, ensure_ascii=False, indent=4)  
      
    with open(fpath2, 'w', encoding='utf-8') as file:  
        json.dump(sheet_json_name_id, file, ensure_ascii=False, indent=4)  


    ''' with open('sheet_json_name_group.json', 'w', encoding='utf-8') as file:  
        json.dump(sheet_json_name_group, file, ensure_ascii=False, indent=4)  
      
    with open('sheet_json_name_id.json', 'w', encoding='utf-8') as file:  
        json.dump(sheet_json_name_id, file, ensure_ascii=False, indent=4)  '''
      

    '''# 过滤和整理数据的函数  
    filtered_group=[]  
    for item in sheet_json_name_group:  
        if "分组原则" in item["组号"] or "样例" in item["组号"] or "请所有同学按照以下分组原则" in item["组号"]:  
            continue  # 跳过不需要的内容  
        # 修正键名中的空格问题  
        #item["组长"] = item.pop("组长 ")  
        # 提取有用的信息  
        group_info = {  
            "组号": item["组号"],  
            "组长": item["组长"],  
            "组员": [  
                item.get(f"组员{i}", "未分配") for i in range(1, 6)  
            ]  
        } 
        filtered_group.append(group_info)  

    # 将处理后的数据保存为新的 JSON 文件  
    with open('processed_data.json', 'w', encoding='utf-8') as f:  
     json.dump(filtered_group, f, ensure_ascii=False, indent=4) '''
    
    filtered_group={}
    totalGroupNums=0
    supervisedG=0
    for group in sheet_json_name_group:
        if not re.match(r"第\d+组", group["组号"]):  
            continue
        group_id = (group['组号'].replace('第', '').replace('组', ''))
        totalGroupNums=int(group_id)
    print(totalGroupNums)
    # 遍历每个组  
    for group in sheet_json_name_group:  
        '''if "分组原则" in group["组号"] or "样例" in group["组号"] or "请所有同学按照以下分组原则" in group["组号"]:  
            continue  # 跳过不需要的内容  '''
        if not re.match(r"第\d+组", group["组号"]):  
            continue
        group_id = (group['组号'].replace('第', '').replace('组', ''))
        #group_id = (group['组号'].replace('第', '').replace('组', ''))
        # print(group_id)
        if group_id not in filtered_group:  
                filtered_group[group_id] = []    
                #filtered_group[group_id] = []  
        #groupMemberInfo=[]
        #print(int(group_id))
        mark=1
        supervisedG=(int(group_id))%totalGroupNums+1
 

        for i,(key,value) in enumerate(group.items(), start=1): 
            if key.startswith('组号'):  
                continue
            else:
                name=''
                
                if key.startswith('组长'):
                    name=value.split('（')[0]
                elif key.startswith('组员'):
                    name=value.split('（')[0]
                match = re.match(r'^([^（）()]+)', name)  
                if match:  
                    name = match.group(0).strip()   
                for std in sheet_json_name_id:
                    if std['姓名']==name:
                        studentID=std['学号']
                #if member: #or member["组员"] or member["组员2"] or member["组员3"] or member["组员4"]:
                filtered_group[group_id].append({
                #filtered_group[group_id].append=({
                    "group id":mark,  #这个group id是组内第几个，不是第几组
                    "name":name,  
                    "student id":studentID,  
                    "shoot": True,  
                    "program": True,  
                    "absent": False,
                    "absent times":0,
                    "supervised group":supervisedG
                    })
                mark=mark+1          
                          
    '''for i, member in enumerate(members, start=1.0):  
        name, info = member.split('（')  
        #sex_dorm = info.rstrip('）').split('-')  
        #student_sequence = int(sex_dorm[0])  
        student_id = 20235850#generate_student_id(202458501, student_sequence)  # 假设的student_id生成逻辑  
        
            # 添加到输出JSON中  
        if group_id not in  filtered_group:  
            filtered_group[f"{group_id:.1f}"] = []  
        
        filtered_group[f"{group_id:.1f}"].append({  
            "group id": i,  
            "name": name,  
            "student id": student_id,  
            "shoot": True,  
            "program": True,  
            "absent": False  
            })  '''
    filename_without_extension, extension = os.path.splitext(filenameAC) 
##################################################
# 设置全局变量方便使用
    global global_filename
    global_filename= filename_without_extension+'.json'
##################################################
    global global_process_file
    global_process_file=filtered_group #设置临时文件对象

    #存储信息的全局变量
    with open(f"{filename_without_extension}.json", 'w', encoding='utf-8') as f:
        json.dump(filtered_group, f, ensure_ascii=False, indent=4)
    with open(f"{filename_without_extension}_backup.json", 'w', encoding='utf-8') as f:  
        json.dump(filtered_group, f, ensure_ascii=False, indent=4) 
    # 返回响应给前端  
    return jsonify({"message": "文件接收成功,处理完成"}), 200


#########################
# 班级管理：加载班级
#########################
def load_data(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

def save_data(filename, data):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

def update_students(data):
    for group_id, students in data.items():
        all_program_false = all(not student["program"] for student in students)
        if all_program_false:
            for student in students:
                student["program"] = True

        all_shoot_false = all(not student["shoot"] for student in students)
        if all_shoot_false:
            for student in students:
                student["shoot"] = True

        for student in students:
            student['absent'] = False

#########################
# 班级管理：标记缺席
#########################
def mark_absent(data, names_to_mark):  
    valid_names = {student['name'] for group in data.values() for student in group}  
  
    for name in names_to_mark:  
        if name in valid_names:  
            for group_id, students in data.items():  
                for student in students:  
                    if student['name'] == name:  
                        student['absent'] = True  
                        # 确保 'absent times' 是一个整数，并增加1  
                        if 'absent times' not in student:  
                            student['absent times'] = 0  
                        student['absent times'] += 1
                        print(f"'{name}'缺席已标记")  
                        # 由于已经找到了学生并进行了修改，跳出内层循环 
                        break  # 跳出
            # 由于已经找到了学生并进行了修改，跳出外层循环 
        else:  
            print(f"警告: 名字 '{name}' 不在学生名单中。")
              
            
'''def mark_absent(data, names_to_mark):
    valid_names = {student['name'] for group in data.values() for student in group}

    for name in names_to_mark:
        if name in valid_names:
            for group_id, students in data.items():
                for student in students:
                    if student['name'] == name:
                        student['absent'] = True
                        student['absent times'] += 1
        else:
            print(f"警告: 名字 '{name}' 不在学生名单中。")'''
def write_absent_students_to_file(data, pk_num, class_number):
    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{class_number}_absent.txt"

    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"PK 第 {pk_num} 次缺席学生记录 - 日期: {current_date}\n")
            for group_id, students in data.items():
                absent_students = [student['name'] for student in students if student.get('absent', False)]
                if absent_students:
                    f.write(f"组 {group_id}: {', '.join(absent_students)}\n")
            f.write("\n")
        print(f"缺席学生信息已写入 {filename}")
    except IOError as e:
        print(f"写入文件时出错: {e}")

#########################
# 班级管理：生成小组pk
#########################

def select_programmers(data):
    selected_members = []
    all_eligible_members = []

    for group_key, group in data.items():
        eligible_members = [member for member in group if not member['absent']]
        all_eligible_members.extend(eligible_members)

    for group_key, group in data.items():
        group_index = int(group_key.split('.')[0])
        eligible_members = [member for member in group if not member['absent'] and member['program']]

        if eligible_members:
            selected = eligible_members[0]
        else:
            eligible_members = [member for member in group if not member['absent']]
            if eligible_members:
                max_absent_times = max(member.get('absent times', 0) for member in eligible_members)
                candidates = [member for member in eligible_members if member.get('absent times', 0) == max_absent_times]
                selected = random.choice(candidates)
            else:
                if all_eligible_members:
                    selected = random.choice(all_eligible_members)
                else:
                    continue

        selected_members.append((group_index, selected))
        selected['program'] = False
        selected['absent times'] = 0
    return selected_members

def write_results_to_file(selected_students, selected_photographers, pk_num, class_number):
    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{class_number}第{pk_num}次PK{current_date}.txt"
    global global_pkResult_name
    global_pkResult_name=filename

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("测试要求\n")
        f.write("（1）参赛同学可以操作机器提交代码，其他同学只能围观，不能操作机器。\n")
        f.write("组号\t\t\t参赛同学\t\t\t学号\n")

        for group_index, student in selected_students:
            f.write(f"第{group_index}组\t\t{student['name']}\t\t{student['student id']}\n")

        f.write("（2）监督同学\n")
        f.write("①负责监督被监督小组做题过程中是否存在作弊行为\n")
        f.write(f"②拍一张被监督小组做题的照片，证明正在做题的情形，命名 \"小组PK{pk_num}_组号_姓名.png\"\n")
        f.write("组号\t\t\t监督同学\t\t\t学号\t\t\t监督组号\n")

        for group_index, photographer in selected_photographers:
            f.write(
                f"第{group_index}组\t\t{photographer['name']}\t\t{photographer['student id']}\t\t{photographer['supervised group']}\n")
        global global_pkResult_path
        global_pkResult_path= os.path.join(os.getcwd(), filename)
        
    print(f"结果已保存到 {filename}")

def select_photographers(data, selected_programmers):
    selected_photographers = []
    selected_programmer_names = {student['name'] for _, student in selected_programmers}
    all_eligible_members = []

    for group_key, group in data.items():
        eligible_members = [member for member in group if not member['absent'] and member['name'] not in selected_programmer_names]
        all_eligible_members.extend(eligible_members)

    for group_key, group in data.items():
        group_index = int(group_key.split('.')[0])
        eligible_members = [member for member in group if not member['absent'] and member['shoot'] and member['name'] not in selected_programmer_names]

        if eligible_members:
            selected = eligible_members[0]
        else:
            eligible_members = [member for member in group if not member['absent'] and member['name'] not in selected_programmer_names]
            if eligible_members:
                max_absent_times = max(member.get('absent times', 0) for member in eligible_members)
                candidates = [member for member in eligible_members if member.get('absent times', 0) == max_absent_times]
                selected = random.choice(candidates)
            else:
                if all_eligible_members:
                    selected = random.choice(all_eligible_members)
                else:
                    continue

        selected_photographers.append((group_index, selected))
        selected['shoot'] = False
        if selected['absent times'] > 0:
            selected['absent times'] -= 1
    return selected_photographers

def backup_data(filename, data, pk_num, class_number):
    backup_folder = f"{class_number}备份"
    os.makedirs(backup_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = os.path.join(backup_folder, f"{os.path.splitext(os.path.basename(filename))[0]}_PK{pk_num}前_{timestamp}.json")

    try:
        with open(backup_filename, 'w', encoding='utf-8') as backup_file:
            json.dump(data, backup_file, ensure_ascii=False, indent=4)
        print(f"备份已保存到 {backup_filename}")
    except Exception as e:
        print(f"备份文件保存失败: {e}")


@app.route('/find_files',methods=['GET'])
def find_files():
    json_files =[f for f in os.listdir() if f.endswith('.json')]
    if not json_files:
        print("当前目录下没有找到任何 JSON 文件。")
        return jsonify({"当前目录下没有找到任何 JSON 文件。"})
    else:
        return jsonify(json_files)


@app.route('/load_class', methods=['POST'])
def load_class():
    
    tmpFileInfo = request.get_json()
    filename=tmpFileInfo.get('filename')
    if not filename:
        return jsonify({"error": "没有加载到有效文件"}), 400
    data = load_data(filename)

    global global_filename
    global_filename=filename
    '''global global_process_file
    global_process_file=data'''
    '''with open(global_filename,'r',encoding='utf-8') as f:
        global global_process_file
        global_process_file=f
        pass'''
    if not data:
        return jsonify({"error": "没有加载到有效的数据"}), 400
    return jsonify({"message": "班级数据加载成功", "data": data})

@app.route('/mark_absent', methods=['POST'])
def mark_absent_students():
    data=load_data(global_filename)#global_process_file
    print('processing:'+global_filename)
    #with open(global_filename,'w') as data:
    names_to_mark = request.get_json().get('names')
    if not data:
        return jsonify({"error": "无效的输入数据"}), 400

    mark_absent(data, names_to_mark)
        #json.dump(data,data, ensure_ascii=False, indent=4)
        # 将处理后的数据保存为新的 JSON 文件  
    #save_data(global_filename, data)
    with open(global_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    data=load_data(global_filename)
    '''data=load_data(global_filename)
    print('processing: '+global_filename)
    #with open(global_filename,'w') as data:
    names_to_mark = request.get_json().get('names')
    if not data:
        return jsonify({"error": "无效的输入数据"}), 400

    mark_absent(data, names_to_mark)
    # 将处理后的数据保存为新的 JSON 文件  
    save_data(global_filename, data)  # 假设数据保存到 data.json'''
    return jsonify({"message": "缺席学生已标记"})
    
@app.route('/generate_pk', methods=['POST'])
def generate_pk():
    class_number = request.json.get('class_number')
    pk_num = request.json.get('pk_num')
    #print(class_number+'  '+pk_num)
    filename = global_filename#request.json.get('filename')
    data=load_data(global_filename)#global_process_file
    #data =load_data(filename)
    if not data:
        return jsonify({"error": "没有加载到有效的数据"}),
    backup_data(filename, data, pk_num, class_number)

    update_students(data)

    #names_to_mark = request.json.get('names_to_mark', [])
    #mark_absent(data, names_to_mark)
    #save_data(filename, data)
    with open(global_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    for group in data.values():
        for student in group:
            student['absent'] = False
    selected_students = select_programmers(data)
    selected_photographers = select_photographers(data, selected_students)

    # 保存更新后的数据
    #save_data(filename, data)
    with open(global_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    write_results_to_file(selected_students, selected_photographers, pk_num, class_number) #生成结果以及发送给前端 
    data=load_data(global_filename)
    return jsonify({"message": "小组 PK 生成完成"})

@app.route('/download_pkResult',methods=['GET'])
def downloadPkResult():
     # 处理 GET 请求以下载文件  
    file_path =global_pkResult_path
    if os.path.isfile(file_path):  
        return send_from_directory(global_pkResult_path, global_pkResult_name, as_attachment=True)  
    else:  
        return jsonify({"error": "文件未找到"}), 404 
   # return send_from_directory(global_pkResult_path,global_pkResult_name, as_attachment=True)  
    
    #return send_from_directory(global_pkResult, filename, as_attachment=True) #让前端下载pk结果

@app.route('/reset_students', methods=['POST'])
def reset_students():
    filename =global_filename
    data = load_data(filename)

    if not data:
        return jsonify({"error": "没有加载到有效的数据"}), 400

    for group_id, students in data.items():
        for student in students:
            student['shoot'] = True
            student['program'] = True

    save_data(filename, data)  # 保存更新后的数据
    return jsonify({"message": "所有学生的 shoot 和 program 值已重置为 True"})


@app.route('/query_student_status', methods=['POST'])
def query_student_status_route():
    group_number = request.json.get('group_number')
    data = load_data(global_filename)  
    group_key =str(group_number)
    print(group_key)
    if group_key not in data:
        return jsonify({"error": f"警告: 组 {group_number} 不存在。"}), 400

    students=data[group_key]
    status_list = []
    for student in students:
        name = student['name']
        program_status = "可以比赛" if student['program'] else "不可比赛"
        shoot_status = "可以监督" if student['shoot'] else "不可监督"
        absent_times = student['absent times']#.get('absent times', 0)
        status_list.append({
            "name": name,
            "program_status": program_status,
            "shoot_status": shoot_status,
            "absent_times": absent_times
        })
    print(status_list)
    return jsonify(status_list)




#########################
# 班级管理：查询学生状态
#########################

#########################
# 班级管理：重置学生状态
#########################
    
if __name__=='__main__':
    app.run(debug=True)