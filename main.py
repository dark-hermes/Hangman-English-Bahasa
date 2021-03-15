import json
import random
import ascii_art
import sound
import os

print(ascii_art.logo)

# initiate is_replay to True for infinty loop
is_replay = True

# will do infinity loop while is_replay = True
while is_replay:
    # demand user input for language and level diff
    lang = input("\nChoose Language:\n\t1. English\n\t2. Bahasa Indonesia\n> ")
    level = input("\nChoose Level (1-3)\n> ")

    game_is_finished = False
    lives = len(ascii_art.hangman_pics)-1

    # create condition if user choose english
    if lang == "1":

        # open english json depend on it's level
        with open(f'dictionaries/english_level{level}.json','r') as read_json:
            data = json.load(read_json)

        # genereate random word to play in game
        random_word = random.choice(list(data))

        # transform word into underscore char
        hidden_word = [" " if letter==" " else "_" for letter in random_word ]

        # set language to english
        sound.set_language(lang)

        # hint to user
        word_explain = data[random_word]

        # some sentences in game
        request = "Guess a letter"
        if_double = "You've already guessed"
        if_false = "False"
        if_lose = "You lose"
        true_answer = f"The answer is {random_word}"
        if_win = "You win!"
        if_finish = "Do you want to play again?"
        
    # condition if user choose bahasa
    elif lang =="2":
        # read bahasa indonesia json depend on it's level
        with open(f'dictionaries/indonesia_level{level}.json', 'r') as read_json:
            data = json.load(read_json)
        
        # generate random word from indonesia json
        random_word = random.choice(list(data))

        # hidden the word
        hidden_word = [" " if letter==" " else "_" for letter in random_word]
        # set language into bahasa
        sound.set_language(lang)
        #hint
        word_explain = data[random_word]

        # some sentences in game
        request = "Tebak sebuah huruf"
        if_double = "Anda telah menebak huruf"
        if_false = "Salah"
        if_lose = "Anda kalah"
        true_answer = f"Jawaban yang benar adalah {random_word}"
        if_win = "Selamat, anda menang!"
        if_finish = "Ingin bermain lagi?"

    # conditon if user is playing or just begin the game
    is_play = False

    # loop until live numbers reach zero
    while not game_is_finished:

        print(ascii_art.hangman_pics[len(ascii_art.hangman_pics)-1-lives])
        print(data[random_word])

        # play hint sound if user just begin the game 
        if not is_play:
            sound.sayit(data[random_word])
            is_play = True

        print(' '.join(hidden_word))

        # ask user input
        guess = input(f"\n{request}:\n> ")

        # clear output in terminal
        os.system("cls")

        # condition if user input a true letter twice
        if guess in hidden_word:
            print(f"{if_double} {guess}")

        # change hidden word if user guessed right
        for position in range(len(random_word)):
            if guess == random_word[position]:
                hidden_word[position] = random_word[position]
        
        # condition if user input is false
        if guess not in hidden_word:
            print(if_false)
            lives -= 1
            sound.sayit(if_false)

            # if live numbers reach zero (lose)
            if lives == 0:
                game_is_finished = True
                print(if_lose)
                sound.sayit(if_lose)
                print(true_answer)
                sound.sayit(true_answer)

        # if hidden word is completely guessed (win)
        if not "_" in hidden_word:
            game_is_finished = True
            print(if_win)
            sound.sayit(if_win)
            print(true_answer)
            sound.sayit(true_answer)

    sound.sayit(if_finish)

    # ask for replay
    is_replay = input(f"\n{if_finish} (yes/no)\n> ")
    
    is_replay = (True if is_replay=="yes" else False)
