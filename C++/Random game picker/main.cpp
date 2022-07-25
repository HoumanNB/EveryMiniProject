// include libraries
#include <iostream> // the basic input/output system
#include <cstdlib> //  generating random numbers
#include <time.h> // for date and time

using namespace std;

// main function
int main()
{   
    // the list containing the items to be selected from
    string games[] = { 
    "short hike", "alba", "banished", "big pharma", "call of juarez", "change", "chef", "cities skylines", 
    "citizen sleeper", "Coffe talk", "cuphead", "death trash", "do not feed the monkeys", "factorio", 
    "fallout new vegas", "Graveyard keeper", "gris", "hacknet", "hades", "house flipper", "inmost", "KSP", 
    "kona", "martial law", "mind scanners", "minecraft", "oxygen not included", "papers please", 
    "pc building simulator", "police stories", "portal 2", "portal", "shenzhen io", "civ 6", "spirit farer", 
    "spore", "starbound", "stardew", "noita", "punch club", "serial cleander", "startup company", "surviving mars",
    "tastemaker","binding of isaac", "darksied detective", "tennants", "witcher 2", "there is no game",
    "theif simulator", "twelve minutes", "unpacking", "while true", "worksop simulator"};
     
    // gets the size of the array (by deviding the total byte size by the size of one item)
    // this variable is later used to determine the maximum value of the randomizer range
    int index = sizeof(games) / sizeof(games[0]);
    
    // using the current time as seed for the randomizer
    srand(time(0));

    // prints the header of the message(if in for-loop, it would have been printed many times)
    cout << "Your games for this week are:" << endl;

    // printing the chosen game based on randomly generated index
    for(int i = 0; i < 3; i++) { 
        // generates a random number from 0 to the last item index
        int selection = rand() % index;

        // prints the name
        cout << games[selection] << endl;

        return 0;
    } 
}
