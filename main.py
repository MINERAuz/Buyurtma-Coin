
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_db = {}

@app.post("/register")
async def register(user_id: str):
    if user_id not in fake_db:
        fake_db[user_id] = {"balance": 0}
    return {"status": "ok", "balance": fake_db[user_id]["balance"]}

@app.post("/mine")
async def mine(user_id: str):
    if user_id in fake_db:
        fake_db[user_id]["balance"] += 1
        return {"status": "ok", "balance": fake_db[user_id]["balance"]}
    return {"status": "error", "message": "User not found"}

@app.get("/balance")
async def balance(user_id: str):
    if user_id in fake_db:
        return {"balance": fake_db[user_id]["balance"]}
    return {"status": "error", "message": "User not found"}
