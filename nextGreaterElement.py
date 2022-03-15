#since this is a circular array, we need to loop through the array twice.
#first we check if the length of stack is more than 0 and stack last element is smaller
# than the current elemet. then we pop stack and put result at that index the 
#current element. otherwise we append the stack
# we are storing the index in the stack.


def nextGreaterElement(array):
	result=[-1]*len(array)
	stack=[]
	
	for idx in range(2*len(array)):
		circularIdx=idx%len(array)
		
		while len(stack) >0 and array[stack[len(stack)-1]]< array[circularIdx]:
			top=stack.pop()
			result[top]=array[circularIdx]
			
		stack.append(circularIdx)
	return result
