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

three_hundred_one_plus_park = Building("301 Plus Park", 3)
three_hundred_one_plus_park.purchase("Jeff Besos")
three_hundred_one_plus_park.construct()
three_hundred_one_plus_park.building_info()

batman_building = Building("AT&T Building Downtown Nashville", 219)
batman_building.purchase("Mark Cuban")
batman_building.construct()
batman_building.building_info()

ninety_six_10_mercedes_drive = Building("9610 Mercedes Drive", 2)
ninety_six_10_mercedes_drive.purchase("Parks")
ninety_six_10_mercedes_drive.construct()
ninety_six_10_mercedes_drive.building_info()

sears_tower = Building("Sears Tower", 10000)
sears_tower.purchase("NSS")
sears_tower.construct()
sears_tower.building_info()


