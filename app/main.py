from fastapi import FastAPI, WebSocket
import asyncio
import time
from prometheus_client import Counter, Gauge, start_http_server

# Create FastAPI app instance
app = FastAPI(title="ZeroLatency Backend", version="1.0")

# Metrics for Prometheus/Grafana
frame_counter = Counter("frames_processed_total", "Total frames processed")
latency_gauge = Gauge("frame_latency_ms", "Average frame latency in milliseconds")

@app.get("/")
async def root():
    return {"status": "ZeroLatency backend running"}

@app.websocket("/stream")
async def stream(websocket: WebSocket):
    await websocket.accept()
    print("📡 Client connected to /stream")
    try:
        while True:
            start_time = time.time()
            data = await websocket.receive_bytes()
            await asyncio.sleep(0.02)  # Simulated 20 ms processing delay
            latency = (time.time() - start_time) * 1000
            latency_gauge.set(latency)
            frame_counter.inc()
            await websocket.send_bytes(data)
    except Exception as e:
        print("❌ Stream closed:", e)
    finally:
        await websocket.close()
        print("🔌 Connection closed")

# Start Prometheus metrics server
start_http_server(8001)
