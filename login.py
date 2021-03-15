import tkinter as tk

class MyApp(tk.Frame):
    def __init__(self, master = None):
    super().__init__(master)
    self.master = master
    self.pack()
    self.create_widget()

root = tk.Tk()
app = MyApp(master = root)

app.mainloop