# Seleucos Project 
A realistic script to create JSON database for fantasy football games. 

# The goal
The goal is to create a full and realistic environment for fantasy football games so as to make it easier for future developers to create Football Games without having to worry about copyrights or database management
A passage to Open Source VideoGames era!

# Authors

* **StathisM27** - *Initial work* - [StathisM27](https://github.com/stathism27)

# Technical explanation 
## Abilities :
The abilities are 2 : Current and Potential Ability. Current ability is calculated randomly between [1,100], as well as Potential between [Current,100]

## Age : 
The age is defined randomly.The distribution used is uniform between [17,35]

## Attributes: 
The attributes of each players are divided in 3: Technical,Mental and Physical
For each player, there are some weights(1-6) for each attribute,depend on the player's positions.For instance, a Striker has maximum weight on Finishing and minimum on marking.There are also attributes with no Weights at all(for instance aggression)
For the attributes with no weights the number is calculated completely at random.
For the other attributes things get more complicated.
For major attributes(weight=4,5 or 6) the attributes are calculated using gaussian distribution,with mean value the current ability of player and standard deviation at 20%
For minor attributes(weight=1,2,3) the attributes are usually very low eg marking for strikers or finishing for defender.So,by 99% each attribute is between [1,Current Ability/2] and by 1% is between [Current Ability/2,100]
Then, of course we need to re-evaluate the current and potential ability accordingly
## Body :
First of all height is calculated at gaussian distribution (mean val=1.78m,stand_dev=0.8m)
Then,the weight based on height - gaussian distribution with mean val = mean_weight,stand_dev =10kg - mean weight for every player is his height after decimal minus 5%
Eg for 1.75 players mean weight = 75-3.75=71.25
Then feet, 35% of being left-foot, 40% of being right-foot, 25% of being 2-footed

## Country: 
Completely random between all countries in the world (needs update)

## Names:
The name is a random name from the country of the player. The names categories are far less from countries,because many countries have mainly names from other countries.That's been told, Argentinian and Spanish players share the name pool, as well as Italian and Sammarinese(from San Marino),Greek and Cupriots etc (needs expansion for better results)

## Positions:
Main position is calculated randomly.Then using distribution : [1: 60% ,2: 30% ,3: 7% ,4: 3%] there are extra number of positions accordingly.
Depended on the main position the extra positions are calculated accordingly. Special regard about Goalkeeps,who have no extra positions.

## Auxilary Scripts and Resources : 
For this project there are some useful auxilary scripts and resources so as to build and expand the database.
For the names there have been used the names of current players, which are found in the resources directory as csv files.
Countries.txt contains all the countries names and countries-regions matches each country with the region names that should have.

# About update
## Update Ideas :
- [ ]  Expand and fix the names database - more names,better specifications about countryies and regions
- [ ]  Give each player citizenship based on real world distribution
- [ ]  Update the project and create scripts for creating fantasy teams,stadiums,competitions etc.
