import game
import getpass

if __name__ == '__main__':
    secret_input = getpass.getpass('Secret Word: ').upper()

    game = game.Hangman(secret_input)
    game.play()