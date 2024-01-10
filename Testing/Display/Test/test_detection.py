#Basic Libraries
import kivy
from kivy.app import App
from kivy.lang import Builder


#Uxi Libraries
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.clock import Clock

import cv2

#loading design file
Builder.load_file("Testing/design/Test_Detection.kv")

class Detection_Layout(Widget):
    pass

class Detection(App):
    def build(self):
        return Detection_Layout
    
Detection().run()