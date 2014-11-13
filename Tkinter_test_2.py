import Tkinter as tk
import ttk

class Example(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.floater = FloatingWindow(self)

class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        # tk.Toplevel.__init__(self, *args, **kwargs)
        pass
        self.overrideredirect(True)
        self.wm_geometry("400x400")

app=Example()
app.mainloop()