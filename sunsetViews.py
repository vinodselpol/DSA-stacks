# Create an empty stack (array) iterate from left if direction is west else from reverse
#create one standrd varibale to compare the height to currenr building
#if current building height > variable then append that index to stack


def sunsetViews(buildings, direction):
    stack=[]
	idx =0 if direction=="WEST" else len(buildings)-1
	step=1 if direction =="WEST" else -1
	buildingRunningHeight=0
	while idx >=0 and idx <len(buildings):
		buildingHeight=buildings[idx]
		
		if buildingHeight > buildingRunningHeight:
			stack.append(idx)
		buildingRunningHeight=max(buildingHeight, buildingRunningHeight)
		idx+=step
	if direction=="EAST":
		return stack[::-1]
	return stack
