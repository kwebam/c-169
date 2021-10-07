from tkinter import *

root = Tk()
root.geometry("900x600")
root.title("Classes")

class CreateElement:
    
    def __init__(self):
        print("This is Create Elements class")
        
    def CreateNewElement(self):
        label = Label(root, text = "A new label is been Created Using Class", fg = "red")
        label.pack()
        class_btn = Button(root, text = "Button", command = self.message)
        class_btn.pack(padx = 20, pady = 10)
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button created using class")
        
obj_of_CreateElement = CreateElement()
btn = Button(root, text = "click to create button and label Element", command = obj_of_CreateElement.CreateNewElement)
btn.pack(padx = 20, pady = 10)

root.mainloop()