import ipdb
class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) and not hasattr(self, "title"):
            self._title = title
        else:
          raise Exception()
            
    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        results = self.results()
        return [result.player for result in results]

    def average_score(self, player):
        pass

class Player:

    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) >= 2 and len(username) <= 16:
            self._username = username
        else:
            raise Exception()

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        #Returns a unique list of all games played by a particular player
        #Games must be of type Game
      game_list = []
      for result in self.results():
        if result.game not in game_list:
          game_list.append(result.game)
      return game_list

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

class Result:

    all = []
    
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        if isinstance(score, int) and score >= 1 and score <= 5000 and not hasattr(self, "score"):
            self._score = score
        else:
            raise Exception()
    
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception()
    
    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception()