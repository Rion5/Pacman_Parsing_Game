# Pacman game - Parse through each word and keep track of score and lives
pacman_txt = 'Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,InvincibleGhost,Melon,Galaxian,VulnerableGhost,VulnerableGhost,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Bell,Cherry,Strawberry,InvincibleGhost,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Orange,Apple,InvincibleGhost,VulnerableGhost,Key,InvincibleGhost,Dot,Dot,Dot,Dot,Dot,VulnerableGhost'
separated_txt = pacman_txt.split(',')

# Start of Game
STARTING_SCORE = 5000
score = 0
STARTING_LIVES = 3
extra_lives = 0
extra_lives_counter = 0
vulnerable_ghost_counter = 1
ghost_point_value = 200
pacman_dict = {
    'Dot'       : 10,
    'Cherry'    : 100,
    'Strawberry': 300,
    'Orange'    : 500,
    'Apple'     : 700,
    'Melon'     : 1000,
    'Galaxian'  : 2000,
    'Bell'      : 3000,
    'Key'       : 5000,
    'InvincibleGhost': 0,
    'VulnerableGhost': 0
}

def pacman_eats_food(score):
    global STARTING_LIVES
    global extra_lives_counter
    # If the score // 10000 >= 1 then add an extra live for 1x the output
    if ((score - (10000 * extra_lives_counter)) // 10000 >= 1):
        number_of_extra_lives = (score - (10000 * extra_lives_counter)) // 10000
        STARTING_LIVES += number_of_extra_lives
        extra_lives_counter += number_of_extra_lives
        print(f'{score} - Gaining {number_of_extra_lives} Extra Lives\n\t{STARTING_LIVES} lives')
    else:
        print(score)

def pacman_eats_vulnerable_ghost():
    global ghost_point_value
    global vulnerable_ghost_counter
    if vulnerable_ghost_counter == 1:
        vulnerable_ghost_counter += 1
        return 200
    else:
        updated_score = ghost_point_value * 2
        ghost_point_value = updated_score
        vulnerable_ghost_counter += 1
        return updated_score

# Run Game
print('Pacman-Man Game')
print(separated_txt)
print(f'\nStarting\nScore: {STARTING_SCORE}\n# of lives: {STARTING_LIVES}\n')
for word in separated_txt:
    if pacman_dict[word]:
        score += pacman_dict[word]
        pacman_eats_food(score + STARTING_SCORE)
    if word == 'InvincibleGhost':
        STARTING_LIVES -= 1
        print(f'{score + STARTING_SCORE} - Ouch! Attacked by Ghost:\n\t{STARTING_LIVES} lives left')
    if word == 'VulnerableGhost':
        score += pacman_eats_vulnerable_ghost()
        pacman_eats_food(score + STARTING_SCORE)
        print(f'*Ate Ghost* {score + STARTING_SCORE}')
    if STARTING_LIVES == 0:
        print(word)
        print('Out of Lives')
        exit()

print(f'\nEnding\nScore: {STARTING_SCORE + score}\n# of lives: {STARTING_LIVES + extra_lives}')

#TODO: Refactor with OOP