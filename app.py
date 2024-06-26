from flask import Flask, render_template

app = Flask(__name__)
app.run(debug=True)


# 调查问卷项目
@app.route('/practise1')
def practice1_html():  # put application's code here
    return render_template('practise1/practise1.html')

# 盒子模型
@app.route('/practise2')
def practice2_html():  # put application's code here
    return render_template('practise2/practise2.html')

# 弹性盒模型
@app.route('/practise3')
def practice3_html():  # put application's code here
    return render_template('practise3/practise3.html')

# 学习排版
@app.route('/practise4')
def practice4_html():
    return render_template('practise4/practise4.html')


if __name__ == '__main__':
    app.run()
