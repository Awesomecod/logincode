class game():
    def __init__(self,game,gun,sword):
        self.game = game
        self.gun = gun
        self.sword = sword
    def change_gun(self,new_gun):
        self.gun = new_gun
    def play_game(self):
        return self.best_gun

    def best_gun(self):
        return self.best_gun
    def best_sword(self):
        return self.best_sword

    def __str__(self):
        return f"I love playing {self.game} My best gun in GTAV is {self.gun} My best sword GTAV is {self.sword}."

Awesome = game("GTAV","Sniper","cutlass ")
Awesome.change_gun("Ak47")
print(Awesome)
