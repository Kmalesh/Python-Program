class Bike:
    def __init__(self):

        key_on=False
        clutch=False
        gair=False
        axceletor=False

    
    def start(self):
        self.key_on=True
        self.clutch=True
        self.gair=True
        self.axceletor=True
        print("Bike Start...")


key1=Bike()      
key1.start()
