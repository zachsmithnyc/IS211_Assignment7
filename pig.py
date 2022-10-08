import argparse
import random


def throw_the_die(sides=6):
    """
    dice roll
    """
    return random.randint(1, sides)


class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0

    def show(self):
        print(f"{self}")

    def __str__(self):
        """String representation"""
        return f"{self.name}'s Total = {self.total}"

    def turn(self):
        """
        Play one turn
        """
        turn_total = 0
        roll_hold = 'r'
        while roll_hold != "h":
            die = throw_the_die()
            if die == 1:
                # scratch - let the user know!
                break

            turn_total += die
            # Print some information to the user. My recommendation is to:
            # print turn_total,
            # print possible total if I hold, total + turn_total
            # print real total
            roll_hold = input("Roll(r) or Hold(h)? ").lower()

        if roll_hold == 'h':
            # update the player's total
            self.total += turn_total

        self.show()


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None

    def check_winner(self):
        """
        Returns true if there is winner
        :return:
        """
        for player in self.players:
            if player.total >= 100:
                self.winner = player
                return True

        return False

    def play_game(self):
        current_player = self.players[0]
        while not self.check_winner():
            # play the game
            current_player.turn()
            # change current_player to the next player

        # show the winner


if __name__ == '__main__':
    p1 = Player("John")
    p2 = Player("Jane")
    pig_game = Game(p1, p2)
    pig_game.play_game()

    
