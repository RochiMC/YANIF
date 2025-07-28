from fastapi import FastAPI, WebSocket, Query,WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi import FastAPI, Request
from game.Player import Player
from typing import List, Dict, Optional
import datetime
import uuid
import random
import asyncio
import os
import jwt
from game.GameRoom import GameRoom
from fastapi.responses import HTMLResponse

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware


SECRET_KEY = "YANIFROCIOMARTINCAMPOY"
ALGORITHM = "HS256"


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Solo para desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rooms: Dict[str, GameRoom] = {}
rooms_websockets: Dict[str, list] = {}


async def actualise_number_players(room_id: str):
    """"
    Function that actualises the before start game view"""
    num_players = len(rooms_websockets[room_id])
    for connection in rooms_websockets[room_id]:
        await connection.send_json({
            "type": "player_count",
            "count": num_players
        })

async def common_add_player(room_id: str, username: str):
    # Create the room
    
    rooms[room_id].add_player(username)
    
    payload = {
        "username": username,
        "room_id": room_id,
        "exp": datetime.datetime.now() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    return {
        "room_id": room_id,
        "token": token
    }
    
    
@app.post("/create_room")
async def create_room(request: Request):
    # Crea un ID único para la room
    body = await request.json()
    username = body.get("username")
    room_id = str(uuid.uuid4())[:8]
    
    room = GameRoom(room_id)
    rooms_websockets[room_id] = []
    rooms[room_id] = room
    print(f"EL room id es {room_id}")
    return await common_add_player(room_id, username)

    

@app.post("/join_room")
async def join_room(request: Request):
    data = await request.json()
    username = data.get("username")
    room_id = data.get("roomId")
    
    return await common_add_player(room_id, username)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str = Query(...)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload["username"]
        room_id = payload["room_id"]

        # if the room id is not created, or the username was not previously added
        if room_id not in rooms.keys() or not rooms[room_id].check_player(username):
            return 

        await websocket.accept()
        if room_id not in rooms_websockets:
            rooms_websockets[room_id] = []
        rooms_websockets[room_id].append(websocket)
        
        await actualise_number_players(room_id)
        # Mantener conexión viva
        while True:
            data = await websocket.receive_text()
            print(f"[{username} @ {room_id}] sent: {data}")

    except jwt.ExpiredSignatureError:
        await websocket.close(code=4001)
    except jwt.InvalidTokenError:
        await websocket.close(code=4002)
    except WebSocketDisconnect:
        await actualise_number_players(room_id)
    finally:
        try:
            rooms_websockets[room_id].remove(websocket)
            await actualise_number_players(room_id)
            # SI no queda nadie, quitar el roomID 
            print(f"{username} disconnected from room {room_id}")
        except:
            pass
        
        
app.mount("/static", StaticFiles(directory="/"), name="static")

@app.get("/")
def get_index():
    print(os.getcwd())
    if os.path.exists("templates/login.html"):
        return FileResponse("templates/login.html")
    return {"mensaje": "login.html no encontrado"}

@app.get("/room/{room_id}", response_class=HTMLResponse)
def serve_room_page(room_id: str):
    with open("templates/room.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)