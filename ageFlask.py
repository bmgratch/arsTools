from flask import Flask, render_template #? url_for

app = Flask(__name__)

grogs = ['1','2']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cov/<name>')
def hello_name(name):
    return render_template('covenant.html', grogs=grogs)

if __name__ == '__main__':
    app.run(debug = True)