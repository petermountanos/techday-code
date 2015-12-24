import csv, random
import matplotlib.pyplot as plt
import numpy as np

#-----Global Variables------#
responders = []
finalResponders = []
#---------------------------#

def main(csvFile):
	# properly format response data from csv file
	contestants = createResponseList(csvFile)
	# generate pseudo-random winning number for raffle
	winningNumber = random.randint(0, len(contestants)-1)
	# show histogram plot of question number
	try:
		dataAnalytics(contestants,4)
	except:
		print 'uh'
	# print winner's name to collect prize
	print "The winner is: "+contestants[winningNumber][0]

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
		# append each record (not separated yet) to a responders list

	# for each record in responders list...
	for i in responders:
		recordInfo = i.split(',')	# split record by commas (CSV file)
		tempList = [] # create a temporary list
		for x in recordInfo: # for each value in row...
			tempList.append(x) # append it to a temporary list
		finalResponders.append(tempList) # append temporary list to the responders list of lists
	return finalResponders # 2-dimensional list of responder information

def dataAnalytics(someList,questNum):
	# initialize data list
	rollingData = []
	# for each response...
	for responder in someList:
		# add the value of their response to question <questNum> to list
		rollingData.append(int(responder[questNum]))
	# testing purposes
	#uh = np.random.random_integers(1,10,1000) # create 1000 item list of random numbers range (1,10)
	plt.hist(rollingData) # plot data in histogram
	plt.title("Instructor Ratings") # graph title
	plt.xlabel("Value") # x-axis label
	plt.ylabel("Frequency") # y-axis label
	plt.xlim(1,10) # x-axis range
	plt.ylim(0,40)
	plt.show() # show graph

# application code
if __name__ == '__main__':
	main('test2.csv')
