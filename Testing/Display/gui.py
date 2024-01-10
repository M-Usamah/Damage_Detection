import cv2
import torch
import pandas
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics.texture import Texture
from kivy.uix.floatlayout import FloatLayout





Builder.load_file("GUI.kv")

class design(FloatLayout):
    pass
        
        

class GUI(App):
    def build(self):
        self.model = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/Final_Data_Item/weights/last.pt', source='local')
        self.damage = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/Final_Data_Damaged/weights/last.pt', source='local')
        self.models = []
        self.damages = []
        # Window.fullscreen = 'auto'
        self.root = design()
        
        self.det =Image(
            source= "",
            size_hint=(None, None),
            width= 800,
            height=610,
            pos_hint={'x':.10, 'y':.29})
        self.root.add_widget(self.det)
        
        self.img = Image(
            source= "",
            size_hint=(None, None),
            width= 500,
            height=650,
            pos_hint={'x':.65, 'y':.28})
        self.root.add_widget(self.img)
        
        
        self.dets = Label(
            # background_color:(188/255, 190/255, 194/255,1)
            text='',
            color= (1,0,0,1),
            size_hint=(None, None),
            width= 500,
            height=50,
            pos_hint={'x':.65, 'y':.20}
            )
        self.root.add_widget(self.dets)
        
        self.Start = Button(
            text='Start',
            size_hint= (None, None),
            width= 150,
            height=50,
            pos_hint={'x':.46, 'y':.05},
            # on_press: root.detects()
        )
        
        self.Start.bind(on_press=self.detects)
        
        self.root.add_widget(self.Start)

        
        # print(self.detect())
        return self.root
    
    def detects(self,id):
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/30.0)
    
    def update(self,dt):


        ret, self.frame = self.capture.read()
        resize = cv2.resize(self.frame,(500,500))
        self.frames = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
        
        buf1 = cv2.flip(self.frame, 0)
        buf1 = cv2.flip(self.frame, 0)
        
        buf = buf1.tobytes()
        img_texture = Texture.create(size=(self.frame.shape[1], self.frame.shape[0]), colorfmt='bgr')
        img_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        det = self.model(self.frames)
        df = det.pandas().xyxy[0]
        for i in df['name']: # name->labels
            self.models.append(i)
        if len(self.models) == 0:
    
            self.img = Image(
                source= "",
                size_hint=(None, None),
                width= 500,
                height=650,
                pos_hint={'x':.65, 'y':.28})
            self.root.add_widget(self.img)
            print("No detection")
            
            self.dets = Label(
            # background_color:(188/255, 190/255, 194/255,1)
            text='',
            color= (1,0,0,1),
            size_hint=(None, None),
            width= 500,
            height=50,
            pos_hint={'x':.65, 'y':.20}
            )
            self.root.add_widget(self.dets)
            
            pass
        
        
        else:
            inf = self.models[-1]
            if inf == "ItemA":
                self.itemDetec('ItemA')
                               
                
            elif inf == "ItemB":
                 self.itemDetec('ItemB')
                # print("ok 2")
                # self.img = Image(
                #     source= "ItemB-Clear.jpg",
                #     size_hint=(None, None),
                #     width= 500,
                #     height=650,
                #     pos_hint={'x':.65, 'y':.28})
                # self.root.add_widget(self.img)
                # self.lst = []
                # print(self.lst)
            elif inf == "ItemC":
                 self.itemDetec('ItemC')
                # print("ok 3")
                
                # self.img = Image(
                #     source= "ItemC-Clear.jpeg",
                #     size_hint=(None, None),
                #     width= 500,
                #     height=650,
                #     pos_hint={'x':.65, 'y':.28})
                # self.root.add_widget(self.img)
                # self.lst = []
                # print(self.lst)
    
        
        self.det.texture = img_texture
    def itemDetec(self,Item):  
        print(Item)
        dam = self.damage(self.frames)
        dt = dam.pandas().xyxy[0]
        for i in dt['name']: # name->labels
            self.damages.append(i)
        if self.damages == 0:
            Items = str(Item)+"-Clear.jpg" 
            print(Items)    
            self.img = Image(
                source= Items,
                size_hint=(None, None),
                width= 500,
                height=650,
                pos_hint={'x':.65, 'y':.28})
            self.root.add_widget(self.img)
            self.dets = Label(
            # background_color:(188/255, 190/255, 194/255,1)
                text='Clear',
                color= (1,0,0,1),
                size_hint=(None, None),
                width= 500,
                height=50,
                pos_hint={'x':.65, 'y':.20}
            )
            self.root.add_widget(self.dets)
            self.models = []
            # print(self.lst)
        else:
            Items = str(Item)+"-Clear.jpg" 
            print(Items)    
            self.img = Image(
                source= Items,
                size_hint=(None, None),
                width= 500,
                height=650,
                pos_hint={'x':.65, 'y':.28})
            self.root.add_widget(self.img)
            self.dets = Label(
            # background_color:(188/255, 190/255, 194/255,1)
                text=Item,
                color= (1,0,0,1),
                size_hint=(None, None),
                width= 500,
                height=50,
                pos_hint={'x':.65, 'y':.20}
            )
            self.root.add_widget(self.dets)
            
            self.models = []
            self.damages = []
            # print(self.lst)
        # damg = self.ls[-1]
        
        # Items = str(Item)+"-Clear.jpg" 
        # print(Items)    
        # self.img = Image(
        #     source= Items,
        #     size_hint=(None, None),
        #     width= 500,
        #     height=650,
        #     pos_hint={'x':.65, 'y':.28})
        # self.root.add_widget(self.img)
        # self.lst = []
        # print(self.lst)


if __name__ == "__main__":
    GUI().run()

