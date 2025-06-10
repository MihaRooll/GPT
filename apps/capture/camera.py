import cv2


class Camera:
    """Simple camera wrapper using OpenCV."""

    def __init__(self, index: int = 0) -> None:
        self.cap = cv2.VideoCapture(index)

    def read(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self) -> None:
        self.cap.release()
