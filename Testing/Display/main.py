#Important libraries for GUI

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics.texture import Texture
from kivy.uix.floatlayout import FloatLayout

#Important for Detection Libraries
import os
import cv2
import torch
import numpy as np


Builder.load_file("GUI.kv")
torch.cuda.empty_cache


class design(FloatLayout):
    pass


class GUI(App):
    
    def build(self):
        
        self.root = design()
        
        self.det =Image(
            source= "",
            size_hint=(None, None),
            width= 800,
            height=610,
            pos_hint={'x':.10, 'y':.29})
        self.root.add_widget(self.det)
        
        self.images()
        
        
        
        self.dets = Label(
            background_color=(1,1,1,1),
            text='Press Start Button',
            font_size=35,
            color= (0,0,0,1),
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
        )
        
        self.Start.bind(on_press=self.start)
        torch.cuda.empty_cache
        self.root.add_widget(self.Start)
        self.item = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/Final_Data_Items_small/weights/last.pt', source='local')
        self.damage = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/Final_Data_Damages_small/weights/last.pt', source='local')
        # Window.fullscreen = 'auto'
        return self.root
    
    def images(self, sor=""):
        img = Image(
        source= sor,
        size_hint=(None, None),
        width= 500,
        height=650,
        pos_hint={'x':.65, 'y':.28})
        self.root.add_widget(img)
            
    def start(self,id):
        self.item_list = []
        self.damage_list = []
        self.capture = cv2.VideoCapture('https://192.168.18.15:8080/video')
        Clock.schedule_interval(self.update, 1.0/30.0)
            
    def update(self,dt):
        ret, frame = self.capture.read()
        if ret:
            self.camEdit(frame)
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tobytes()
            img_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            img_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.det.texture = img_texture
        else:
            self.dets.text="Can't connect to the Camera"
            self.dets.color=(1,1,1,1)
            self.dets.background_color=(1, 0, 0,1)
   
            
    def camEdit(self,frames):
        resize = cv2.resize(frames,(500,500))
        gray_frames = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
        self.Detect_Items(gray_frames)
        
    def Detect_Items(self,frames):
        detect_item = self.detect_model(self.item,frames)
        detect_item_img=np.squeeze(detect_item.render())
        listss = self.item_name(detect_item,self.item_list)
        lens = len(listss)
        if lens == 0:
            self.images('')
        else:
            print(self.item_list[-1])
            if self.item_list[-1] == "ItemA":
                self.Detect_Damage(frames,detect_item_img,'ItemA')
            elif self.item_list[-1] == "ItemB":
                self.Detect_Damage(frames,detect_item_img,'ItemB')
            elif self.item_list[-1] == "ItemC":
                self.Detect_Damage(frames,detect_item_img,'ItemC')
                
            
    def Detect_Damage(self, frames, imgs, Items):
        detect_damage = self.detect_model(self.damage,frames)
        detect_damage_img=np.squeeze(detect_damage.render())
        damage_lists = self.item_name(detect_damage,self.damage_list)
        lens = len(damage_lists)
        if lens == 0:
            self.damage_list = []
            # print(self.damage_list)
            self.dets.color=(1,1,1,1)
            self.dets.background_color=(80/225, 222/255, 87/225,1)
            # self.dets.color=(0,0,0,1)
            if Items == 'ItemA':
                self.images("/home/usamah/Documents/office_project/Damage_Detection/Testing/Display/Images/ItemA-Clear.png")
                print(f'ItemA Clear')
                self.dets.text=f"ItemA Clear"
            elif Items == 'ItemC':
                self.images("/home/usamah/Documents/office_project/Damage_Detection/Testing/Display/Images/ItemC-Clear.png")
                print(f'ItemC Clear')
                self.dets.text=f"ItemC Clear"
            else:
                self.images("")
        else:
            self.dets.color=(1,1,1,1)
            self.dets.background_color=(1,0,0,1)
            if Items == 'ItemA':
                self.images("/home/usamah/Documents/office_project/Damage_Detection/Testing/Display/Images/ItemA-Damaged.png")
                print(f'ItemA Damage')
                self.dets.text=f"ItemA Damage"
            elif Items == 'ItemC':
                self.images("/home/usamah/Documents/office_project/Damage_Detection/Testing/Display/Images/ItemC-Damage.png")
                print(f'ItemC Damage')
                self.dets.text=f"ItemC Damege"
            else:
                self.images("")
            # print(self.damage_list)
        self.item_list = []
        self.damage_list = []
        # print("list is empty")
            
        
    def detect_model(self,models,frames):
        return models(frames)
    
    def item_name(self,name,lists):
        names = name.pandas().xyxy[0]
        for i in names['name']:
            lists.append(i)
        return lists        

    
    def show_Imgs_Status(self,status,items,imgs):
            
        # cv2.imwrite(f'{status}_{items}.png',imgs)
        self.images("{items}-{status}.png")
        print(f'{items}-{status}')
        self.dets.text=f"{items} {status}"
        # os.remove(f"{status}_{items}.png")
        
    

      
if __name__ == "__main__":
    GUI().run()