import random


kleuren_lijst = ['rood', 'oranje', 'geel', 'groen', 'blauw', 'paars']
def gok():
    k1 = input('Geef je 1e kleur: ')
    k2 = input('Geef je 2e kleur: ')
    k3 = input('Geef je 3e kleur: ')
    k4 = input('Geef je 4e kleur: ')
    guess = [k1.lower(), k2.lower(), k3.lower(), k4.lower()]
    print(guess)
    return guess

def generate_secret_key():
    secret_key = []
    for kleur in range(4):
        kleur = random.choice(kleuren_lijst)
        secret_key.append(kleur)
    print('antwoord:', secret_key)
    return secret_key

def mastermind_pc_code():
    secret_key = generate_secret_key()
    guess = gok()
    if guess == secret_key:
        print('Gefeliciteerd je bent een mastermind!')
    else:
        aantal_guesses = 0
        while guess != secret_key:
            pins = []
            pogingen += 1
            for i in range(0, 4):
                if (guess[i] == secret_key[i]):
                    pins.append('wit')
                    print('Gefeliciteerd je bent een mastermind!')
                elif (guess[i] in secret_key):
                    pins.append('zwart')
            print(pins)
            print('Je hebt {} van de 10 pogingen gebruikt'.format(pogingen))
            if pogingen < 10:
                guess = gok()
            else:
                print('game over')
                break
mastermind_pc_code()
