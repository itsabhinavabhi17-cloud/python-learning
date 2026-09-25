class player:
    def __init__(self):
        self.health=100

    def damage(self,damage_taken):
        self.health -=damage_taken





player=player()
player.damage(18)