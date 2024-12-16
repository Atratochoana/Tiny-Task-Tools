import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Vanguards Macros")
        self.geometry("700x500")
        self.resizable(False,False)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.sideBarFrame = ctk.CTkFrame(master=self,width=150,corner_radius=0)
        self.sideBarFrame.grid(sticky="nesw",column=0,row=0)
        self.mainFrame = ctk.CTkFrame(master=self,width=500,corner_radius=0,fg_color=("gray75", "gray25"))
        self.mainFrame.grid(sticky="news",column=1,row=0)

        #---------Frames----------#
        self.macroFrame = macroFrame(self)
        self.webhookFrame = webhookFrame(self)
        self.creatorFrame = creatorFrame(self)
        self.settingFrame = settingFrame(self)
        self.infoFrame = infoFrame(self)



        #------------ SideBar -------------#
        self.sideBarFrame.grid_rowconfigure(6, weight=1)


        self.sideBarLabel = ctk.CTkLabel(master=self.sideBarFrame,text="Sidebar",font=ctk.CTkFont(size=30))
        self.sideBarLabel.grid(row=0,column=0, padx=20, pady=10)
        self.macroButton = ctk.CTkButton(master=self.sideBarFrame, corner_radius=0, text="Macro", border_spacing=10, height=40,
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        anchor="w", command=lambda : self.select_frame_by_name("macro"),font=ctk.CTkFont(size=25))
        self.macroButton.grid(row=1,column=0, sticky="ew")
        self.webhookButton = ctk.CTkButton(master=self.sideBarFrame, corner_radius=0, text="Webhook", border_spacing=10, height=40,
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        anchor="w", command=lambda : self.select_frame_by_name("webhook"),font=ctk.CTkFont(size=25))
        self.webhookButton.grid(row=2,column=0, sticky="ew")
        self.creatorButton = ctk.CTkButton(master=self.sideBarFrame, corner_radius=0, text="Creator", border_spacing=10, height=40,
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        anchor="w", command=lambda : self.select_frame_by_name("creator"),font=ctk.CTkFont(size=25))
        self.creatorButton.grid(row=3,column=0, sticky="ew")
        self.settingsButton = ctk.CTkButton(master=self.sideBarFrame, corner_radius=0, text="Settings", border_spacing=10, height=40,
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        anchor="w", command=lambda : self.select_frame_by_name("setting"),font=ctk.CTkFont(size=25))
        self.settingsButton.grid(row=4,column=0, sticky="ew")
        self.infoButton = ctk.CTkButton(master=self.sideBarFrame, corner_radius=0, text="Info", border_spacing=10, height=40,
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        anchor="w", command=lambda : self.select_frame_by_name("info"),font=ctk.CTkFont(size=25))
        self.infoButton.grid(row=5,column=0, sticky="ew")
        self.appearance_mode_menu = ctk.CTkOptionMenu(self.sideBarFrame, values=["System", "Dark", "Light"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")


        self.select_frame_by_name("macro")
        
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.macroButton.configure(fg_color=("gray75", "gray25") if name == "macro" else "transparent")
        self.webhookButton.configure(fg_color=("gray75", "gray25") if name == "webhook" else "transparent")
        self.creatorButton.configure(fg_color=("gray75", "gray25") if name == "creator" else "transparent")
        self.settingsButton.configure(fg_color=("gray75", "gray25") if name == "setting" else "transparent")
        self.infoButton.configure(fg_color=("gray75", "gray25") if name == "info" else "transparent")

        # show selected frame
        if name == "macro":
            self.macroFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.macroFrame.grid_forget()
        if name == "webhook":
            self.webhookFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.webhookFrame.grid_forget()
        if name == "creator":
            self.creatorFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.creatorFrame.grid_forget()
        if name == "setting":
            self.settingFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.settingFrame.grid_forget()
        if name == "info":
            self.infoFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.infoFrame.grid_forget()
        
    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)
        

class macroFrame(ctk.CTkFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._corner_radius = 0
        self._fg_color = "transparent"
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.label = ctk.CTkLabel(master=self,text="MACROFRAME")
        self.label.grid(row=0,column=0,sticky="nesw")
    
class webhookFrame(ctk.CTkFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._corner_radius = 0
        self._fg_color = "transparent"
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.label = ctk.CTkLabel(master=self,text="WEBHOOK")
        self.label.grid(row=0,column=0,sticky="nesw")

class creatorFrame(ctk.CTkFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._corner_radius = 0
        self._fg_color = "transparent"
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.label = ctk.CTkLabel(master=self,text="Creator")
        self.label.grid(row=0,column=0,sticky="nesw")
    
class settingFrame(ctk.CTkFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._corner_radius = 0
        self._fg_color = "transparent"
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.label = ctk.CTkLabel(master=self,text="Settings")
        self.label.grid(row=0,column=0,sticky="nesw")

class infoFrame(ctk.CTkFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._corner_radius = 0
        self._fg_color = "transparent"
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.label = ctk.CTkLabel(master=self,text="Developed independently by @atratochoana")
        self.label.grid(row=0,column=0,sticky="nesw")

app = App()
app.mainloop()

