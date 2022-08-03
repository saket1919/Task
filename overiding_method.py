class family:
  
 
    def trd(self):
         print('Welcome to family')
 
class house(family):


    def srd(self):
        print('Welcome to house')
        print('This is inherited from family')
 
emp = family()
print(emp)
emp.trd()
 

dept = house()
print(dept)
dept.srd()