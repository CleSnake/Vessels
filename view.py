import tkinter as tk

# import controller


class View(tk.Tk):

    def main(self):
        if __name__ == '__main__':

            view = View()

    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.start_params()
        self.get_message("start")
        self.water_var = tk.StringVar()
    def open_main(self,controller):
        self.create()

    @staticmethod
    def start_params():
        global object_name
        global is_next
        global hydration
        global max_thirst
        global is_start
        object_name = ""
        is_next = True
        is_start = True
        hydration = ""
        max_thirst = ""

    @staticmethod
    def disable_next():
        global is_next
        is_next = not is_next
    @staticmethod
    def disable_else():
        global is_start
        is_start = not is_start
    @staticmethod
    def getvariables_drinker(params):
        global object_name
        global hydration
        global max_thirst

        object_name = params["name"]
        hydration = params["Volume"]
        max_thirst = params["Max Volume"]
    @staticmethod
    def getvariables_container(params):
        global vessel_name
        global volume
        global max_volume
        vessel_name = params["name"]
        volume = params["Volume"]
        max_volume = params["Max Volume"]
    def get_message(self,p1):
        global message
        global is_error
        is_error = False
        if p1 != "start":
            message = p1
        else:
            message = "The first day of work at the waterhole. We are waiting for the first customer, click next"

    def get_error_message(self,p1):
        global message
        global is_error
        is_error = True
        message = p1
    def create(self):
        global is_start
        self.title("Vessels: CleSnake")

        self.textfield_object = tk.Label(text=object_name,height=2,borderwidth=4,relief="groove",width=30)

        self.textfield_object_vessel = tk.Label(text=vessel_name, height=2, borderwidth=4, relief="groove", width=30)

        self.textfield_thirst = tk.Label(text="hydration:", borderwidth=4, relief="groove", width=15)

        self.thirst = tk.Label(text=hydration, borderwidth=4, relief="groove", width=15)

        self.textfield_volume = tk.Label(text="Water volume:", borderwidth=4, relief="groove", width=15)

        self.volume = tk.Label(text=volume, borderwidth=4, relief="groove", width=15)

        self.textfield_thirst_max = tk.Label(text="Sufficient hydration:", borderwidth=4, relief="groove", width=15)

        self.thirst_max = tk.Label(text=max_thirst, borderwidth=4, relief="groove", width=15)

        self.textfield_volume_max = tk.Label(text="Vessel volume", borderwidth=4, relief="groove", width=15)

        self.volume_max = tk.Label(text=max_volume, borderwidth=4, relief="groove", width=15)

        self.water_entry = tk.Entry(textvariable=self.water_var,width=18)

        self.next_bt = tk.Button(command=self.controller.nexto,text="Next", borderwidth=4, relief="ridge",width = 15,cursor="hand2",state="normal",bg="AntiqueWhite3")

        self.give_bt = tk.Button(command=self.controller.water_give,text="Give Water", borderwidth=4, relief="ridge",width = 15,cursor="hand2",bg="AntiqueWhite3")

        self.refill_bt = tk.Button(command=self.controller.refill_vessel,text="Refill", borderwidth=4, relief="ridge",width = 15,cursor="hand2",bg="AntiqueWhite3")

        self.change_vessel = tk.Button(command=self.controller.vessel_change,text="Change Vessel", borderwidth=4, relief="ridge", width=15, cursor="hand2",bg="AntiqueWhite3")

        self.message_l = tk.Label(text="Message",borderwidth=4, relief="groove", width=15,height=2,anchor = "center")

        self.message_l2 = tk.Label(text=message,wraplength=320,borderwidth=4,width=50,height=2, relief="groove",anchor = "center")

        if is_next == False:
            self.next_bt.config(state="disabled")
        if is_start == True:
            self.change_vessel.config(state="disabled")
            self.refill_bt.config(state="disabled")
            self.give_bt.config(state="disabled")
            is_start = False
        if is_error == True:
            self.message_l2.config(fg="red")

        self.textfield_object.grid(row=0, column=0, columnspan=2)

        self.textfield_object_vessel.grid(row=0, column=2, columnspan=2)

        self.textfield_thirst.grid(row=1, column=0)

        self.thirst.grid(row=1, column=1)

        self.textfield_volume.grid(row=1, column=2)

        self.volume.grid(row=1, column=3)

        self.textfield_thirst_max.grid(row=2, column=0)

        self.thirst_max.grid(row=2, column=1)

        self.textfield_volume_max.grid(row=2, column=2)

        self.volume_max.grid(row=2, column=3)

        self.next_bt.grid(row=3, column=0, columnspan=2, rowspan=2)

        self.water_entry.grid(row=3, column=2)

        self.give_bt.grid(row=3, column=3)

        self.refill_bt.grid(row=4, column=3)

        self.change_vessel.grid(row=4, column=2)

        self.message_l.grid(row=5, column=0)

        self.message_l2.grid(row=5, column=1, columnspan=3, pady=5)

        self.mainloop()

