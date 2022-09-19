from abc import ABC, abstractmethod

# import PIL
"""
name - name of object
volume - starting volume for Vessel
max_volume - maximal volume of Vessel
Type - Vessel Type ("R" for Receiver, "C" for Container")
Receiver can olny accept water
Container can give off water or fill up to the maximum volume
species: H is for human(uses bottle), A is for animal(uses bowl)

"""

@abstractmethod
class Vessel():
    def __init__(self,name,volume,max_volume,typ,species = ""):
        self.__name = name
        self.__volume = volume
        self.__max_volume = max_volume
        if typ == "C" or typ == "R":
            self.__type = typ
        else:
            raise TypeError("wrong typ input for object (\"R\" or \"C\" is expected)")

        if species == "A" or species == "H" or species == "":
            self.__species = species
        else:
            raise TypeError("wrong species input for object (\"A\" or \"H\" or\"\" is expected")
    def __del__(self):
        print ("object", self.__name , "deleted")
    def refill(self):
        if self.__type == "C":
            self.__volume = self.__max_volume
        else:
            pass
    @property
    def get_all(self):
        return {"name":self.__name, "Volume":self.__volume, "Max Volume": self.__max_volume,"Species":self.__species,"Type:":self.__type}
    @property
    def drink(self):
        return self.__volume
    @drink.setter
    def drink(self,value):
        if self.__type == "R":
            if self.__max_volume >= self.__volume + value:
                self.__volume += value
            else:
                self.__volume = self.__max_volume
        if self.__type == "C":
            if self.__volume - value >= 0:
                self.__volume-=value
            else:
                self.__volume = 0
    @classmethod
    def unpack_dict(cls, dict):
        name = dict["name"]
        volume = dict["Volume"]
        max_volume = dict["Max Volume"]
        species = dict["Species"]
        typ = dict["Type:"]
        return cls(name, volume, max_volume, typ, species)

class Picking(Vessel):
    @staticmethod
    def start_params():
        global pick_d
        pick_d = 0
        global pick_c
        pick_c = 1

    @staticmethod
    def pick_drinker():
        global pick_d
        global cat
        global dog
        global human

        if pick_d == 0:
            cat = Picking("Cat",0,250,"R","A")
            pick_d +=1
            return cat.get_all
        elif pick_d == 1:
            dog = Picking("Dog",0,300,"R","A")
            pick_d +=1
            return  dog.get_all
        elif pick_d == 2:
            human = Picking("Vagabond",0,800,"R","H")
            pick_d += 1
            return human.get_all
        elif pick_d > 2:
            return "end"
    @staticmethod
    def pick_container(f1):
        global bowl
        global bottle

        if f1 == 1:
            bowl = Picking("Bowl", 200, 200,"C","")
            return bowl.get_all
        elif f1 == -1:
            bottle = Picking("Bottle",700,700,"C","")
            return bottle.get_all

class Volume_change(Vessel):
    @staticmethod
    def refilling(x):
        obj = Vessel.unpack_dict(x)
        obj.refill()
        return obj.get_all
    @staticmethod
    def change_volume_drinker(vessel,drink_volume):
        volume_before = vessel["Volume"]
        obj = Vessel.unpack_dict(vessel)
        obj.drink = drink_volume
        volume_after = obj.get_all["Volume"]
        return [obj.get_all,volume_after-volume_before]
    @staticmethod
    def change_volume_vessel(vessel,drink_volume):
        obj = Vessel.unpack_dict(vessel)
        obj.drink = drink_volume
        return obj.get_all

class Vessel_check(Vessel):
    @staticmethod
    def Volume_check(dict,value):
        max_volume = dict["Max Volume"]
        volume = dict["Volume"]
        if max_volume >= value and volume-value>=0:
            return True
        else:
            return False
    @staticmethod
    def is_vessels_compatible(drinker,vessel):
        drink_species = drinker["Species"]
        vessel_name = vessel["name"]
        if drink_species == "H" and vessel_name == "Bottle":
            return True
        elif drink_species == "A" and vessel_name == "Bowl":
            return True
        else:
            return False
    @staticmethod
    def is_Drinker_full(dict):
        max_volume = dict["Max Volume"]
        volume = dict["Volume"]
        if max_volume == volume:
            return True
        else:
            return False

class Dialogs():
    @staticmethod
    def get_message(dict,x):
        return Dialogs.messages((dict["name"]),x)
    @staticmethod
    def messages(msg,x):
        Cat = ["An old tomcat jumped over your fence and began to meow at you.",
         "The cat looked contemptuously at the quality of the bowl's materials, but began to drink from it."
            , "The cat purred to you and went its way."]
        Dog = ["The puppy appeared nearby. It is very hot today, maybe he is thirsty?", "Doggo happily start drinking water waving his tail","Happy puppy ran to play with other dogs"]
        Vagabond = ["A strange man came up to you. He looks thirsty.", "The man smiled broadly and began to drink",
         "The man shouted ahoy! and went his way."]
        if msg == "Cat":
            return Cat[x]
        elif msg == "Dog":
            return  Dog[x]
        elif msg == "Vagabond":
            return Vagabond[x]
