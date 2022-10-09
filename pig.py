import argparse
import random
import sys


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

    def play_turn(self):
        """
        Play one turn
        """
       
        print(f"Current player {self.name}")
        print()
        print()
        turn_total = 0
        roll_hold = 'r'
        while roll_hold == "r":
            die = throw_the_die()
            if die == 1:
                print(f"{self.name} Scratched!")
                self.show
                break

            

            turn_total += die
            # Print some information to the user. My recommendation is to:
            # print turn_total,
            # print possible total if I hold, total + turn_total
            # print real total
            print(f"Roll: {die}")
            print()
            print()
            print(f"Points this turn: {turn_total}")
            print()
            print(f"Score on hold: {self.total + turn_total}")
            print()
            print(f"Current Score: {self.total}")
            print()
            
            roll_hold = input("Roll(r) or Hold(h)? ").lower()
            print()
            print()


        if roll_hold == 'h':
            # update the player's total
            self.total += turn_total
            

        if roll_hold == "x":
            exit()

        self.show()


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None

    def check_winner(self):

        for player in self.players:
            if player.total >= 100:
                self.winner = player
                return True

        return False


    def play_game(self):
        current_player = self.players[0] 

        while not self.check_winner():
            # play the game
            for player in self.players:
                current_player = player
                current_player.play_turn()
                if player.total >= 100:
                    break
                
        print()
        print()
        print(f"{self.winner.name} is victorious!")

                
            
    
       

if __name__ == '__main__':
    p1 = Player("John")
    p2 = Player("Jane")
    pig_game = Game(p1, p2)
    pig_game.play_game()

    
