import asyncio
import websockets

async def test_stream():
    uri = "ws://localhost:8000/stream"
    async with websockets.connect(uri) as ws:
        for i in range(5):
            await ws.send(b"dummyframe")
            msg = await ws.recv()
            print("Echo:", msg)
    print("✅ Stream test complete")

asyncio.run(test_stream())
