class Pizza:

    def __init__(self):
        self.size = 0
        self.crust = ""
        self.toppings = []

    def add_topping(self, *args):
        self.toppings += args
        # for topping in args:
        #     self.toppings += [topping]

    def pizza_made(self):
        space = " and "
        print(f'I would like a {self.size}-inch, {self.crust} crust pizza with {space.join(self.toppings)}.')

thick_crust_pizza = Pizza()

thick_crust_pizza.size = 16
thick_crust_pizza.crust = "thick"
thick_crust_pizza.add_topping("pineapple")
thick_crust_pizza.add_topping("canadian bacon")

# print(thick_crust_pizza.add_topping("bacon"))


thick_crust_pizza.pizza_made()