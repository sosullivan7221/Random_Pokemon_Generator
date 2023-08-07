from flask import Flask, render_template
import pandas as pd
from flask import request
import random


app = Flask(__name__)



@app.route('/', methods = ['GET', 'POST'])
def home():
    data = pd.read_csv('Pokedex_Ver_SV2.csv')
    # if the request is a POST request then we will get the data from the form
    if request.method == 'POST':
        dataForm = request.form
        print('Data from form: ', dataForm)
        ## if data from form is a empty dictionary, lets select a random number betweeen 1 and 1000
        if dataForm == {}:
            dataForm = {'number': random.randint(1,1010)}
            print('Random number selected: ', dataForm['number'])
        else:
            print('....')
        # convert random number to a string
        # dataForm['number'] = str(dataForm['number'])
        # get matching row from data where the number is equal to the number from the form
        data = data[data['No'] == dataForm['number']]
        print('Data selected: ', data.to_dict('records'))
        return render_template('results.html', data = data)

    return render_template('home.html')

@app.route('/results')
def results():
    return render_template('results.html')

app.run(host = '0.0.0.0', port = 8080, debug = True, use_reloader = True)
