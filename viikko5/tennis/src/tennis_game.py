class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score_when_equal(self):
        if self.m_score1 < 3:
            return self.scores[self.m_score1] + "-All"
        else:
            return "Deuce"
    
    def get_score_when_advantage_or_win(self):
        minus_result = self.m_score1 - self.m_score2
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
    
    def get_score_when_not_equal(self):
        return self.scores[self.m_score1] + "-" + self.scores[self.m_score2]

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.get_score_when_equal()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.get_score_when_advantage_or_win()
        else:
            return self.get_score_when_not_equal()