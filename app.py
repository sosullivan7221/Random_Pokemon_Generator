from flask import Flask, render_template
import pandas as pd
from flask import request
import random
import logging


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    poke_data = pd.read_csv('Pokedex_Ver_SV2.csv')
    
    if request.method == 'POST':
        dataForm = request.form
        print(f"Data from form: %s", dataForm)
        
        if not dataForm:
            dataForm = {'number': random.randint(1, 1010)}
            print(f"Random number selected: %s", dataForm['number'])
            
        local_data = poke_data.query(f'No == {int(dataForm["number"])}')
        print(f"Data selected: %s", local_data.to_dict('records'))
        
        poke_data = local_data.copy()
        
        return render_template('results.html', data=local_data)
    return render_template('home.html') 

@app.route('/results', methods = ['GET', 'POST'])
def results():
    return render_template('results.html', data=poke_data)
 
@app.route('/choices', methods = ['GET', 'POST'])
def choices():
    return render_template('choices.html', data = poke_data)


app.run(host = '0.0.0.0', port = 8080, debug = True, use_reloader = True)

