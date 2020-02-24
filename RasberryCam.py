import threading
import cv2
global timer
import sys
import os, datetime

"""
For Rasberry Pi Camera
This ounction is for capturing image and keep the storage inmage in a recent period of time.
"""


def gstreamer_pipeline (capture_width=3280, capture_height=2464, display_width=820, display_height=616, framerate=21, flip_method=0) :   
    return ('nvarguscamerasrc ! '
            'video/x-raw(memory:NVMM), '
            'width=(int)%d, height=(int)%d, '
            'format=(string)NV12, framerate=(fraction)%d/1 ! '
            'nvvidconv flip-method=%d ! '
            'video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! '
            'videoconvert ! '
            'video/x-raw, format=(string)BGR ! appsink' %(capture_width,capture_height,framerate,flip_method,display_width,display_height)) 

def delete_pic(path, days = 0,hours = 0, minutes = 0, seconds = 0):
    path_list=os.listdir(path)
    path_list.sort() 
    
    now = datetime.datetime.now()
    
    days = datetime.timedelta(days = days)
    hours = datetime.timedelta(hours = hours)
    minutes = datetime.timedelta(minutes = minutes)
    seconds = datetime.timedelta(seconds = seconds)
 
    delta_time_sum = hours + minutes + seconds
    
    if path_list != []:
        for img in path_list:
            obj_path = os.path.join(path,img)
            #print(obj_path)
            ctime = datetime.datetime.fromtimestamp(os.path.getctime(obj_path))
            #print(ctime)
            if ctime < (now - delta_time_sum):
                os.remove(obj_path)


def shot_img():
    global time_int
    path = "/home/asidemo/Env_test/img/"  ### location
    delete_pic(path, minutes = 1)
    success, frame = cameraCapture.read()
    
    #frame=cv2.flip(frame,1)
    now_time=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    outputpath=path +now_str+ '.jpg'
    
    cv2.imwrite(outputpath, frame)
    timer = threading.Timer(time_int, shot_img)
    timer.start()

if __name__ == '__main__':

    time_int = 10   ###set ? sec per img
    
    cameraCapture = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)
    
    #cameraCapture.set(cv2.CAP_PROP_FRAME_WIDTH,256)   ### set resolution 
    #cameraCapture.set(cv2.CAP_PROP_FRAME_HEIGHT,256)
    
    timer = threading.Timer(1,shot_img)
    timer.start()