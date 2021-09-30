def Add(No1,No2):
	add = No1+No2
	return add

def Sub(No1,No2):
	sub = No1-No2
	return sub

def Div(No1,No2):
	div = No1/No2
	return div

def Mul(No1,No2):
	mul = No1*No2
	return mul

def main():

	value1 = int(input("Enter First Number"))
	value2 = int(input("Enter Second Number"))
	
	ret1 = Add(value1,value2)
	print("Addition is :",ret1)

	ret2 = Sub(value1,value2)
	print("Substraction is : ",ret2)
	
	ret3 = Div(value1,value2)
	print("division is : ",ret3)
	
	ret4 = Mul(value1,value2)
	print("multiplication is : ",ret4)

if __name__ == "__main__":
	main()