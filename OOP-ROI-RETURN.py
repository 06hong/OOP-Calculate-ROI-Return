from IPython.display import clear_output

class roi:
    def __init__(self):
        pass
        
    
    def income(self):
        
        while True:
            
            try:
                rentalincome = input("How much is your total rental income?")

                self.rentalincome = int(rentalincome)
               
                break
                
                
                
            except:

                print('This is not a number, please type again!')
                
                
                
               
        while True: 
            
            try:
                
                otherincome= input("How much are your other total income?")
                
                self.otherincome = int(otherincome)
                
                break
                
                
            
            except:

                print('This is not a number, please type again!')
                
        self.totalincome = self.rentalincome + self.otherincome
        
        
        clear_output()
        
    def expense(self):
        
        while True: 
            
            try:
                totaltax = input("How much is your total tax?")
                
                self.totaltax = int(totaltax)
                
                break
            
            except:

                print('This is not a number, please type again!')
        
        
        while True:
                
            try:
                
                totalinsurance= input("how much is your total insurance?")
                
                self.totalinsurance = int(totalinsurance)
                
                break
                
            except:

                print('This is not a number, please type again!')
                
                
        clear_output()
        
        while True:
                
            try:
                
                totalHOA = input("how much is your total HOA fees?")
                
                self.totalHOA = int(totalHOA)
                
                break
            
            except:

                print('This is not a number, please type again!')
                
                 
                
        while True:
                
            try:      
                
                totalmortage = input("how much is your total montly mortage?")
                
                self.totalmortage = int(totalmortage)
                
                break
                
            except:

                print('This is not a number, please type again!')
                
            
           
        while True:
                
            try:  
                totalotherexpense = input("how much is your total other expenses?") 
                
                self.totalotherexpense = int(totalotherexpense)
                
                break
                
            except:
                
                print('This is not a number, please type again!')
        
        self.totalexpense = self.totaltax + self.totalinsurance + self.totalHOA + self.totalmortage + self.totalotherexpense
        clear_output()
        
    def cashflow(self):

        self.totalcashflow = self.totalincome - self.totalexpense

        print(f'Your total cash flow is {self.totalcashflow}')
        
        clear_output()
    def cashoncash(self):
        
        while True:
            
            try:
        
                totaldownpayment = input("How much is your down payment?")

                self.totaldownpayment = int(totaldownpayment)
                
                break
            
            except:
                
                print('This is not a number, please type again!')
        
                
        while True:
            
            try:      
                totalclosingcost = input("How much is your closing cost?")
                
                self.totalclosingcost = int(totalclosingcost)
                
                break
                
            except:
                
                print('This is not a number, please type again!')
                
        while True:
            
            try:
            
                totalothercost = input("How much are you other total costs, such as rehabilitation cost, for example?")
                
                self.totalothercost = int(totalothercost)
                
                break
            
            except:
                
                print('This is not a number, please type again!')
        
        
        self.totalinvestment = self.totaldownpayment + self.totalclosingcost + self.totalothercost
        
        self.totalroi = (self.totalcashflow*2)/self.totalinvestment
        
        
        
        clear_output()
        
        print(f'Your total ROI is {self.totalroi}%')

        
house=roi()
house.income()
house.expense()
house.cashflow()
house.cashoncash()