db = "Database link"
class Video(db.Model):
    __tablename__ = "videos"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    people = db.Column(db.String(200), nullable = False)