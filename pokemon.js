// Assuming you have loaded 'Pokedex_Ver_SV2.csv' into a variable named 'poke_data' in the same format as the pandas DataFrame

// Generator Function
function Generator() {
    // Selecting random Pokemon from the Pokedex
    let Random_Pokemon = poke_data['Name'][Math.floor(Math.random() * poke_data['Name'].length)];

    // Return the random Pokemon
    return Random_Pokemon;
}

function HP() {
    // Display the HP of the Pokemon selected from the generator function
    let HP_Stat = poke_data['HP'].findIndex(row => row['Name'] === Random_Pokemon);
    
    // Return the HP stat
    return HP_Stat;
}

function Attack() {
    // Display the attack of the Pokemon selected from the generator function
    let Attack_Stat = poke_data['Attack'].findIndex(row => row['Name'] === Random_Pokemon);
    
    // Return the attack stat
    return Attack_Stat;
}

function Defense() {
    // Display the defense of the Pokemon selected from the generator function
    let Defense_Stat = poke_data['Defense'].findIndex(row => row['Name'] === Random_Pokemon);
    
    // Return the defense stat
    return Defense_Stat;
}

function SP_Attack() {
    // Display the special attack of the Pokemon selected from the generator function
    let SP_Attack_Stat = poke_data['SP_Attack'].findIndex(row => row['Name'] === Random_Pokemon);
    
    // Return the special attack stat
    return SP_Attack_Stat;
}

function SP_Defense() {
    // Display the special defense of the Pokemon selected from the generator function
    let SP_Defense_Stat = poke_data['SP_Defense'].findIndex(row => row['Name'] === Random_Pokemon);
    
    // Return the special defense stat
    return SP_Defense_Stat;
}

function Speed() {
    // Display the speed of the Pokemon selected from the generator function
    let Speed_Stat = poke_data['Speed'].findIndex(row => row['Name'] === Random_Pokemon);
    
    // Return the speed stat
    return Speed_Stat;
}

function Total() {
    // Display the sum of the chosen stats from the stat function
    let HP_Stat = HP();
    let Attack_Stat = Attack();
    let Defense_Stat = Defense();
    let SP_Attack_Stat = SP_Attack();
    let SP_Defense_Stat = SP_Defense();
    let Speed_Stat = Speed();
    let Total_Stat = poke_data['HP'][HP_Stat] + poke_data['Attack'][Attack_Stat] + poke_data['Defense'][Defense_Stat] + poke_data['SP_Attack'][SP_Attack_Stat] + poke_data['SP_Defense'][SP_Defense_Stat] + poke_data['Speed'][Speed_Stat];
    
    // Return the total stat
    return Total_Stat;
}

function Reset() {
    // Reset all stored variables
    Random_Pokemon = null;
    Attack_Stat = null;
    Defense_Stat = null;
    HP_Stat = null;
    SP_Attack_Stat = null;
    SP_Defense_Stat = null;
    Speed_Stat = null;
    Total_Stat = null;
}
