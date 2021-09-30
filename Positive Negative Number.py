def ChkNum(No):
	if No == 0:
		print("Number is zero")
	elif No < 0:
		print("Number is negative")
	else:
		print("Number is positive")

def main():
	print("Enter one number")
	value = int(input())
	ChkNum(value)
	
if __name__ == "__main__":
	main()