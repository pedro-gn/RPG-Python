from model.character import Character
from model.monster import Monster
from model.user import User
from persistence.database import Database
import random

# def battle (character:Character, monster:Monster):
#     damage = 1
#     while 1:
        
#         damage = random.randint(1,5)
#         monster.health -= damage
#         print(f"CH :{character.health} MH {monster.health}")
#         if monster.health <= 0 :
#             character.level += 1
#             print(f"Personagem ganhou 1 nivel agora esta nivel : {character.level}")
#             break
        
#         damage = random.randint(1,5)
#         character.health -= damage
        
#         if character.health <= 0:
#             print("character died")
#             break


class Controler():
    def __init__(self, db : Database):
        self.db = db
        pass
    
    def userLogin(self, username, password):
        userL  =  self.db.searchUser( User(username, password) )
        return userL

    def userRegister(self, username, password):
        userL  =  self.db.insertUser(User(username, password))
        return userL

    def getAllowedClasses(self):
        return self.db.classes

    def createUserCharacter(self, name , _class, user : User):
        char  = self.db.insertCharacter( Character(name, _class, user), user )
        return char

    def getUserCharacters(self, user : User):
        chars = self.db.getUserCharacters(user)
        charsObj = [Character( char[0], char[1], user) for char in chars ]
        return charsObj
