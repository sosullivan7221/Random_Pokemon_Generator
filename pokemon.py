## Packages
import pandas as pd
import numpy as np

## Importing Pokedex Data
poke_data = pd.read_csv('Pokedex_Ver_SV2.csv')

#Select random Pokemon from the Pokedex
Random_Pokemon = poke_data['Name'].sample(n=1)

#Generator Function

def Generator():
    
    # Return the random Pokemon
    return Random_Pokemon

def HP():
    # Display the HP of the Pokemon selected from the generator function
     HP_Stat = poke_data['HP'].loc[poke_data['Name'] == Generator().values[0]]
     
     # Return the HP sat
     return HP_Stat

def Attack():
    # Display the attack of the Pokemon selected from the generator function
    Attack_Stat = poke_data['Attack'].loc[poke_data['Name'] == Generator().values[0]]
     
    # Return the attack stat
    return Attack_Stat

def Defense():
    # Display the defense of the Pokemon selected from the generator function
    Defense_Stat = poke_data['Defense'].loc[poke_data['Name'] == Generator().values[0]]
    
    # Return the defense stat
    return Defense_Stat

def SP_Attack():
    # Display the special attack of the Pokemon selected from the generator function
    SP_Attack_Stat = poke_data['SP_Attack'].loc[poke_data['Name'] == Generator().values[0]]
    
     # Return the special attack stat
    return SP_Attack_Stat

def SP_Defense():
    # Display the special defense of the Pokemon selected from the generator function
    SP_Defense_Stat = poke_data['SP_Defense'].loc[poke_data['Name'] == Generator().values[0]]
    
    # Return the special defense stat
    return SP_Defense_Stat

def Speed():
    # Display the speed of the Pokemon selected from the generator function
    Speed_Stat = poke_data['Speed'].loc[poke_data['Name'] == Generator().values[0]]
    
    # Return the speed stat
    return Speed_Stat
