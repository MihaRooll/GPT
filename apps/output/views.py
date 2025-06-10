from django.http import StreamingHttpResponse

from apps.capture import Camera
from apps.stylizer import apply_style

import cv2

camera = Camera()

def frame_generator():
    """Yield JPEG frames wrapped for MJPEG streaming."""
    while True:
        frame = camera.read()
        if frame is None:
            break
        frame = apply_style(frame)
        ret, jpeg = cv2.imencode(".jpg", frame)
        if not ret:
            continue
        yield (
            b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n"
        )


def video_feed(request):
    return StreamingHttpResponse(
        frame_generator(),
        content_type="multipart/x-mixed-replace; boundary=frame",
    )
