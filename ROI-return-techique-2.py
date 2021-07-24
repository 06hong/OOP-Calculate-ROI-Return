from IPython.display import clear_output

class roi:
    
    def __init__(self):
        pass
        
    
    def income(self):
        
    
            
           
        rentalincome = input("How much is your total rental income?")

        self.rentalincome = int(rentalincome)


        otherincome= input("How much are your other total income?")

        self.otherincome = int(otherincome)
        
        clear_output()
        
        self.totalincome = self.rentalincome + self.otherincome
        
        
    
    def expense(self):
        
        
        totaltax = input("How much is your total tax?")

        self.totaltax = int(totaltax)






        totalinsurance= input("how much is your total insurance?")

        self.totalinsurance = int(totalinsurance)
        
        
    

        totalHOA = input("how much is your total HOA fees?")

        self.totalHOA = int(totalHOA)
        





        totalmortage = input("how much is your total montly mortage?")

        self.totalmortage = int(totalmortage)
        
        
                
              
            
           

        totalotherexpense = input("how much is your total other expenses?") 

        self.totalotherexpense = int(totalotherexpense)
                
              
        
        self.totalexpense = self.totaltax + self.totalinsurance + self.totalHOA + self.totalmortage + self.totalotherexpense
       
        clear_output()
        
        
        
    def cashflow(self):

        self.totalcashflow = self.totalincome - self.totalexpense

        print(f'Your total cash flow is {self.totalcashflow}')
        
        
    def cashoncash(self):
        
        
        
        totaldownpayment = input("How much is your down payment?")

        self.totaldownpayment = int(totaldownpayment)
                
               
        
                
            
        totalclosingcost = input("How much is your closing cost?")

        self.totalclosingcost = int(totalclosingcost)

               
                
            
                
        

        totalothercost = input("How much are you other total costs, such as rehabilitation cost, for example?")

        self.totalothercost = int(totalothercost)
                
             
        
        
        self.totalinvestment = self.totaldownpayment + self.totalclosingcost + self.totalothercost
        
        self.totalroi = (self.totalcashflow*2)/self.totalinvestment
        
        
        
        clear_output()
        
        print(f'Your total ROI is {self.totalroi}%')

        
        
        
                
            
        
        
    

                

                
    
    def not_num(self):
                
                
        print('This is not a number, please type again!')
    
    
   


        
    #to call
    def try_roi(self):
        
        while True:
            
            try:
                self.income()
                
                break
                
                
                
            except:

                self.not_num()
                
                
        while True:
            
            try:
                self.expense()
                
                break
                
                
                
            except:

                self.not_num() 
                

        self.cashflow()  
        
        
        while True:
            
            try:
                self.cashoncash()
                
                break
                
                
                
            except:

                self.not_num() 
                

roi = roi()
roi.try_roi()