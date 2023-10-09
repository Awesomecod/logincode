class game():
    def __init__(self,game,gun,sword):
        self.game = game
        self.gun = gun
        self.sword = sword
    
    def play_game(self):
        return self.game

    def best_gun(self):
        return self.gun
    def best_sword(self):
        return self.sword

    def change_game(self,new_game):
        self.game = new_game
    def change_gun(self,new_gun):
        self.gun = new_gun
    def change_sword(self,new_sword):
        self.sword = new_sword

    def __str__(self):
        return f"I love playing {self.game} My best gun in {self.game} is {self.gun} My best sword {self.game} is {self.sword}."

Awesome = game("GTAV","Sniper","cutlass")
Awesome.change_game("CODM")
Awesome.change_gun("Ak47")
Awesome.change_sword("Knife")
print(Awesome)
