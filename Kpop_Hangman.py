# Personal project #2
import random

Kpop_words = ['Superhuman', 'Pinball', 'In Bloom', 'Guerilla', 'All My Poetry', 'Fairy Of Shampoo', 'Chroma Drift', 'GPT', 'Sticker', 'Selfish Waltz', 'Elevator', 'UN Village', 'Just One Day', 'Hype Boy', 'Cosmic', 'Attention', 'After Like', 'Drama', 'Bad Boy', 'Stereotype', 'Miniskirt', 'Love Me Back', 'ETA', 'Supernatural', 'DM', 'Scientist', 'Ill See You There Tomorrow', 'Dreamer', 'Garden In the Air', 'Panorama', 'We Go', 'Stay This Way', 'On My Youth', 'Doughnut', 'Pinball', 'Swicy', 'Stunner', 'Yogurt Shake', 'Baggy Jeans', 'Phantom', 'Sad Song', 'Back Down', 'Perfume', 'Kiss', 'Smoothie', 'Strawberry Sunday', 'Sherlock', 'Steady', 'House Of Cards', 'Y Si Fuera Ella', 'Tell Me', 'Doctor Doctor', 'Sugar Rush Ride', 'Lucky', 'Snowy Summer', 'Movie Star', 'Insomnia', 'Ice Queen', 'Permission To Dance', 'Dynamite', 'Poppop', 'Only One Story', 'Deja Vu', 'Good So Bad', 'Get A Guitar', 'ISTJ', 'God Of Music', 'Mansae', 'Russian Roulette', 'Cant Get You', 'Wish', 'Silly Dance', 'Flight To Paris', 'Love Language', 'Maybe Tomorrow', 'Chewing Gum', 'Underwater', 'Poison', 'Duh']
secret_word = random.choice(Kpop_words)
secret_word_lower = secret_word.lower()

display = ["_" if letter != " " else " " for letter in secret_word]

lives = 7

print(f"Word to guess: {' '.join(display)}")

while "_" in display and lives > 0:
    print(f'\nYou currently have {lives} lives.')
    print("Current word: " + " ".join(display))
          
    guess = input('Guess a letter:  ').lower()

    if guess in secret_word_lower:
        for q in range(len(secret_word_lower)):
            if secret_word_lower[q] == guess:
                display [q] = secret_word[q]
    else:
        lives -= 1
        print(f'You lost a life. Choose your letters carefully!😢')

if lives > 0:
    print(f'\n😎😎 YOUUUUU WONNN! The word was: {secret_word}!')
else:
    print(f'\n😢😢 Game Overrr!!!! The word was: {secret_word}!! Better luck next time')