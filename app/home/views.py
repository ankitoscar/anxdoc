from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from mtcnn import MTCNN

@gzip.gzip_page
def home(request):
    return render(request, 'home/homepage.html')

#to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        try:
            image = self.frame
            detector = MTCNN()
            detections = detector.detect_faces(image)

            for detection in detections:
                x, y, width, height = detection['box']
                keypoints = detection['keypoints']
                cv2.rectangle(image, (x,y), (x+width,y+height), (0,155,255), 2)
                cv2.circle(image, (keypoints['left_eye']), 2, (0,155,255), 2)
                cv2.circle(image, (keypoints['right_eye']), 2, (0,155,255), 2)
                cv2.circle(image, (keypoints['nose']), 2, (0,155,255), 2)
                cv2.circle(image, (keypoints['mouth_left']), 2, (0,155,255), 2)
                cv2.circle(image, (keypoints['mouth_right']), 2, (0,155,255), 2)
            
            _, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes()
        except Exception as e:
            print(e)

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass