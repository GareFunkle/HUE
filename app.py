import tkinter as tk
import time


framelist = []
frame_index = 0
count = 0
animation_speed = 1
# frame_index += animation_speed

_tick2_frame=0
_tick2_fps=20000000 # real raw FPS
_tick2_t0=time.time()


def animate_gif(count):
    l1.config(image = framelist[count])
    count += 1
    
    if count > last_frame :
        count = 0
    
        
    window.after(100, lambda : animate_gif(count))
    
def tick(fps=60):
    global _tick2_frame,_tick2_fps,_tick2_t0
    n=_tick2_fps/fps
    _tick2_frame += n
    while n > 0: 
        n -= 1
    if time.time()-_tick2_t0>1:
        _tick2_t0=time.time()
        _tick2_fps=_tick2_frame
        _tick2_frame=0
    


    

window = tk.Tk()

window.title("H.U.E")
window.geometry("540x300")
window.minsize(50, 50)
window.maxsize(540, 300)


while True:
    tick(60) #1 frame per second
    print(_tick2_fps) #see adjustment in action
    try:
        part = 'gif -index {}'.format(frame_index)
        frame = tk.PhotoImage(file='assets/BLkE.gif', format = part)
    except:
        print("break")
        last_frame = frame_index -1
        break
    framelist.append(frame)
    print(len(framelist), "frame")
    frame_index += animation_speed
        
        
l1 = tk.Label(window, bg = '#202020', image = '')
l1.pack()


start_button = tk.Button(window, text="start", command= lambda : animate_gif(0))
start_button.pack()

window.mainloop()





