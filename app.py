import tkinter as tk

framelist = []
frame_index = 0
count = 0

def animate_gif(count):
    l1.config(image = framelist[count])
    count +=1
    
    if count > last_frame :
        count = 0
        
    window.after(100, lambda : animate_gif(count))


window = tk.Tk()

window.title("H.U.E")
window.geometry("540x300")
window.minsize(50, 50)
window.maxsize(540, 300)


while True:
        try:
            part = 'gif -index {}'.format(frame_index)
            frame = tk.PhotoImage(file='/Users/vincent/Downloads/BLkE.gif', format = part)
        except:
            print("break")
            last_frame = frame_index -1
            break
        framelist.append(frame)
        print(len(framelist), "frame")
        frame_index += 1
        
l1 = tk.Label(window, bg = '#202020', image = '')
l1.pack()


start_button = tk.Button(window, text="start", command= lambda : animate_gif(0))
start_button.pack()

window.mainloop()