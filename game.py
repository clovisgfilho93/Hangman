import os

class Hangman:
    winner = False
    word = ''
    mask = []
    mistakes = []

    def __init__(self, word):
        self.word = word
        self.mask = ['_'] * len(word)

    def make_move(self, letter):
        letter_match = self.word.find(letter)
        if letter_match >= 0:
            for i, w in enumerate(self.word):
                if w == letter:
                    self.mask[i] = letter
            self.check_winner()
        else:
            self.mistakes.append(letter)
            print(f"Already tried: {', '.join(self.mistakes)}")


    def check_winner(self):
        if '_' not in self.mask:
            self.show_board()
            print('You won!')
            return True

        return False

    def check_loser(self):
        if len(self.mistakes) > 4:
            print('You lose! The word was %s' % self.word)
            quit()

    def show_board(self):
        os.system('clear')
        print(self.mask)
        print(self.mistakes)

    def play(self):
        won = False
        while not won:
            self.show_board()

            letter_input = input('Choose a letter: ').upper()
            self.make_move(letter_input)

            won = self.check_winner()
            self.check_loser()