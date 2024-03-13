import random
import requests
import json

def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }

def run():
    player_wins = 0
    opponent_wins = 0
    rounds = 0
    while True:
        rounds += 1
        my_pokemon = random_pokemon()
        opponent_pokemon = random_pokemon()
        print('Round {}'.format(rounds))
        print('You were given {}'.format(my_pokemon['name']))

        stat_choice = input('Which stat do you want to use? (id, height, weight) : ')
        my_stat = my_pokemon[stat_choice]
        opponent_stat = opponent_pokemon[stat_choice]

        if my_stat > opponent_stat:
            print('The opponent chose {}'.format(opponent_pokemon['name']))
            print('You Win!')
            player_wins += 1
        elif my_stat < opponent_stat:
            print('The opponent chose {}'.format(opponent_pokemon['name']))
            print('You Lose!')
            opponent_wins += 1
        else:
            print('The opponent chose {}'.format(opponent_pokemon['name']))
            print('Draw!')

        play_again = input('Do you want to play again? (yes/no): ')
        if play_again.lower() != 'yes':
            break

    print('Final Score:')
    print('Player Wins: {}'.format(player_wins))
    print('Opponent Wins: {}'.format(opponent_wins))
    print('Total Rounds: {}'.format(rounds))


    with open('high_scores.json', 'r+') as f:
        high_scores = json.load(f)
        player_name = input('Enter your name: ')
        high_scores.append({'name': player_name, 'score': player_wins})
        f.seek(0)  
        json.dump(high_scores, f, indent=4)

run()
