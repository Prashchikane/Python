def Maximum(LIST):					
	iCnt = 0
	iMax = arr[0]
	for i in range(len(LIST)):
		if arr[iCnt] > iMax:
			iMax = arr[iCnt]
	return iMax

def main():
	arr = []
	print("Enter the number of elements")
	size = int(input())

	print("Enter the elements")
	for i in range(size):
		arr.append(int(input()))

	print("Addition of all elements is :",Maximum(arr))

if __name__ == "__main__":
	main()