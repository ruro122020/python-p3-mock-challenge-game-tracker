#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

game_1 = Game("Skribbl.io")
game_2 = Game("Codenames")
player = Player("Nick")
Result(player, game_1, 5000)
Result(player, game_2, 19)
Result(player, game_1, 100)
    
print(len(set(player.games_played())) == len(player.games_played()))
print(len(player.games_played()))

    #ipdb.set_trace()
