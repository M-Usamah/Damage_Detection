from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: left
        resolution: (640, 480)
        play: False
    Camera:
        id: right
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: left.play = not left.play
        on_press:right.play = not right.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['left']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()































# import kivy
# from kivy.app import App
# from kivy.clock import Clock
# from kivy.lang import Builder

# from kivy.uix.image import Image
# from kivy.uix.widget import Widget

# from kivy.graphics.texture import Texture

# import cv2
# from threading import Thread

# Builder.load_file("Testing/design/detection.kv")


# class KivyCamera(Image):
    
#     def __init__(self, **kwargs):
#         super(KivyCamera, self).__init__(**kwargs)
#         self.capture = None

#     def start(self, capture, fps=30):
#         self.capture = capture
#         Clock.schedule_interval(self.update, 1.0 / fps)

#     def stop(self):
#         Clock.unschedule_interval(self.update)
#         self.capture = None

#     def update(self, dt):
#         return_value, frame = self.capture.read()
#         if return_value:
#             texture = self.texture
#             w, h = frame.shape[1], frame.shape[0]
#             if not texture or texture.width != w or texture.height != h:
#                 self.texture = texture = Texture.create(size=(w, h))
#                 texture.flip_vertical()
#             texture.blit_buffer(frame.tobytes(), colorfmt='bgr')
#             self.canvas.ask_update()

# capture = None

# def cam(idss):
#     return cv2.VideoCapture(idss)
    

# class detection_layout(Widget):
#     def layout(self):
#         pass
#     def dostart(self,*largs):
#         global capture
#         # right=cv2.VideoCapture(0)
#         t1= Thread(target = cam,args=(0))
#         t1.start()
#         # left = t1.join()
#         # left=cv2.VideoCapture(2)
#         self.ids.left_cam.start(t1)

# class Detection(App):
#     def build(self):
#         return detection_layout()


# if __name__ == "__main__":
#     Detection().run()