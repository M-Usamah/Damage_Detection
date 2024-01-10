# import tkinter as tk

# root = tkinter.Tk()
# # root.overrideredirect(True)
# # root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# root.minsize(500, 500)
# # root.maxsize(500, 500)

# root.frame()
 
# root.mainloop()
from tkinter import *

root = Tk()  # create root window
root.title("Frame Example")
# root.minsize(520, 500)
root.config(bg="skyblue")

root_frame_1 = Frame(root, width=800, height=800)
root_frame_1.grid(row=0, column=0,padx=(1,1),pady=(1,1))


root_frame_2 = Frame(root, width=800, height=100)
root_frame_2.grid(row=1, column=0,padx=(0,0),pady=(0,0))

root_frame_3 = Frame(root, width=800, height=100)
root_frame_3.grid(row=1, column=1,padx=(0,0),pady=(0,0))
# camera_frame_2 = Frame(root, width=850, height=850)
# camera_frame_2.grid(row=0, column=1,padx=0,pady=0)



# bottom_frame = Frame(root,width=50, height=400)
# bottom_frame.grid(row=1, column=0,padx=0,pady=0)
root.mainloop()