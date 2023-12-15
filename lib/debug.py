#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

game_1 = Game("Skribbl.io")
game_2 = Game("Scattegories")
player_1 = Player("Saaammmm")
player_2 = Player("ActuallyTopher")
Result(player_1, game_1, 2000)
Result(player_1, game_2, 3500)
Result(player_2, game_1, 190)

assert player_1.played_game(game_1) == True
assert player_1.played_game(game_2) == True
assert player_2.played_game(game_1) == True
assert player_2.played_game(game_2) == False
    #ipdb.set_trace()
