from flask import Flask, render_template #? url_for
import csv, arsAge, sys, os
# from grogs import Grog, csvGrog

# Constants
COV_FOLDER = "covenants"

app = Flask(__name__)

## TODO Display listed grogs in covenant when selected
## TODO Make buttons on COV do something
## TODO actually update save data
## TODO Make new covenants

@app.route('/')
def index():
    covenants = [cov[:-4] for cov in os.listdir(COV_FOLDER) if cov.endswith('.tsv')]
    return render_template('index.html', covenants=covenants)

@app.route('/cov/<name>')
def covenant(name):
    grogs = ['1','2']
    return render_template('covenant.html', grogs=grogs, name=name)

if __name__ == '__main__':
    app.run(debug = True)