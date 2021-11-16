from django.shortcuts import render
from django.views.decorators import gzip
from django.conf import settings
from django.http import StreamingHttpResponse
import cv2
import threading
from mtcnn import MTCNN
import numpy as np
import tensorflow as tf
from tensorflow import keras 
import cv2 
from PIL import Image


global result, model
model = tf.keras.models.load_model(settings.MODEL_PATH)
print('Model loaded !!!')

@gzip.gzip_page
def home(request):
    return render(request, 'home/homepage.html')

#to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        self.input_size = (1, 175, 175, 3)
        
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
                cv2.rectangle(image, (x,y), (x+width,y+height), (0,155,255), 2)
                global result 
                result = self.predict(image, (x, y, width, height))
            
            _, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes()
        except Exception as e:
            print(e)

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
    
    def predict(self, image, dimensions):
        x1, y1 = abs(dimensions[0]), abs(dimensions[1])
        x2, y2 = x1 + dimensions[2], y1 + dimensions[3]

        face_array = image[y1:y2, x1:x2]
        face_image = Image.fromarray(face_array)
        face_image = face_image.resize((175, 175))
        face = np.asarray(face_image)

        return np.argmax(model.predict(face.reshape(self.input_size)))



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