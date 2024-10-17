from flask import Flask, request, redirect, url_for, render_template, flash, send_from_directory  
import os  
  
app = Flask(__name__)  
app.config['UPLOAD_FOLDER'] = 'uploads/'  
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','xls','xlsx','xlsb','xlsm','xlst'} #限制上传的文件类型 
app.secret_key = 'supersecretkey'  # 用于 flash 消息  
  
if not os.path.exists(app.config['UPLOAD_FOLDER']):  
    os.makedirs(app.config['UPLOAD_FOLDER'])  
  
def allowed_file(filename):  
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']  
  
@app.route('/')  
def upload_form():  
    return render_template('upload.html')  
  
@app.route('/', methods=['POST'])  
def upload_file():  
    # 检查是否有文件部分在请求中  
    if 'file' not in request.files:  
        flash('No file part')  
        return redirect(request.url)  
    file = request.files['file']  
    # 如果用户没有选择文件  
    if file.filename == '':  
        flash('No selected file')  
        return redirect(request.url)  
    if file and allowed_file(file.filename):  
        filename = file.filename  
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  #文件储存位置
        flash('File successfully uploaded')  
        #return redirect(url_for('uploaded_file', filename=filename))  
        return render_template('upload.html')  
    else:  
        flash('Allowed txt pdf, png, jpg, jpeg, gif,xls,xlsx,xlsb,xlsm,xlst')  
        return redirect(request.url)  
  
@app.route('/uploads/<filename>')  
def uploaded_file(filename):  
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)  
  
if __name__ == '__main__':  
    app.run(debug=True)