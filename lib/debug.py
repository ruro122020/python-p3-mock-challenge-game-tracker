#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

game = Game("Skribbl.io")

player = Player("Nick")
player_2 = Player("Ari")
Result(player, game, 4000)
Result(player, game, 5000)
Result(player_2, game, 4999)
print(game.players())
len(set(game.players())) == len(game.players())
len(game.players()) == 2

    #ipdb.set_trace()
