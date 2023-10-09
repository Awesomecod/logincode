from os import name
from re import sub
from flask import Flask


db = "Database link"
class Video(db.Model):
    __tablename__ = "videos"
    id = db.Column(db.Integer, primary_key = True)
name = db.Column(db.string(200),nulable = False)
likes = db.column(db.Model):
     __tablename__ = "likes"
     likes = db.Column(db.Integer, primary_key = True)
sub = db.column(db.Model):
     __tablename__ = "sub"
     sub = db.Column(db.Integer, primary_key = True)