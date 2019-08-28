import datetime

class Building:

    def __init__(self, address, stories):
        self.designer = "Ben Parker"
        self.date_constructed = 0
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, owner):
        self.owner = owner

    def building_info(self):
        print(f'{self.address} was purchased by {self.owner} on {(self.date_constructed).strftime("%x")} and has {self.stories} stories.')

eight_hundred_eighth = Building("800 8th Street", 12)
eight_hundred_eighth.purchase("Richard LeFrak")
eight_hundred_eighth.construct()
eight_hundred_eighth.building_info()