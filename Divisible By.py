def ChkNum(No):
	if No % 5 == 0:
		return True
	else:
		return False

def main():
	print("Enter one number")
	value = int(input())
	bret = ChkNum(value)

	if bret == True:
		print("{} is Divisible by 5".format(value))
	else:
		print("{} is Not Divisible by 5".format(value))

if __name__ == "__main__":
	main()