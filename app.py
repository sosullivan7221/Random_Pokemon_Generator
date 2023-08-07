from flask import Flask, render_template
import pandas as pd
from flask import request
import random


app = Flask(__name__)



@app.route('/', methods = ['GET', 'POST'])
def home():
    global poke_data
    poke_data = pd.read_csv('Pokedex_Ver_SV2.csv')
    # if the request is a POST request then we will get the data from the form
    if request.method == 'POST':
        global dataForm
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
        poke_data = poke_data[poke_data['No'] == dataForm['number']]
        print('Data selected: ', poke_data.to_dict('records'))
        return render_template('results.html', data = poke_data)

    return render_template('home.html')

@app.route('/results', methods = ['GET', 'POST'])
def results():
    poke_data_HP = pd.read_csv('Pokedex_Ver_SV2.csv')
    if request.method == 'POST':
        dataForm2 = request.form
        print('Data from form: ', dataForm2)
        
        if dataForm2 == {}:
            dataForm2 = poke_data_HP
            print('Stat Selected: ', dataForm2.values)
        
        poke_data_HP = poke_data_HP[poke_data_HP.values['HP'] == poke_data.values['HP']]
        print('HP Selected: ', poke_data_HP.to_dict('records'))
        return render_template('home.html', data = poke_data_HP)
    
    return render_template('results.html')

app.run(host = '0.0.0.0', port = 8080, debug = True, use_reloader = True)
