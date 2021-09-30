def Addition(LIST):					
	sum = 0
	for i in range(len(LIST)):
		sum = sum + LIST[i]
	return sum

def main():
	arr = []
	print("Enter the number of elements")
	size = int(input())

	print("Enter the elements")
	for i in range(size):
		arr.append(int(input()))

	print("Addition of all elements is :",Addition(arr))

if __name__ == "__main__":
	main()