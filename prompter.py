#! /usr/bin/env python

def prompt():
	"""Prompts user for information until sentinal ('exit') is given.
	   Returns a list of the responses"""
	count = 1
	newResponse = ""
	promptList = []

	print "Enter words into the list. Type 'exit' to end the program and return the list."

	while True:
		prompter = "%d. " % count
		newResponse = raw_input(prompter)
		if newResponse == 'exit':
			break
		promptList.append( newResponse )
		count+=1
	
	return promptList

if __name__ == '__main__':
	print prompt()
