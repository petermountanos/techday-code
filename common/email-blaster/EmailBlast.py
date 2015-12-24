# EmailBlast.py
# Purpose       : Wantagh TechDay 2015
# Created by    : Peter Mountanos
# Date Created  : 11/21/14
# Last Modified : 11/21/14

#-----IMPORT MODULES-----#
import smtplib, csv, sys, getpass, csv
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
#------------------------#

#----CLASS DEFINITION----#
class EmailBlast():
	"""
	Simple class to send an email message, with or without an attachment,
	to a list of users given in a csv file. This class utilizes the smtplib
	and email modules to connect to gmail and send the personalized emails.
	"""

	def __init__(self, email, password, subject, toFile, messageFile, attachment=None):
		"""
		Default constructor which instantiates an EmailBlast object, and 
		automatically calls all of the helper methods to create the recipients
		list, and send the emails out. No further method calls are needed after
		the instantiatation.

			:param email       : string holding the email address to send the 
							     email from
			:param password    : string holding the password to the email 
			 					 account
			:param subject     : subject of the email message stored in email
			   					 header
			:param toFile      : path to csv file containing list of users in 
								 form <firstname,lastname,email>
			:param messageFile : path to text file storing the message to be
								 sent out
			:param attachment  : path to pdf file to be attached; default is 
								 there is no attachment

		If the program cannot parse the input files, it exits the program. If 
		it has trouble sending a message to a specifc user, it skips that user
		(but prints the error to output) and then continues to the next user.
		"""

		self.email       = email
		self.password    = password
		self.subject     = subject
		self.toFile      = toFile
		self.messageFile = messageFile
		self.attachment  = attachment
		self.recipients  = []
		self.server      = None
		
		# try to read file containing recipients, if runs into error, quits
		try:			
			self.getRecipients()
		except:
			print "Could not generate a list of recipients from file: \"%s\"" \
				  % self.toFile
			sys.exit(1)
		
		# try to read file containing message, if runs into error, quits
		try:
			self.getMessage()
		except:
			print "Could not generate a message from file: \"%s\"" \
				  % self.messageFile
			sys.exit(1)

		self.sendMessage() # helper method to send out personalized emails
		
	def getMessage(self):
		"""
		Method to read the email message from the inputted text file, and store
		it in the message data field.
		"""	

		with open(self.messageFile, 'r') as src_file:
			self.message = src_file.read()


	def getRecipients(self):
		"""
		Method to read the recipients list from the csv file, and split the
		comma-separated values by delimiter and store them in an array. This
		array is then appended onto the recipients data field, which is a
		multi-dimensional array, that contains information on each user.
		"""

		with open(self.toFile, 'rU') as src_file:
			# generate csv reader object from inputted file
			csvReader = csv.reader(src_file, dialect=csv.excel_tab)

			for row in csvReader:
				# split on commas, and append to instance variable
				self.recipients.append(row[0].split(","))

	def sendMessage(self):
		"""
		Method which sends a personalized email to each user in the recipients
		list. If the message cannot be sent to a specific user, it prints an
		error message, and moves onto the next user. In the beginning of this 
		method, it connects to the server only once, and then sends multiple
		messages under that connection. This method expects that the recipients
		array has rows that are in the form: [first name, last name, email].

		When the emailing is complete, it generates an output message notifying
		the user how many emails were sent successfully. It also prints a
		message after each successful email sent.
		"""

		# instantiate connection to gmail server
		self.instantiateServer()

		counter = 0
		# for each user, send an email...
		for user in self.recipients:
			try:
				firstName = user[0]
				lastName  = user[1]
				emailTo   = user[2]
				
				#----INSTANTIATE MESSAGE OBJECT---#
				msg             = MIMEMultipart() 
				msg['Subject']  = self.subject
				msg['From']     = self.email
				msg['Reply-to'] = self.email
				msg['To']       = emailTo 
				part       		= MIMEText(self.message % firstName)
				msg.attach(part)

				# if an EmailBlast object contains a file path to an attachment
				# attach that file to the email
				if self.attachment:
					try:
						part = MIMEApplication(open(self.attachment,"rb").read(),
											   "pdf", name=self.attachment)
						part.add_header('Content-Disposition', 'attachment',
									    filename=self.attachment)
						msg.attach(part)
		 			except:
		 				print "Could not attach: \"%s\"" % self.attachment
				
				
		 		# send the email via server connection
				self.server.sendmail(msg['From'], msg['To'], msg.as_string())

				# output message on successful email sent
				print "Email sent to %s %s: %s" % (firstName, lastName, emailTo) 
				counter += 1 
			except Exception:
				# notify user if an email could not be sent
				print "Error: email not sent to %s %s: %s" \
					  % (firstName, lastName, emailTo) 
				continue # go to next user
		
		# report number of successful emails sent
		print "Successfully send to %s/%s email(s)!" % (str(counter),
		 											 str(len(self.recipients))) 

	def instantiateServer(self):
		"""
		Method to connect to the gmail server under port 587, using the smtplib
		module. The SMTP connect is in TLS (Transport Layer Security) mode, 
		which means all of the commands are encrypted. It logs in based on the
		email and password instance variables set in the constructor. The server
		object is stored as an instance variable as well.
		"""
		
		self.server = smtplib.SMTP("smtp.gmail.com:587")
		self.server.ehlo() # identify to an ESMTP server using EHLO
		self.server.starttls() # put connection in TLS mode. 
		self.server.login(self.email, self.password) 

#-------------------#

#----MAIN METHOD----#
def main():
	"""
	Main method which instantiates an EmailBlast object, which send outs
	personalized emails based on the toFile (email list) and messageFile
	(which contains the message) from the account given by the email and 
	password. 
	"""
	email       = ""
	password    = ""
	subject     = ""
	toFile      = "test.csv"
	messageFile = "test_message.txt"
	attachment  = "Flyer_v2.pdf"
	blast       = EmailBlast(email, password, subject, toFile,
							 messageFile, attachment)
#---------------------#

#---APPLICATION CODE--#
if __name__ == '__main__':
	main()