def Add(No1,No2):
	ret = No1 + No2
	return ret

def main():
	value1 = int(input("Enter First Number"))
	value2 = int(input("Enter Second Number"))
	ans = Add(value1,value2)
	print("Addition is :",ans)

if __name__ == "__main__":
	main()
