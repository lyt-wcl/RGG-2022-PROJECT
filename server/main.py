# 对前端的细节比较不熟悉，所以没有写处理搜索和处理搜索框
# 如果是单纯的根据药名和属性名搜索，直接调用getMedicine这个函数
# 如果要实现模糊搜索，应该是先使用倒排索引返回一个id列表，再根据getMedicineById这个函数进行搜索

from flask import Flask, jsonify, render_template
from db_manager import getMedicine
from db_manager import randomName

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/medicines/<medicine_name>")
def getMedicines(medicine_name):
    tags = []
    # 属性为空表示返回所有属性
    medicine = getMedicine(medicine_name, tags)
    if medicine['Image'] is not None:
        img_stream = medicine['Image'].decode('ascii')
        medicine['Image'] = img_stream

    return render_template('index.html', medicine=medicine)


@app.route("/radom/")
def radomMessage():
    # medicine是一个字典，里面有除了image之外的药材所有属性
    medicine = randomName()
    if medicine['Image'] is not None:
        img_stream = medicine['Image'].decode('ascii')
        medicine['Image'] = img_stream

    return jsonify(medicine)


#处理输入框
@app.route("/preProcess")
def preProcess():
    pass


#处理搜索
@app.route("/search/")
def search():
    pass


@app.route("/")
def index():
    medicine = randomName()
    # print(len(dict))
    # print(dict['Image'])

    img_stream = medicine['Image'].decode('ascii')
    medicine['Image'] = img_stream

    # 以下是flask使用的jinja2模板的写法，
    return render_template('index.html', medicine=medicine)


if __name__ == "__main__":
    app.run()
