#Alice has some cards with 
#numbers written on them.
# She arranges the cards
# in decreasing order, and 
#lays them out face down in 
#a sequence on a table. She 
#challenges Bob to pick out 
#the card containing a given 
#number by turning over as 
#few cards as possible.
# Write a function to help
# Bob locate the card.
# input= numbers in dec order
#problem =having num in dec order we have to 
#find the postion of card wher the min no of cards have to be turned
def locatecard(cards,query):
	#creating a variable postion with value 0
	position=0
	print('cards :',cards)
	print('query :',query)
	#set up loop for repetion
	while (position<len(cards)):
		#check if the element is at currest postion
		if cards[position]==query:
			#answer found 
			
			print("query at:",position)
			return position
		position += 1

		if position==len(cards):
			return -1
	

#creating the list of test cases
"""tests=[]
tests.append(test)

test.append({
		'input':{
			'cards':[13,12,11,7,6,5,2,1,0],
			'query':7
			},
		'output':3
})
#card is at first position
test.append({
		'input':{
			'cards':[7,2,1],
			'query':7
			},
		'output':0
})
#cards does not contain query
test.append({
		'input':{
			'cards':[13,12,11,7,6,5,2,1,],
			'query':15
			},
		'output':-1 
})
#when query occur many time 
test.append({
		'input':{
			'cards':[13,12,7,7,7,7,7,7,7],
			'query':7
			},
		'output':2 # returning first postion 

})"""
cards=[10,7,4,2,1,0]
query=7
locatecard(cards,query)

