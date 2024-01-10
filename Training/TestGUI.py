from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.texture import Texture
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.app import App
import cv2


class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)
        

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # convert it to texture
            frames = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            buf1 = cv2.flip(frame, 0)
            # buf = buf1.tostring()
            buf = buf1.tobytes()
            image_texture = Texture.create(
                size=(frames.shape[1], frames.shape[0]), colorfmt='luminance')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture
            
class Design(App):
    def build(self):        
        # Window.fullscreen = "auto"
        self.root = FloatLayout()
        
        
        return self.root
    
    
if __name__ == "__main__":
    Design().run()