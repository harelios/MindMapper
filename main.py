from Structure_Extractor import extractor
from graph_builder import builder 
from renderer import renderer
from tkinter import * 
from tkinter import Tk,ttk,END
import tkinter as tk
from tkinter import simpledialog

root = Tk()
root.title("MindMapper")
root.geometry("100x100")

text_area = Text(root,height=25,width=140)
text_area.pack()

valeur = StringVar()
valeur.set("")

style = ttk.Style()
style.configure("Hover.TButton", font=("Arial",12,"bold"),foreground="black",background="#5865F2",padding="10")
#finir de créer l'interface

def main():
            sentence_user = text_area.get("1.0",END)
            if sentence_user:
                extract = extractor(sentence_user)
                graph,edge_labels = builder(extract)
                render = renderer(graph,edge_labels)
            else:
                text_area.insert("Enter a valid sentence : \n")


def on_enter(e):
    return e.widget.configure(style="Hover.TButton")

def on_leave(e):
    return e.widget.configure(style="Hover.TButton")

Button_Ok = ttk.Button(root, text="Ok",command=main, style="TButton")
Button_Ok.bind("<Enter>", on_enter)
Button_Ok.bind("<Leave>",on_leave)
Button_Ok.pack()
            
            
root.mainloop()        
if __name__ == "__main__":
    main()