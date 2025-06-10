import cv2


def apply_style(frame):
    """Apply a simple cartoon-like effect using OpenCV."""
    return cv2.stylization(frame, sigma_s=60, sigma_r=0.6)
