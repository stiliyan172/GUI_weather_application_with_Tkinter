import tkinter as tk

HEIGHT = 500
WIDTH = 700

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Test button", font=40)
button.place(relx=0.7, relwidth=0.3, relheight=1)


label = tk.Label(frame, text="This is a label", bg='yellow')
# label.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)

root.mainloop()
