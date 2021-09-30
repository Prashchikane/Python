# Accept N numbers from user and filter out only even numbers from that numbers after that add 2 in every even number after the 
# addition of 2 perform summation of that modified number.

# Input[1,3,2,4,6,5,4]  ->	pudchya step la even ghenar fkt
# After filter[2,4,6,4] ->	pudchya step la even + 2 karnar
# After map[4,6,8,6]    ->	pudchya step la saglya number chi addition karnar
# After reduced 24		->  final output yenar

import functools

CheckEven = lambda no: (no >= 70 and no <= 90)
	
Increment = lambda no: no + 10

Add = lambda no1,no2: no1 * no2

def main():
	arr = []
	print("Enter number of elements")
	size = int(input())

	for i in range(size):
		print("Enter element number:",i+1)
		no = int(input())
		arr.append(no)

	print("Your entered data is",arr)
	#newdata = filter(function_name, Data)
	newdata = list(filter(CheckEven,arr))				#newdata = MarvellousFilter(arr)
	print("After filtering data is",newdata)

	newdata1 = list(map(Increment, newdata))	#newdata1 = MarvellousMap(newdata)
	print("After map data is",newdata1)

	output = functools.reduce(Add,newdata1)				#output = MarvellousReduce(newdata1)
	print("After reduced data is",output) 

if __name__ == "__main__":
	main() 