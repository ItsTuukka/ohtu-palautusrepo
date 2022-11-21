class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        by_nationality = []
        for player in self.players:
            if player.nationality == nationality:
                by_nationality.append(player)
    
        return sorted(by_nationality, key=lambda x: x.points, reverse=True)