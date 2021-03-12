import json
import random
import ascii_art
import sound
import os

print(ascii_art.logo)

is_replay = True

while is_replay:
    lang = input("\nChoose Language:\n\t1. English\n\t2. Bahasa Indonesia\n> ")
    level = input("\nChoose Level (1-3)\n> ")

    game_is_finished = False
    lives = len(ascii_art.hangman_pics)-1

    if lang == "1":
        with open(f'dictionaries/english_level{level}.json','r') as read_json:
            data = json.load(read_json)
        random_word = random.choice(list(data))

        hidden_word = [" " if letter==" " else "_" for letter in random_word ]
        sound.set_language(lang)

        word_explain = data[random_word]

        request = "Guess a letter"
        if_double = "You've already guessed"
        if_false = "False"
        if_lose = "You lose"
        true_answer = f"The answer is {random_word}"
        if_win = "You win!"
        if_finish = "Do you want to play again?"
        
    elif lang =="2":
        with open(f'dictionaries/indonesia_level{level}.json', 'r') as read_json:
            data = json.load(read_json)
        random_word = random.choice(list(data))

        hidden_word = [" " if letter==" " else "_" for letter in random_word]
        sound.set_language(lang)

        word_explain = data[random_word]

        request = "Tebak sebuah huruf"
        if_double = "Anda telah menebak huruf"
        if_false = "Salah"
        if_lose = "Anda kalah"
        true_answer = f"Jawaban yang benar adalah {random_word}"
        if_win = "Selamat, anda menang!"
        if_finish = "Ingin bermain lagi?"

    is_play = False

    while not game_is_finished:

        print(ascii_art.hangman_pics[len(ascii_art.hangman_pics)-1-lives])
        print(data[random_word])

        if not is_play:
            sound.sayit(data[random_word])
            is_play = True

        print(' '.join(hidden_word))
        guess = input(f"\n{request}:\n> ")

        os.system("cls")
        if guess in hidden_word:
            print(f"{if_double} {guess}")

        for position in range(len(random_word)):
            if guess == random_word[position]:
                hidden_word[position] = random_word[position]
        
        if guess not in hidden_word:
            print(if_false)
            lives -= 1
            sound.sayit(if_false)
            if lives == 0:
                game_is_finished = True
                print(if_lose)
                sound.sayit(if_lose)
                print(true_answer)
                sound.sayit(true_answer)
        
        if not "_" in hidden_word:
            game_is_finished = True
            print(if_win)
            sound.sayit(if_win)
            print(true_answer)
            sound.sayit(true_answer)

    sound.sayit(if_finish)
    is_replay = input(f"\n{if_finish} (yes/no)\n> ")
    
    is_replay = (True if is_replay=="yes" else False)
