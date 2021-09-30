
import MarvellousNumbers as MN
# import MarvellousNumbers
# from MarvellousNumbers import ChkEven
# from MarvellousNumbers import

def main():
	print("Enter one number")
	value = int(input())

	bret = MN.ChkEven(value)

	if bret == True:
		print("{} is Even number".format(value))
	else:
		print("{} is Odd number".format(value))

if __name__ == "__main__":
	main()