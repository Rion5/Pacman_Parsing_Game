# Pacman Parsing Game

## Game Rules  

1. Pac-Man, our hero, moves around the room, munches all of the Dots he meets.  
2. Four ghosts roam the room, trying to catch Pac-Man. If a ghost chomps Pac-Man, a life is lost. When all lives have been lost, the game ends.  
3. In each corner of the room there is a "Power Pellet" that provides Pac-Man with the temporary ability to eat the enemies. Pac-Man can get extra points by eating the ghosts. The first one is worth 200 points and each additional ghost eaten is worth double the number of points (from 200 to 1600 per ghost eaten).  
4. Pac-Man can get extra points as "bonus fruit" appear. The number of points given for each fruit depending on the fruit type.  
5. When the Pac-Man reaches 10000 points, he gets an additional life.  

### Scoring System  

    Vulnerable Ghosts:  
    #1 in succession: 200 points  
    #2 in succession: 400 points  
    #3 in succession: 800 points  
    #4 in succession: 1600 points  

Vulnerable ghost succession doesn’t have to be a continuous sequence, it means that it could be spaced out by other entities. 

Like this:  "VulnerableGhost,Dot,Dot,Dot,....,VulnerableGhost"  

The first VulnerableGhost is worth 200 points and the second one 400 points although there are some Dots between the first and the second occurrence.

    Dot: 10 points
    Cherry: 100 points
    Strawberry: 300 points
    Orange: 500 points
    Apple: 700 points
    Melon: 1000 points
    Galaxian: 2000 points
    Bell: 3000 points
    Key: 5000 points  

### Exercise development

Given a list of the entities that Pac-Man meets during the game in order of appearance.

    Write a console program that reads the file and manages the specific collision with each entity by scoring points and lives.  

Assume that Pac-Man starts the game with:  
5000 points  and  3 lives

1. At the end of the game print out the total points and total lives gained.  

2. Adopt an OOP approach.  

3. Dare to Unit Test.

#### Edit: In my version, I award an additional life for every 10k points gained, not including the starting 5k points.