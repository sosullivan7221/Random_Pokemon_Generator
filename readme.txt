Hello!

This is an attempt to create a Pokemon Stat Generator! The goal is to have a Pokemon randomly generated and allow the user to select the stat they want from the Pokemon.
The end result should be six chosen stat values from six randomly generated Pokemon.

Jupyter notebook is being used for testing code and for easier readbility, which the final version will be stored in 'pokemon.py'. HTML template is WIP, will be worked on once function works properly.

Currently Deployed On Render.com: https://pokemon-stat-generator.onrender.com/  (Note: none of the html functionality is live yet, can use that link to track html process although it may be slow for the time being.)

Current Issues/To Do:

1̶.̶ T̶h̶e̶ v̶a̶r̶i̶a̶b̶l̶e̶ '̶R̶a̶n̶d̶o̶m̶_̶P̶o̶k̶e̶m̶o̶n̶'̶ i̶s̶ d̶e̶f̶i̶n̶e̶d̶ o̶u̶t̶s̶i̶d̶e̶ o̶f̶ t̶h̶e̶ f̶u̶n̶c̶t̶i̶o̶n̶s̶.̶ I̶ w̶a̶n̶t̶ i̶t̶ t̶o̶ b̶e̶ d̶e̶f̶i̶n̶e̶d̶ i̶n̶s̶i̶d̶e̶ o̶f̶ t̶h̶e̶ '̶G̶e̶n̶e̶r̶a̶t̶o̶r̶'̶ f̶u̶n̶c̶t̶i̶o̶n̶,̶ b̶u̶t̶ d̶o̶i̶n̶g̶ s̶o̶ c̶a̶u̶s̶e̶s̶ t̶h̶e̶ s̶t̶a̶t̶ f̶u̶n̶c̶t̶i̶o̶n̶s̶ t̶o̶ g̶e̶n̶e̶r̶a̶t̶e̶ a̶ r̶a̶n̶d̶o̶m̶ v̶a̶l̶u̶e̶ f̶r̶o̶m̶ t̶h̶e̶ D̶F̶ r̶a̶t̶h̶e̶r̶ t̶h̶a̶n̶ t̶h̶e̶ v̶a̶l̶u̶e̶ m̶a̶t̶c̶h̶i̶n̶g̶ t̶h̶e̶ o̶u̶t̶p̶u̶t̶ o̶f̶ t̶h̶e̶ '̶G̶e̶n̶e̶r̶a̶t̶o̶r̶'̶ f̶u̶n̶c̶t̶i̶o̶n̶.̶
    1a. Resolved! Used global function to store the Random_Pokemon variable and each stat globally, allowing for stat functions to pull the correct value and store it.

2̶.̶ T̶h̶e̶ '̶T̶o̶t̶a̶l̶-̶S̶t̶a̶t̶'̶ f̶u̶n̶c̶t̶i̶o̶n̶ h̶a̶s̶ i̶s̶s̶u̶e̶s̶,̶ i̶t̶ s̶e̶e̶m̶s̶ t̶o̶ b̶e̶ t̶h̶a̶t̶ t̶h̶e̶ v̶a̶l̶u̶e̶ f̶o̶r̶ e̶a̶c̶h̶ s̶t̶a̶t̶ f̶u̶n̶c̶t̶i̶o̶n̶ i̶s̶ n̶o̶t̶ s̶t̶o̶r̶e̶d̶ w̶h̶e̶n̶ t̶h̶e̶ f̶u̶n̶c̶t̶i̶o̶n̶ i̶s̶ r̶u̶n̶,̶ b̶u̶t̶ s̶t̶o̶r̶e̶d̶ w̶h̶e̶n̶ t̶h̶e̶ G̶e̶n̶e̶r̶a̶t̶o̶r̶ f̶u̶n̶c̶t̶i̶o̶n̶ i̶s̶ r̶u̶n̶.̶
    2a. Resolved! This was easily fixed once the global function was used to store the values. The stat values can be summed easily.

3. Mapping these python functions to html buttons to display the results. Most resources have examples for the user inputting data, not sure how to map the function so it displays the stored value.
    3a. HTML has been updated, POST request used to display the current stats for the randomyl selected Pokeomon. Current objective is to place buttons where these stats are currently, allowing user to choose a stat. The result should be the user being returned to the home page, with the selected stat being displayed in the table. The user can generate a new pokemon after this. 

4̶.̶ A̶d̶d̶ a̶ r̶e̶s̶e̶t̶ f̶u̶n̶c̶t̶i̶o̶n̶ t̶o̶ r̶e̶s̶e̶t̶ a̶n̶y̶ s̶t̶o̶r̶e̶d̶ v̶a̶l̶u̶e̶s̶.̶ 
    4a. Resolved! Created function using del to remove all stored variables.

5. Prevent Stat functions from being run if there is already a stored varaible. Can be run again once reset button is used.