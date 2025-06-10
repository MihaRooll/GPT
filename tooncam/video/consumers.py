from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaBlackhole
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio
from apps.capture.video import CameraCapture
from apps.stylizer.cartoon import CartoonStylizer
from aiortc import MediaStreamTrack
from av import VideoFrame

class CameraVideoTrack(MediaStreamTrack):
    kind = "video"

    def __init__(self, capture: CameraCapture, stylizer: CartoonStylizer):
        super().__init__()
        self.capture = capture
        self.stylizer = stylizer

    async def recv(self) -> VideoFrame:
        loop = asyncio.get_event_loop()
        frame = await loop.run_in_executor(None, self.capture.read)
        if frame is None:
            await asyncio.sleep(0.01)
            return await self.recv()
        frame = self.stylizer.stylize(frame)
        video_frame = VideoFrame.from_ndarray(frame, format="bgr24")
        video_frame.pts, video_frame.time_base = self.next_timestamp()
        return video_frame

class VideoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.pc = RTCPeerConnection()
        self.media = MediaBlackhole()
        self.capture = CameraCapture()
        self.stylizer = CartoonStylizer()

    async def disconnect(self, close_code):
        await self.pc.close()
        self.capture.release()

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        if data.get("type") == "offer":
            offer = RTCSessionDescription(sdp=data["sdp"], type=data["type"])
            await self.pc.setRemoteDescription(offer)
            self.pc.addTrack(CameraVideoTrack(self.capture, self.stylizer))
            answer = await self.pc.createAnswer()
            await self.pc.setLocalDescription(answer)
            await self.send(json.dumps({
                "sdp": self.pc.localDescription.sdp,
                "type": self.pc.localDescription.type
            }))

