import tkinter

import model
import view
from model import *
from view import View
global receiver_pack
global vessel_pack
global drinker_pack

class Controller:
    def __init__(self):
        self.view = View(self)
    def start(self):
        global pick_c
        pick_c = -1
        global vessel_pack
        Picking.start_params()
        vessel_pack = Picking.pick_container(-1)
        self.view.getvariables_container(vessel_pack)
        self.view.open_main(self)
    def nexto(self):
        global drinker_pack
        drinker_pack = Picking.pick_drinker()
        if drinker_pack != "end":
            self.view.getvariables_drinker(drinker_pack)
            self.view.get_message(Dialogs.get_message(drinker_pack,0))
            self.view.disable_next()
            self.view.open_main(self)
        else:
            self.view.get_error_message("The day is coming to an end and it looks like all customers are happy. Keep it up!.")
            self.view.disable_next()
            self.view.disable_else()
            self.view.open_main(self)
    def refill_vessel(self):
        global vessel_pack
        vessel_pack = model.Volume_change.refilling(vessel_pack)
        self.view.getvariables_container(vessel_pack)
        self.view.open_main(self)

    def water_give(self):
        global vessel_pack
        global drinker_pack
        try:
            drink_volume = int(self.view.water_var.get())
            if drink_volume == "":
                self.view.get_error_message("Please type amount of water you want to give")
                self.view.open_main(self)
                pass
            check_volume = model.Vessel_check.Volume_check(vessel_pack,drink_volume)
            if check_volume == True:
                check_compabillity = model.Vessel_check.is_vessels_compatible(drinker_pack,vessel_pack)
                if check_compabillity == True:
                    drinker_pack = Volume_change.change_volume_drinker(drinker_pack,drink_volume)
                    self.view.getvariables_drinker(drinker_pack[0])
                    vessel_pack = Volume_change.change_volume_vessel(vessel_pack,drinker_pack[1])
                    drinker_pack = drinker_pack[0]
                    self.view.getvariables_container(vessel_pack)

                elif check_compabillity == False:
                    self.view.get_error_message("Human can drink only from bottle, animal can drink only from bowl")
                    self.view.open_main(self)
            elif check_volume == False:
                self.view.get_error_message("Entered value is greater than water volume.")
                self.view.open_main(self)
        except ValueError:
            self.view.get_error_message("You can't water someone with blanc space, letters or fractions")
            self.view.open_main(self)
        is_full = Vessel_check.is_Drinker_full(drinker_pack)
        if is_full == True:
            self.view.get_message(Dialogs.get_message(drinker_pack, 2))
            self.view.disable_next()
            self.view.disable_else()
            self.view.open_main(self)
        else:
            self.view.get_message(Dialogs.get_message(drinker_pack, 1))
            self.view.open_main(self)

    def vessel_change(self):
        global pick_c
        global vessel_pack
        pick_c *=-1
        vessel_pack = Picking.pick_container(pick_c)
        self.view.getvariables_container(vessel_pack)
        self.view.get_message("Vessel changed to: " + str(vessel_pack["name"]))
        self.view.open_main(self)

if __name__ == "__main__":
    controler = Controller()
    controler.start()

