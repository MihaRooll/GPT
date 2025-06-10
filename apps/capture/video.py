import cv2

class CameraCapture:
    """Simple wrapper around cv2.VideoCapture"""

    def __init__(self, device: int = 0):
        self.cap = cv2.VideoCapture(device)

    def read(self):
        if not self.cap.isOpened():
            return None
        ret, frame = self.cap.read()
        return frame if ret else None

    def release(self):
        if self.cap.isOpened():
            self.cap.release()
