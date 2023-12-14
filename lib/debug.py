#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    game = Game("Skribbl.io")
    game_2 = Game("Scattegories")
    player = Player("Saaammmm")
    result_1 = Result(player, game, 2000)
    result_2 = Result(player, game, 3500)
    result_3 = Result(player, game_2, 19)

    print(len(game.results()))
    #ipdb.set_trace()
