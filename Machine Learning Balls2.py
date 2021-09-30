from sklearn import tree

def main():
	Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

	Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

	dobj = tree.DecisionTreeClassifier()

	dobj.fit(Features,Labels)

	result = dobj.predict([[40,1]])

	print("Ball is",result)


if __name__ == "__main__":
	main()