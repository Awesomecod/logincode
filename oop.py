class Student():
    def __init__(self,name, Class,game,movie):
        self.name = name
        self.Class = Class
        self.game = game
        self.movie = movie
    
    def play_game(self):
        return self.game

    def best_movie(self):
        return self.movie

    def __str__(self):
        return f" {self.name} is a student {self.movie} is intresting.I love playing {self.game}"

Kamshire = Student("Kcoder","Jss3","CODM","Naruto Shippumen VI")
Awesome = Student("Awesome","Basic5","GTAV","Justice Legue")
Great = Student("Greatee","Jss3","blox fruit","One piece")
print(Kamshire)
print(Awesome)
print(Great)
