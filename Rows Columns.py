
def Display(iRow,iCol):
	for i in range(1, iRow):
		for j in range(1, icol):
			print("*")
		print("")

def main():
	value1 = int(input("Enter Number of rows "))
	value2 = int(input("Enter Number of cols"))
	Display(value1,value2)
	
if __name__ == "__main__":
	main()