from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_me():
    return render_template('hello.html')

@app.route('/hello/<cov>')
def hello_name(cov):
    return render_template('hello.html', covenant=cov)

if __name__ == '__main__':
    app.run(debug = True)