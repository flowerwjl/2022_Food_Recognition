from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from Service.main import main_method

app = Flask(__name__, static_url_path="/")
app.config['UPLOAD_FOLDER'] = 'static/uploads/'


def fill_list(my_list: list, length, fill=None):  # 使用 fill字符/数字 填充，使得最后的长度为 length
    if len(my_list) >= length:
        return my_list
    else:
        return my_list + (length - len(my_list)) * [fill]


@app.route('/index', methods=['POST', 'GET'])
def upload():
    if request.method == "POST":
        upload_pic = request.files['pic']
        if upload_pic:
            filename = "new_pic.jpg"
            # 将文件保存到 static/uploads 目录
            upload_pic.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
            filepath = app.root_path + "/static/uploads/new_pic.jpg"
            foodnames, foodlists = main_method(filepath)
            for i in foodlists:
                i[3] = i[3].replace('\n', '<br />')
                i[5] = i[5].replace('\n', '<br />')
                i[6] = i[6].replace('\n', '<br />')
            return render_template("result.html", foodnames=foodnames, foodlists=foodlists)
        else:
            return "上传失败"
    return render_template("index.html")


@app.route('/detail', methods=['POST', 'GET'])
def detail():
    foodname = request.form['foodname']
    steps = request.form['steps']
    step_pics = request.form['step_pics']
    steps = steps.split('<br />')
    step_pics = step_pics.split('<br />')
    while '' in steps and step_pics:
        steps.remove('')
    while '' in steps and step_pics:
        step_pics.remove('')
    step_pics = fill_list(my_list=step_pics, length=len(steps))
    steps_n_pics = []
    for i in range(0, len(steps)):
        steps_n_pics.append([steps[i], step_pics[i]])
    return render_template("details.html", foodname=foodname, steps=steps_n_pics)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
