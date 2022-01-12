class Hotel: #create a class name Hotel

    def getData(self): # it is the construtor of main class
        print("Fetching Hotel details")
        self.name=input("Hotel Name : ")
        self.service=input("Category(Family or Single) : ")

class Customer(Hotel): #another class insert main class

    def getData(self):
        super().getData() #to fetch Hotel details
        self._customer_name=input("Customer Name : ") #protected
        self.__age=input("age : ") #private


class Bill(Customer):

    def calculateBill(self):#create function and call customer data
        super().getData()
        flag=int(input("1.One Day 2.Full Day "))

        if(flag==1):
            print("Bill Generated for ",self.name)
            print("Customer name ",self._customer_name) #protected variable accessible
            #print("Age ",self.__age) private variable is not accessible
            print("Stay at Full Day Rs. 2000 , suggested by Hotel Manager")
        elif(flag==2):
            print("Stay at One Day Rs. 1000 , suggested by Hotel Manager")
        else:
            print("Wrong choice or No fees")

obj=Bill()
obj.calculateBill()
