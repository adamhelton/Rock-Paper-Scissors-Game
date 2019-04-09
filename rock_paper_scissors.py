from random import randint


class player:
    moves = ['rock', 'paper', 'scissors']

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        return my_move, their_move

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class human(player):
    def move(self):
        warning = """unclear answer please choose
        from 'rock', 'paper', 'scissors' """
        human_move = input("What's your move? ")
        while human_move not in self.moves and human_move != 'quit':
            print(warning)
            human_move = input("What's your move? ")
        if human_move == 'quit':
            self.end_game()
        else:
            return human_move

    def end_game(self):
        quit()


class random(player):
    def move(self):
        return self.moves[randint(0, len(self.moves)-1)]


class reflect(player):
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        return self.their_move


class cycle(player):
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        current_move_index = self.moves.index(self.my_move)
        next_move_index = current_move_index+1
        if next_move_index == 3:
            next_move_index = 0
        return self.moves[next_move_index]


class Game:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        p1_state = self.p1.beats(move1, move2)
        p2_state = self.p1.beats(move2, move1)
        return p1_state, p2_state, move1, move2

    def score_round(self, p1_state, p2_state, p1_score, p2_score):
        if p1_state is True and p2_state is False:
            p1_score = p1_score + 1
            p2_score = p2_score
            print("player 1 wins round\n ")
        elif p1_state is False and p2_state is True:
            p2_score = p2_score + 1
            p1_score = p1_score
            print("player 2 wins round\n ")
        elif p1_state is False and p2_state is False:
            p1_score = p1_score
            p2_score = p2_score
            print(" TIE\n")
        print('score:' '' '' '\n', p1_score, p2_score)
        return(p1_score, p2_score)

    def winner(self, p1_score, p2_score):
        if p1_score > p2_score:
            print("\nFirst Player Wins!")
        elif p2_score > p1_score:
            print("\nSecond Player Wins!")
        else:
            print("\nA TIE ")

    def play_game(self):
        rounds = int(input('\nHow many rounds do you want to play?:'))
        print("\n**********Game start**********\n")
        p1_scr = 0
        p2_scr = 0
        print("Game start!")
        for round in range(rounds):
            if round == 0:
                random_move = self.moves[randint(0, len(self.moves)-1)]
                self.p2.learn(random_move, random_move)
            print(f"Round {round}:")
            p1_stat, p2_stat, move1, move2 = self.play_round()

            p1_scr, p2_scr = self.score_round(p1_stat, p2_stat, p1_scr, p2_scr)
            self.p2.learn(move2, move1)
        self.winner(p1_scr, p2_scr)

        print("\nGame over!")


if __name__ == '__main__':
    players_tuple = {'Multi-Player': human(),
                     'Level 4': random(),
                     'Level 2': reflect(),
                     'Level 3': cycle(),
                     'Level 1': player()}
    game_entry_text = """Difficulty Options:
    level 1: computer plays rock move only
    Level 2: computer imitates your previous move
    Level 3: computer cycles through the moves starting at random
    Level 4: computer chooses random moves
    Multi-Player: control the opponent move"""
    print(game_entry_text)
    opponent_player = input("\nPick your Level:")
    while opponent_player not in players_tuple:
        opponent_player = input("please enter valid mode!!:")
    game = Game(human(), players_tuple[opponent_player])
game.play_game()