class Investment():

    def __init__(self, income, expense, down):
        self.income = income
        self.expense = expense
        self.down = down

    def getincome(self, rental, storage, parking, misc):
        self.rental = rental
        self.storage = storage
        self.parking = parking
        self.misc = misc

        self.income = rental + storage + parking + misc

    def getexpenses(self, tax, ins, utilities, hoa, vacancy, repairs, capEX, manag, morgage):
        self.tax = tax
        self.ins = ins
        self.utilities = utilities
        self.hoa = hoa
        self.vacancy = vacancy
        self.repairs = repairs
        self.capEX = capEX
        self.manag = manag
        self.morgage = morgage
        
        self.expense = tax + ins + utilities + hoa + vacancy + repairs + capEX + manag + morgage
    
    def downpayment(self, downp, closing):
        self.downp = downp
        self.closing = closing

        return self.downp + self.closing

    def cashflow(self):
        return self.income - self.expense

    def return_on(self):
        flow = self.cashflow()
        downtotal = self.downpayment()
        print(f"{((flow / downtotal)*12)*100}%")

    
# class Main:
#     
    # def trigger(self, name):
        # self.name = name
#           
#         while True:

#             w = input("Lets start with some basic Income information. What's the rent on your space? ")
#             x = input("How much does storage cost? ")
#             y = input("How much does parking cost? ")
#             z = input("What is the total misc costs? ")
#             Investment.getincome(self, w, x, y, z)
#             print(Investment.income)
            
#             a = input("Now onto a look at expenses. What is the tax on your space? ")
#             b = input("What is the insurance cost for your space? ")
#             c = input("What is the utility costs for your space? ")
#             d = input("What is the HOA fees for your space? ")
#             e = input("What would you like to put aside for Vacancy? ")
#             f = input("What are you putting aside for repairs? ")
#             g = input("How much capEX are you paying? ")
#             h = input("How much are you paying to have your space managed? ")
#             i = input("What is the morgage on your space? ")
#             Investment.getexpenses(self, a, b, c, d, e, f, g, h, i)
#             print(Investment.expense)

#             alpha = input("Lastly onto downpayment, what did you put down? ")
#             beta = input("And the closing costs? ")
#             Investment.downpayment(self, alpha, beta)
#             print(Investment.down)
#             break




# Main.trigger(my_house)
my_house = Investment(0, 0, 0)
my_house.getincome(2600, 50, 10, 20)
my_house.getexpenses(150, 100, 0, 30, 200, 100, 50, 300, 1400)
my_house.downpayment(40000, 10000)
my_house.return_on()