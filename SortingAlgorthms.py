from tkinter import *
from tkinter import ttk
import random
from Algorithm import bubble_sort, quick_sort, merge_sort

def generate():
    global data
    print('Alg Selected: ' + selected_alg.get())

    minVal = 1

    maxVal = int(maxEntry.get())

    size = int(sizeEntry.get())
    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))
    drawData(data, ['red' for x in range(len(data))])



def drawData(data, colorArray):
    canvas.delete("all")
    c_height = screen_height
    c_width = screen_width
    x_width = c_width / (len(data) +1)

    spacing = 2
    normalizeData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizeData):
        #topleft corner
        x0 = i * x_width + spacing
        y0 = c_height - height * 1400
        #bottom right
        x1 = (i + 1) * x_width
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()

def startAlgorithm():
    global data
    if not data: return

    if(algMenu.get() == 'Quick Sort'):
        quick_sort(data ,0, len(data)-1, drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])
    elif (algMenu.get() == 'Bubble Sort'):
      bubble_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())


root = Tk()
root.title('Sorting Algorithm')
root.attributes('-fullscreen', False)
root.config(bg='#FCFCFC')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


selected_alg = StringVar()
data = []

# frame and base layout
UI_frame = Frame(root, width= screen_width, height=100, bg='#EFEFEF')
UI_frame.grid(row=0, column=0, sticky="ew")

canvas = Canvas(root, width=screen_width, height=screen_height-100, bg='#FCFCFC')
canvas.grid(row=1, column=0)

Label(UI_frame, text="Algorithm").grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort', 'Quick Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

Button(UI_frame, text="Generate", command=generate, bg='white').grid(row=0, column=2, padx=40, pady=5)


sizeEntry = Scale(UI_frame, from_=10, to=500, length=150, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=0, column=4, padx=5, pady=5)

Label(UI_frame).grid(row=0, column=5, padx=30, pady=5)


maxEntry = Scale(UI_frame, from_=1, to=1000, length=150, digits=2, resolution=0.2, orient=HORIZONTAL, label="Max")
maxEntry.grid(row=0, column=7, padx=5, pady=5)

Label(UI_frame).grid(row=0, column=8, padx=30, pady=5)

speedScale = Scale(UI_frame, from_=0.02, to=1.0, length=150, digits=3, resolution=0.02, orient=HORIZONTAL, label="Speed")
speedScale.grid(row=0, column=9, padx=5, pady=5)

Button(UI_frame, text="Start", command=startAlgorithm, width=10, bg='#3DADF2').grid(row=0, column=10, padx=40, pady=5)

root.mainloop()



