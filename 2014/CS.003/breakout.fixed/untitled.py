import csv
import random
#-----Global Variables------#
responders = []
finalResponders = []
#---------------------------#
def main(csvFile):
	contestants = createResponseList(csvFile)
	winningNumber = random.randint(0, len(contestants))

	print "The winner is: "+contestants[winningNumber][1]

def createResponseList(csvFile):
	"""Helper function for main method for module emailReminder.py

		:param csvFile: CSV file that contains registration information

		**Precondition**: CSV file where each record must contain, in this order:
		first name, last name, email, course enrolled, room number, instructor last name
		name

	**Returns**: 2-dimensional list where each index in the list is a list
	containing information for each registrant
	"""
	# open file using csv reader method
	sourceFile = csv.reader(open(csvFile, "rU"), dialect=csv.excel_tab)
	
	# for each row in the source file...
	for row in sourceFile:
		responders.append(row[0])
		# append each record (not separated yet) to a recipients list

	# for each record in recipients list...
	for i in responders:
		recordInfo = i.split(',')	# split record by commas (CSV file)
		tempList = [] # create a temporary list
		for x in recordInfo: # for each value in row...
			tempList.append(x) # append it to a temporary list
		finalResponders.append(tempList) # append temporary list to the registrants list of lists
	return finalResponders # 2-dimensional list of registrant information


if __name__ == '__main__':
	main('test.csv')