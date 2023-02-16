from fastapi import FastAPI
from user import User
app = FastAPI()
users = {}

# Initializes initial set of users
for i in range(5):
  u = User()
  users[str(u.id)] = u

# Returns all users
@app.get("/get-user")
def getUser():
  return users

# Gets specific user
@app.get("/get-user/{id}")
def getUserOnId(id):
  return users[id]

# Damages specific user
@app.post("/damage-user/{id}")
def damageUser(id, d):
  users[id].damage(int(d))
  return users[id].health

# Heals specific user
@app.post("/heal-user/{id}")
def healUser(id, h):
  users[id].heal(int(h))
  return users[id].health

# Get player postion
@app.get("/position/{id}")
def userPosition(id):
  return users[id].position

# Get player stamina
@app.get("/stamina/{id}")
def userStamina(id):
  return users[id].stamina

# Add/Subtract stamina
@app.post("/add-stamina/{id}")
def addStamina(id, s):
  users[id].addStamina(int(s))
  return users[id].stamina

# Get player ammo
@app.get("/ammo/{id}")
def userAmmo(id):
  return users[id].ammo

# Add/Subtract ammo
@app.post("/add-ammo/{id}")
def addAmmo(id, s):
  users[id].addAmmo(int(s))
  return users[id].ammo