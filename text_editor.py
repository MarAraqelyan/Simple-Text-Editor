from tkinter import *
from tkinter import filedialog
from tkinter import font

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.root.geometry("500x500")

        # Font and Font-size
        fonts = ["Arial", "Rockwell"]

        self.my_font = font.Font(family="Arial", size=14)

        font_frame = Frame(self.root, pady=5, bg="lightgray")
        font_frame.pack(fill=BOTH, expand=True)

        font_label = Label(font_frame, text="Font")
        font_label.grid(row=0, column=0)

        selected_font = StringVar(font_frame)
        selected_font.set("Choose Font")

        drop_font = OptionMenu(font_frame, selected_font, *fonts, command=self.change_font)
        drop_font.grid(row=0, column=1, padx=5)


        font_label = Label(font_frame, text="Font-size")
        font_label.grid(row=0, column=2)

        selected_font = StringVar(font_frame)
        selected_font.set("Choose Font Size")

        drop_font = OptionMenu(font_frame, selected_font, *(range(2,70,4)), command=self.change_font_size)
        drop_font.grid(row=0, column=3, padx=5)


        # Textbox
        self.text_box = Text(self.root, wrap="word", padx=5, pady=5, font=self.my_font, undo=True, selectbackground="gray", selectforeground="black")
        self.text_box.place(relx=0, rely=0.1, relwidth=0.98, relheight=1)

        # Scrollbar
        self.scrollbar = Scrollbar(self.root, command=self.text_box.yview)
        self.scrollbar.place(relx=0.98, rely=0.1, relwidth=0.02, relheight=1)
        self.text_box.config(yscrollcommand=self.scrollbar.set)

        # Menu
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)


        # File_menu
        file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)


        # Edit_menu 
        edit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)


    def change_font(self, font):
        self.my_font.config(family=font)

    def change_font_size(self, font_size):
        self.my_font.config(size=font_size)
    
    def new_file(self):
        self.text_box.delete("1.0", END)

    def open_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.file_path:
            try:
                with open(self.file_path, "r") as file:
                    content = file.read()
                    self.text_box.delete("1.0", END)
                    self.text_box.insert(END, content)
            except Exception as e:
                print(f"Error while opening the file - {self.file_path}")

    def save_file(self):
        if hasattr(self, 'file_path') and self.file_path:
            with open(self.file_path, "w") as file:
                content = self.text_box.get("1.0", END)
                file.write(content)
        else:
            self.save_as()


    def save_as(self):
        self.file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if self.file_path:
            try:
                with open(self.file_path, "w") as file:
                    content = self.text_box.get("1.0", END)
                    file.write(content)
            except:
                print(f"Error while saving the file - {self.file_path}")

    def undo(self):
        try:
            self.text_box.edit_undo()
        except Exception as e:
            print(f"Nothing to undo" - {e})


    def redo(self):
        try:
            self.text_box.edit_redo()
        except Exception as e:
            print(f"Nothing to redo - {e}")

    def copy_text(self):
        self.text_box.event_generate("<<Copy>>")

    def cut_text(self):
        self.text_box.event_generate("<<Cut>>")

    def paste_text(self):
        self.text_box.event_generate("<<Paste>>")

if __name__ == "__main__":
    root = Tk()
    editor = TextEditor(root)
    root.mainloop()
