def Menu():
	print('Welcome to UMSL Bookstore')
	print('**************************')
	print('')
	print('1. Select all books') 
	print('2. Select all books sort by column') 
	print('3. Search books') 
	print('4. Add a New Book') 
	print('5. Update quantity on hand') 
	print('6. Delete a book') 
	print ('7. Exit')
	print('')
	menuChoice = int(input('Please select from the menu above: '))
	return menuChoice