Hello!

This is an attempt to create a Pokemon Stat Generator! The goal is to have a Pokemon randomly generated and allow the user to select the stat they want from the Pokemon.
The end result should be six chosen stat values from six randomly generated Pokemon.

Jupyter notebook is being used for testing code and for easier readbility, which the final version will be stored in 'pokemon.py'. HTML template is WIP, will be worked on once function works properly.

Current Issues/To Do:

1. The variable 'Random_Pokemon' is defined outside of the functions. I want it to be defined inside of the 'Generator' function, but doing so causes the stat functions to generate a random value from the DF rather than the value matching the output of the 'Generator' function.
    1a. Resolved! Used global function to store the Random_Pokemon variable and each stat globally, allowing for stat functions to pull the correct value and store it.

2. The 'Total-Stat' function has issues, it seems to be that the value for each stat function is not stored when the function is run, but stored when the Generator function is run.
    2a. Resolved! This was easily fixed once the global function was used to store the values. The stat values can be summed easily.

3. Mapping these python functions to html buttons to display the results. Most resources have examples for the user inputting data, not sure how to map the function so it displays the stored value.

4. Add a reset function to reset any stored values.

5. Prevent Stat functions from being run if there is already a stored varaible. Can be run again once reset button is used.