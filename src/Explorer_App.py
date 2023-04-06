# import libraries
import tkinter
import customtkinter as CTK
from PIL import Image

## Parent app setting - global
app_version = '1.0'
CTK.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
CTK.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(CTK.CTk):
    
    # Class variable
    test_chainList = ["Goerli","Sepolia", "Polygon"] # list of test network
    main_chainList = ["Ethereum", "Polygon"]

    def __init__(self):
        super().__init__()

        ## Global options
        self.title(f"ETH Explorer  v{app_version}")
        self.geometry("960x540+400+200") # WxH: use x (and not *)  |  + (or -) is to display the window on the screen (+x+y)
        # self.resizable(False, False)     # Fix the window movement (width and height)
        
        ## Top Frame and object inside
        self.frame_top = CTK.CTkFrame(self, width = 960, height= 90, corner_radius= 0, border_width = 1)
        self.frame_top.place(x=0, y=0)

        self.Testnet_MainNet_label = CTK.CTkLabel(self.frame_top, text="TestNet <-> MainNet", fg_color="transparent")
        self.Testnet_MainNet_label.place(x=45, y=10)

        self.chainList = App.test_chainList   # Assign test chains as default
        self.chain_switch_variable = CTK.StringVar(value = "TestNet")
        self.main_test_switch = CTK.CTkSwitch(self.frame_top, text="",
                                              variable=self.chain_switch_variable,
                                              command=self.select_Testnet_Mainnet,
                                              onvalue  = "MainNet", 
                                              offvalue = "TestNet",
                                              fg_color = '#8F43EE',
                                              progress_color = '#FFA3FD')
        self.main_test_switch.place(x=80, y=40)

        self.chain_variable = CTK.StringVar(value = None)
        self.chain_options = CTK.CTkOptionMenu(self.frame_top, 
                                               values= App.test_chainList,
                                               command= self.choose_chain,
                                               variable = self.chain_variable)
        self.chain_options.place(x= 200 , y= 30)

        self.connect_chain = CTK.CTkButton(self, text="Connect to Blockchain", command = self.show_blockchain_image)
        self.connect_chain.place(x= 500, y=30)

        ## Body content
        self.Block_info_label = CTK.CTkLabel(self, fg_color="transparent", 
                                             text= ":Block \n :Gas \n :Hash \n :Info")
        self.Block_info_label.place(x=880, y=180)

        self.Latest_block_var = tkinter.StringVar(value="00000000")
        self.Latest_block_info = CTK.CTkLabel(self, fg_color="red",text= ":Block \n :Gas \n :Hash \n :Info")
        self.Latest_block_info.place(x=800, y=180)

        self.SecLast_block_info = CTK.CTkLabel(self, fg_color="blue",text= ":Block \n :Gas \n :Hash \n :Info")
        self.SecLast_block_info.place(x=630, y=180)

        self.ThirdLast_block_info = CTK.CTkLabel(self, fg_color="green",text= ":Block \n :Gas \n :Hash \n :Info")
        self.ThirdLast_block_info.place(x=460, y=180)

        self.FourthLast_block_info = CTK.CTkLabel(self, fg_color="gray",text= ":Block \n :Gas \n :Hash \n :Info")
        self.FourthLast_block_info.place(x=290, y=180)

        self.Nth_block_info = CTK.CTkLabel(self, fg_color="pink",text= ":Block \n :Gas \n :Hash \n :Info")
        self.Nth_block_info.place(x=130, y=220)

        self.chain_image = CTK.CTkImage(light_image=Image.open("C:\GitHUB-Pranav\Personal\ETH_Explorer\Images\chain_image.png"), size=(672,107))
        self.chain_image_label = CTK.CTkLabel(self, text = '', image= None)
        self.chain_image_label.place(x=200, y=250)

        self.block_num_entry = CTK.CTkEntry(self, width = 110, height = 25, 
                                       placeholder_text = "Block number ",
                                       corner_radius = 5,
                                       fg_color = '#F9F5EB',
                                       placeholder_text_color = '#37306B',
                                       text_color =  '#37306B',
                                       state = "normal"
                                       )
        self.block_num_entry.place(x= 110 , y= 298)


    def show_blockchain_image(self):
        self.chain_image_label.configure(image = self.chain_image)

    def choose_chain(self, _chain):
        self.chain_variable = _chain
        print (f"Current selected chain is {self.chain_variable}")

    def select_Testnet_Mainnet(self):
        print (f"Selected {self.chain_switch_variable.get()}")
        if(self.chain_switch_variable.get() == "TestNet"):
            self.chainList = App.test_chainList
            self.chain_options.configure(values = App.test_chainList)
        else:
            self.chainList = App.main_chainList
            self.chain_switch_variable.set(value = App.main_chainList[0])  # update the default entry to show the var
            self.chain_options.configure(values = App.main_chainList)



if __name__ == "__main__":
    app = App()
    app.mainloop() 


