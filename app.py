import customtkinter as ctk
from tkinter import filedialog
import os
from ML_Model import BuildModel
import warnings
from PIL import Image
# from tkinter import PhotoImage

warnings.filterwarnings('ignore')


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("App")
        self.geometry("400x400")
        self.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.iconbitmap('Images/Logo.ico')
        self.folder_path = ctk.StringVar(value=os.getcwd())
        self.destination_path = ctk.StringVar(value=os.getcwd())
        self.model_name = ctk.StringVar()

        self.model_path = ctk.StringVar(value="--Select--")
        self.root = None

        self.createMainWindow()
        self.mainloop()

    def _clear(self):

        for widget in self.winfo_children():
            widget.destroy()

    def createMainWindow(self):

        self._clear()

        add_model_btn = ctk.CTkButton(master=self, text="Add Model", font=ctk.CTkFont(family="lucida", size=16),
                                      border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                      hover=True, command=self.addModelWindow)
        add_model_btn.place(relx=0.5, rely=0.4, anchor="center", relwidth=0.5, relheight=0.1)

        use_model_btn = ctk.CTkButton(master=self, text="Use Model", font=ctk.CTkFont(family="lucida", size=16),
                                      border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                      hover=True, command=self.useModelWindow)
        use_model_btn.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.5, relheight=0.1)

    def _askFolder(self):
        path = filedialog.askdirectory()
        if path == "":
            return

        self.folder_path.set(path)
        return

    def _training(self):
        try:
            model = BuildModel(self.folder_path.get())
            model.trainModel(self.model_name.get())

            self._clear()

            ctk.CTkLabel(self, text=f"Done Training For {self.model_name.get()}", font=ctk.CTkFont(
                family="lucida", size=14), compound="center").place(relx=0.5, rely=0.35, anchor="center", relwidth=1, relheight=0.2)

            done_btn = ctk.CTkButton(master=self, text="Done", font=ctk.CTkFont(family="lucida", size=16),
                                      border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                      hover=True, command=self.createMainWindow)
            done_btn.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.4, relheight=0.1)

        except:
            self._clear()

            ctk.CTkLabel(self, text=f"Some Error Occured", font=ctk.CTkFont(
                family="lucida", size=14), compound="center").place(relx=0.5, rely=0.5, anchor="center", relwidth=1,
                                                                    relheight=0.2)

    def _askDestinationFolder(self):
        path = filedialog.askdirectory()
        if path == "":
            return

        self.destination_path.set(path)
        return

    def _askNameWindow(self):

        self._clear()

        img = Image.open("images/arrow.png")

        back_btn = ctk.CTkButton(master=self,width=40, height=40,text="",
                                  border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                  hover=True, command=self.createMainWindow, image=ctk.CTkImage(img), compound="left")
        back_btn.place(relx=0.1, rely=0.1, anchor="center")

        ctk.CTkLabel(self, text="Enter The Name Of The Model", font=ctk.CTkFont(
            family="lucida", size=14), compound="center").place(relx=0.5, rely=0.35, anchor="center", relwidth=1, relheight=0.2)

        ctk.CTkEntry(self, corner_radius=5, border_width=2, font=ctk.CTkFont(family="lucida", size=14),
                     textvariable=self.model_name).place(
            relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.1
        )

        start_training_btn = ctk.CTkButton(master=self, text="Start Training", font=ctk.CTkFont(family="lucida", size=16),
                                  border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                  hover=True, command= self._training)

        start_training_btn.place(relx=0.5, rely=0.65, anchor="center", relwidth=0.5, relheight=0.1)

    def useModel(self):

        destination_folder = self.destination_path.get()
        model = BuildModel(self.folder_path.get())

        try:
            model.predictAndSave(self.folder_path.get(), destination_folder, self.model_path.get())
            self._clear()

            ctk.CTkLabel(self, text=f"Done Scanning\nFiles Are Saved In final folder", font=ctk.CTkFont(
                family="lucida", size=14), compound="center").place(relx=0.5, rely=0.35, anchor="center", relwidth=1,
                                                                    relheight=0.2)

            done_btn = ctk.CTkButton(master=self, text="Done", font=ctk.CTkFont(family="lucida", size=16),
                                     border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                     hover=True, command=self.createMainWindow)
            done_btn.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.4, relheight=0.1)
        except:

            self._clear()

            ctk.CTkLabel(self, text=f"Some Error Occured\nPlease Try Again Later", font=ctk.CTkFont(
                family="lucida", size=14), compound="center").place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=0.2)

    def getDestinationFolder(self):

        self._clear()

        img = Image.open("images/arrow.png")

        back_btn = ctk.CTkButton(master=self,width=40, height=40,text="",
                                  border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                  hover=True, command=self.createMainWindow, image=ctk.CTkImage(img), compound="left")
        back_btn.place(relx=0.1, rely=0.1, anchor="center")

        ctk.CTkLabel(self, text="Browse to the folder\nwhere you want to save the extracted files", font=ctk.CTkFont(
            family="lucida", size=14), compound="center").place(relx=0.5, rely=0.3, anchor="center", relwidth=1, relheight=0.2)

        ctk.CTkEntry(self, corner_radius=5, border_width=2, textvariable=self.destination_path, font=ctk.CTkFont(family="lucida", size=14), state="readonly").place(
            relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.1
        )

        browse_btn = ctk.CTkButton(master=self, text="Browse", font=ctk.CTkFont(family="lucida", size=14),
                                      border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                      hover=True, command=self._askDestinationFolder)
        browse_btn.place(relx=0.5, rely=0.7, anchor="center", relwidth=0.35, relheight=0.08)

        next_btn = ctk.CTkButton(master=self, text="Next", font=ctk.CTkFont(family="lucida", size=14),
                                      border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                      hover=True, command=self.useModel)
        next_btn.place(relx=0.5, rely=0.85, anchor="center", relwidth=0.35, relheight=0.08)

    def getTestFolder(self):

        if self.model_path == "--Select--":
            return

        self._clear()

        img = Image.open("images/arrow.png")

        back_btn = ctk.CTkButton(master=self,width=40, height=40,text="",
                                  border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                  hover=True, command=self.createMainWindow, image=ctk.CTkImage(img), compound="left")
        back_btn.place(relx=0.1, rely=0.1, anchor="center")

        ctk.CTkLabel(self, text="Browse to the folder\nwhere you want to use the model", font=ctk.CTkFont(
            family="lucida", size=14), compound="center").place(relx=0.5, rely=0.3, anchor="center", relwidth=1, relheight=0.2)

        ctk.CTkEntry(self, corner_radius=5, border_width=2, textvariable=self.folder_path, font=ctk.CTkFont(family="lucida", size=14), state="readonly").place(
            relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.1
        )

        browse_btn = ctk.CTkButton(master=self, text="Browse", font=ctk.CTkFont(family="lucida", size=14),
                                      border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                      hover=True, command=self._askFolder)
        browse_btn.place(relx=0.5, rely=0.7, anchor="center", relwidth=0.35, relheight=0.08)

        next_btn = ctk.CTkButton(master=self, text="Next", font=ctk.CTkFont(family="lucida", size=14),
                                      border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                      hover=True, command=self.getDestinationFolder)
        next_btn.place(relx=0.5, rely=0.85, anchor="center", relwidth=0.35, relheight=0.08)

    def addModelWindow(self):

        self._clear()

        img = Image.open("images/arrow.png")

        back_btn = ctk.CTkButton(master=self,width=40, height=40,text="",
                                  border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                  hover=True, command=self.createMainWindow, image=ctk.CTkImage(img), compound="left")
        back_btn.place(relx=0.1, rely=0.1, anchor="center")

        ctk.CTkLabel(self, text="Browse to the folder\nwhere you have the pictures of the model", font=ctk.CTkFont(
            family="lucida", size=14), compound="center").place(relx=0.5, rely=0.3, anchor="center", relwidth=1, relheight=0.2)

        ctk.CTkEntry(self, corner_radius=5, border_width=2, textvariable=self.folder_path, font=ctk.CTkFont(family="lucida", size=14), state="readonly").place(
            relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.1
        )

        browse_btn = ctk.CTkButton(master=self, text="Browse", font=ctk.CTkFont(family="lucida", size=14),
                                      border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                      hover=True, command=self._askFolder)
        browse_btn.place(relx=0.5, rely=0.7, anchor="center", relwidth=0.35, relheight=0.08)

        next_btn = ctk.CTkButton(master=self, text="Next", font=ctk.CTkFont(family="lucida", size=14),
                                      border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                      hover=True, command=self._askNameWindow)
        next_btn.place(relx=0.5, rely=0.85, anchor="center", relwidth=0.35, relheight=0.08)

    def useModelWindow(self):

        self._clear()
        # img = ImageTk.PhotoImage(Image.open("images/arrow.png"))
        img = Image.open("images/arrow.png")

        back_btn = ctk.CTkButton(master=self,width=40, height=40,text="",
                                  border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                  hover=True, command=self.createMainWindow, image=ctk.CTkImage(img), compound="left")
        back_btn.place(relx=0.1, rely=0.1, anchor="center")

        ctk.CTkLabel(self, text="Select The Model", font=ctk.CTkFont(
            family="lucida", size=14), compound="center").place(relx=0.5, rely=0.4, anchor="center", relwidth=1, relheight=0.2)

        models = []

        for entry in os.scandir("models"):
            path = entry.path[7:len(entry.path)-4]
            models.append(path)

        option_menu = ctk.CTkOptionMenu(self, corner_radius=5, values=models, variable=self.model_path, dropdown_hover_color="#337ab7", dropdown_fg_color="#5bc0de"
                                        , text_color="black", button_hover_color="#337ab7", button_color="#5bc0de", fg_color="#5bc0de")
        option_menu.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.07)

        ctk.CTkButton(master=self, text="Next", font=ctk.CTkFont(family="lucida", size=14),
                                      border_width=0, hover_color="#337ab7", fg_color="#5bc0de", text_color="black",
                                      hover=True, command=self.getTestFolder).place(relx=0.5, rely=0.65, anchor="center", relwidth=0.4, relheight=0.1)


if __name__ == "__main__":
    app = App()
