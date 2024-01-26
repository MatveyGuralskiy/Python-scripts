    #JSON(JavaScript Object Notation)
import json
FILE='./JSON.txt'
OPENFILE=open(FILE,mode='w',encoding='latin_1')
PLAYER1={
    'username':'alex',
    'score':'3000',
    'rank':'gold-nova',
    'awards':['gold-medal','silver-medal','diamond-medal']
}

PLAYER2={
    'username':'leo',
    'score':'4500',
    'rank':'gold-nova-3',
    'awards':['gold-medal','silver-medal','diamond-medal','emirald-medal']
}
PLAYERS=[]
PLAYERS.append(PLAYER1)
PLAYERS.append(PLAYER2)


#-------SAVE BY JSON-----------
json.dump(PLAYERS,OPENFILE)
print("="*30)
OPENFILE.close()

#-------LOAD BY JSON-----------
OPENFILE=open(FILE,mode='r',encoding='latin_1')
JSON_DATA=json.load(OPENFILE)
for user in JSON_DATA:
    print("Username: "+str(user['username']))
    print("Score: "+str(user['score']))
    print("Rank: "+str(user['rank']))
    print("Third award: "+str(user['awards'][2]))