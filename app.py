from flask import Flask, render_template
import pandas as pd
from flask import request
import random


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
    global poke_data
    poke_data = pd.read_csv('Pokedex_Ver_SV2.csv')

    if request.method == 'POST':
        dataForm = request.form
        print('Data from form: ', dataForm)

        if dataForm == {}:
            dataForm = {'number': random.randint(1, 1010)}
            print('Random number selected: ', dataForm['number'])
        else:
            selected_stat = dataForm.get('selected_stat')  # Get the selected stat
            print('Selected Stat: ', selected_stat)

            if selected_stat:
                # Get the value of the selected stat
                selected_stat_value = poke_data[selected_stat].values[0]

                # You can add the selected value to the home template context
                selected_value = {'selected_stat': selected_stat, 'value': selected_stat_value}
                return render_template('home.html', selected_value=selected_value)

        poke_data = poke_data[poke_data['No'] == dataForm['number']]
        print('Data selected: ', poke_data.to_dict('records'))

    return render_template('home.html')

@app.route('/results', methods = ['GET', 'POST'])
def results():
     return render_template('results.html', data = poke_data)


app.run(host = '0.0.0.0', port = 8080, debug = True, use_reloader = True)
