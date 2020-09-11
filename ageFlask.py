from flask import Flask, render_template #? url_for
import csv, arsAge, sys, os
from grogs import Grog, csvGrog

# Constants
COV_FOLDER = "covenants"

app = Flask(__name__)

## TODO Make buttons on COV do something
## TODO actually update save data
## TODO Make new covenants

@app.route('/')
def index():
    covenants = [cov[:-4] for cov in os.listdir(COV_FOLDER) if cov.endswith('.tsv')]
    return render_template('index.html', covenants=covenants)

@app.route('/cov/<cov>')
def covenant(cov):
    grogs = loadCovenant(cov)
    return render_template('covenant.html', grogs=grogs, cov=cov)

def loadCovenant(covenant):
    grogFile = open(os.path.join(COV_FOLDER, covenant + '.tsv'))
    grogReader = csv.reader(grogFile, delimiter='\t')

    cov_grogs = {}
    grogData = list(grogReader)

    for g in grogData:
        cov_grogs[g[0].lower()] = csvGrog(g)
    grogFile.close()
    return cov_grogs

if __name__ == '__main__':
    app.run(debug = True)