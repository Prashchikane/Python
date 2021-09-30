def Display(value):
	iCnt = 0
	for iCnt in range(0,value):
		print("*")

def main():
	print("Enter the number of iterations")
	no = int(input())

	Display(no)

if __name__ == "__main__":
	main()