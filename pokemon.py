## Packages
import pandas as pd
import numpy as np

## Importing Pokedex Data
poke_data = pd.read_csv('Pokedex_Ver_SV2.csv')

#Generator Function

def Generator():
    # Selecting random Pokemon from the Pokedex
    global Random_Pokemon
    Random_Pokemon = poke_data['Name'].sample(n=1)
    # Return the random Pokemon
    return Random_Pokemon

def HP():
    # Display the HP of the Pokemon selected from the generator function
     global HP_Stat
     HP_Stat = poke_data['HP'].loc[poke_data['Name'] == Random_Pokemon.values[0]]
     
     # Return the HP sat
     return HP_Stat

def Attack():
    # Display the attack of the Pokemon selected from the generator function
    global Attack_Stat
    Attack_Stat = poke_data['Attack'].loc[poke_data['Name'] == Random_Pokemon.values[0]]
     
    # Return the attack stat
    return Attack_Stat

def Defense():
    # Display the defense of the Pokemon selected from the generator function
    global Defense_Stat
    Defense_Stat = poke_data['Defense'].loc[poke_data['Name'] == Random_Pokemon.values[0]]
    
    # Return the defense stat
    return Defense_Stat

def SP_Attack():
    # Display the special attack of the Pokemon selected from the generator function
    global SP_Attack_Stat
    SP_Attack_Stat = poke_data['SP_Attack'].loc[poke_data['Name'] == Random_Pokemon.values[0]]
    
     # Return the special attack stat
    return SP_Attack_Stat

def SP_Defense():
    # Display the special defense of the Pokemon selected from the generator function
    global SP_Defense_Stat
    SP_Defense_Stat = poke_data['SP_Defense'].loc[poke_data['Name'] == Random_Pokemon.values[0]]
    
    # Return the special defense stat
    return SP_Defense_Stat

def Speed():
    # Display the speed of the Pokemon selected from the generator function
    global Speed_Stat
    Speed_Stat = poke_data['Speed'].loc[poke_data['Name'] == Random_Pokemon.values[0]]
    
    # Return the speed stat
    return Speed_Stat

def Total():
    # Display the sum of the chosen stats from the stat function
    global Total_Stat
    Total_Stat = [HP_Stat.values[0] + Attack_Stat.values[0] + Defense_Stat.values[0] + SP_Attack_Stat.values[0] + SP_Defense_Stat.values[0] + Speed_Stat.values[0]]
    
     # Return the total stat
    return Total_Stat


Generator()

HP()
Attack()
Defense()
SP_Attack()
SP_Defense()
Speed()

Total()

