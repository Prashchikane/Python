from sklearn import tree

def MarvellousML(weight,surface):
	Features = 
		[[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

	Labels = 
	[1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

	dobj = tree.DecisionTreeClassifier()

	dobj.fit(Features,Labels)

	result = dobj.predict([[weight,surface]])
	if result == 1:
		print("Your object looks like Tennis Ball")
	else:
		print("Your object looks like Cricket Ball")

	print("Ball is",result)

def main():
	print("----Supervised Machine Learning----")
	print("Enter weight of object")
	weight = int(input())
	print("Enter surface type of object")
	surface = int(input())

	if surface.lower() == "rough":
		surface = 1
	elif surface.lower() == "smooth":
		surface = 0
	else:
		print("Invalid input")
		return


if __name__ == "__main__":
	main()