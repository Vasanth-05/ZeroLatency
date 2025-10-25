from fastapi import FastAPI, WebSocket
import asyncio
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ZeroLatency Backend is running!"}

@app.websocket("/ws/stream")
async def websocket_stream(websocket: WebSocket):
    await websocket.accept()
    while True:
        original_value = random.randint(50, 100)  # Simulated real-time data
        predicted_value = original_value - random.randint(1, 5)  # Simulated prediction
        delta = original_value - predicted_value  # Compression difference

        data = {
            "original": original_value,
            "predicted": predicted_value,
            "delta": delta
        }
        await websocket.send_json(data)
        await asyncio.sleep(1)  # 1-second interval
