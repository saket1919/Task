
class animal():
	
	
	def __init__(self):
		self.value = "Deficiencies in animal"
		
	
	def show(self):
		print(self.value)
		

class dog(animal):
	

	def __init__(self):
		self.value = "Deficiencies in dog"
		

	def show(self):
		print(self.value)
		
		

obj1 = animal()
obj2 = dog()

obj1.show()
obj2.show()
