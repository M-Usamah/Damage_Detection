# import cv2
# import os

# def read(path):
#     img = cv2.imread(path)
#     return img

# Path = "Training/Car_parts/"

# # lst = []
# i = 0

# for im in os.listdir(Path):
    
#     Pat = os.listdir(Path)
#     img = os.listdir(Path + im)
#     Img = Path + Pat[i] +'/' + img[i]
#     print(Img)
    
#     originalImage = read(Img)
#     grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
#     resize = cv2.resize(originalImage, (800, 800))
#     filename = f"test{i}.jpg"
#     cv2.imwrite(filename, resize)
#     i+=1
    

# for ls in lst:
#     print(ls[1])

# for im in os.listdir(Path):
#     path = 'Training/Car_parts/' + lst[0]
#     originalImage = read(path)
#     grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
#     resize = cv2.resize(grayImage, (800, 800))
#     cv2.imshow("test",resize)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     filename = 'Hello.jpg'
#     cv2.imwrite(filename, resize)



import cv2
# import os


# os.chdir('/home/usamah/Documents/DataD')
# save = ('/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Gray/Damages')
# ls = os.listdir('/home/usamah/Documents/DataD')


# i = 0
# for n in ls:
#     img = cv2.imread(n)
#     grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     resize = cv2.resize(grayImage, (500, 500))
#     image = cv2.rotate(resize , cv2.ROTATE_180)
#     cv2.imwrite(f'/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Gray/Damages/{i}.png', image)
#     print(i)
#     i = i+1


    
  
   
    



# class Data_Agmentation_Cv2:
#     def __init__(self) -> None:
#         pass
#     def read(self):
#         pass
# import torch
# from matplotlib import pyplot as plt
# import numpy as np
# import cv2

# model = torch.hub.load('ultralytics/yolov5', 'custom', path='last.pt', force_reload=True)



# cap = cv2.VideoCapture(0)
# while cap.isOpened():
#     ret, frame = cap.read()
    
#     # Make detections 
#     results = model(frame)
#     # print(results)
#     cv2.imshow('YOLO', np.squeeze(results.render()))
   
    
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
# import cv2
# import os
# # print(os.listdir())
# os.chdir('Training/datasets/Data')
# # print(os.listdir())
# data = cv2.imread('20221228_113505.jpg')
# cv2.imshow('image',data)
# cv2.waitKey(0)
# # It is for removing/deleting created GUI window from screen
# # and memory
# cv2.destroyAllWindows()





# from kivy.app import App
# from kivy.clock import Clock
# from kivy.uix.image import Image
# from kivy.uix.boxlayout import BoxLayout
# import cv2

# class kivyCame(Image):
#     def __init__(self, caputer,fps, **kwargs):
#         super(super()).__init__(**kwargs)
#         self.capture = caputer
#         Clock.schedule_interval(self.update, 1.0 / fps)
    
#     def update(self, dt):
#         ret, frame = self.capture.read()
#         try:
#             buf1 = cv2.flip(frame,0)
#             buf = buf1.tostring()
#         except TypeError:
#             print("camera not connected")
        
    
    
# from kivy.app import App
# from kivy.uix.image import Image
# from kivy.clock import Clock
# from kivy.uix.boxlayout import BoxLayout
# from kivy.graphics.texture import Texture
# import cv2


# class KivyCamera(Image):
#     def __init__(self, capture, fps, **kwargs):
#         super(KivyCamera, self).__init__(**kwargs)
#         self.capture = capture
#         Clock.schedule_interval(self.update, 1.0 / fps)

#     def update(self, dt):
#         ret, frame = self.capture.read()
#         if ret:
#             # convert it to texture
#             frames = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             buf1 = cv2.flip(frame, 0)
#             # buf = buf1.tostring()
#             buf = buf1.tobytes()
#             image_texture = Texture.create(
#                 size=(frames.shape[1], frames.shape[0]), colorfmt='luminance')
#             # image_texture = Texture.create(
#                 # size=(frames.shape[1], frames.shape[0]), colorfmt='rgb')
#             image_texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
#             # image_texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
#             # display image from the texture
#             self.texture = image_texture


# class CamApp(App):
#     def build(self):
#         self.layer = BoxLayout(orientation="vertical")
#         self.capture1 = cv2.VideoCapture(0)
#         self.my_camera1 = KivyCamera(capture=self.capture1, fps=30)
#         self.layer.add_widget(self.my_camera1)
#         # self.capture2 = cv2.VideoCapture(2)
#         # self.my_camera2 = KivyCamera(capture=self.capture2, fps=30)
#         # self.layer.add_widget(self.my_camera2)
#         return self.layer

#     def on_stop(self):
#         #without this, app will not exit even if the window is closed
#         self.capture1.release()
#         # self.capture2.release()


# if __name__ == '__main__':
#     CamApp().run()


