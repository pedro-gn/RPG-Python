from model.user import User
import random

class Character:
    
    def __init__(self, name, _class, user : User):
        self.name = name
        self._class = _class
        self.user = user
        self.level = 0
        self.health = 10
    
    def __str__(self):
        return f"Name: {self.name}, Class: {self._class}, User: {self.user}, Level: {self.level}, Health: {self.health}"
        