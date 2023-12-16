
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
          raise Exception("Title must be of type string, more than 1 character, and not set twice")
            
    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        player_list = []
        for result in self.results():
            if result.player not in player_list:
                player_list.append(result.player)
        return player_list

    def average_score(self, player):
        player_scores = []
        for result in Result.all:
            if result.player == player:
                player_scores.append(result.score)
        avg_score = sum(player_scores, 0)
        return avg_score/len(player_scores)

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
            raise Exception("username must be of type str and between 2 and 16 characters")

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
      game_list = []
      for result in self.results():
        if result.game not in game_list:
          game_list.append(result.game)
      return game_list

    def played_game(self, game):
      return game in self.games_played()

    def num_times_played(self, game):
      return len([result.game for result in self.results() if result.game == game])

    @classmethod 
    def highest_scored(cls, game):
      players_of_game = game.players()
      highest_scored = 0
      highest_player = None
      for player in players_of_game:
          if game.average_score(player) >= highest_scored:
              highest_scored = game.average_score(player)
              highest_player = player
      return highest_player
          
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
            raise Exception("Score must be of int type, between 1 and 5000, and not set twice")
    
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception("player must be of Player class")
    
    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception('Game must be of Game class')