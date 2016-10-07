#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  l1.py
#  
#  Copyright 2016 Aditya Gholba <aditya@aditya-ubuntu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os
import math
import random
#GLobal variables
home="~/"
here = os.getcwd()
personalList=["you","your","l"]
mkdirList=['make','new','folder','directory','file','create','dir']
superList=['strength','root','super','superuser','powerful','admin','privelegs','god']
lsList=['files','lists','list','folders','folder','file','files''display','show','contents','look']
findList=['find','search','where','whereis','look']
timeList=['time','clock','date','now',]
eventList=['when','day','date','occur','occured','did','had','has','of','was']
personalQ=["No personal questions please. Ask my creator Aditya.","I dont like talking to strangers, Ask my creator Aditya.","I am not in the mood, Ask my creator Aditya.","Why dont you ask Aditya?"]
fillers=['a','is','in','called','named','desktop','home','downloads','for','the','!','?','.',',','"','of','was','on']
negs=['don\'t','dont','no','not','never','nor','cannot','can\'t']
inputString=[]

class l1:	
	mkdirScore=0
	superScore=0
	lsScore=0
	findScore=0
	timeScore=0
	eventScore=0
	personalScore=0
	inputList=[]
	
	def userInput(self):
		inputString = raw_input("\nWhat can I do for you ?\n")
		print ""
		l1.inputList = inputString.split();
		for i in range(len(l1.inputList)):
			if l1.inputList[i].lower() in negs:
				print "DON'T ENTER NEGATIVE STATEMENT\n"
				l1.userInput(self);
				
	def userIntent(self):
		l1.mkdirScore=0
		l1.superScore=0
		l1.lsScore=0
		l1.findScore=0
		l1.timeScore=0
		l1.eventScore=0
		l1.personalScore=0
		
		for i in range(len(mkdirList)):
			for j in range(len(l1.inputList)):
				if l1.inputList[j].lower() == mkdirList[i].lower():
					l1.mkdirScore=l1.mkdirScore+1
					
		for i in range(len(superList)):
			for j in range(len(l1.inputList)):
				if l1.inputList[j].lower() == superList[i].lower():
					l1.superScore=l1.superScore+1
					
		for i in range(len(lsList)):
			for j in range(len(l1.inputList)):
				if l1.inputList[j].lower() == lsList[i].lower():
					l1.lsScore=l1.lsScore+1
					
		for i in range(len(findList)):
			for j in range(len(l1.inputList)):
				if l1.inputList[j].lower() == findList[i].lower():
					l1.findScore=l1.findScore+1
					
		for i in range(len(timeList)):
			for j in range(len(l1.inputList)):
				if l1.inputList[j].lower() == timeList[i].lower():
					l1.timeScore=l1.timeScore+1
					
		for i in range(len(eventList)):
			for j in range(len(l1.inputList)):
				if l1.inputList[j].lower() == eventList[i].lower():
					l1.eventScore=l1.eventScore+1
					
		for i in range(len(personalList)):
			for j in range(len(l1.inputList)):
				if l1.inputList[j].lower() == personalList[i].lower():
					l1.personalScore=l1.personalScore+1
					
	def mkdirFunc(self):
		for i in range(len(l1.inputList)):
			if "/" in l1.inputList[i]:
				direc=l1.inputList[i]
				break;
			elif "desktop" in l1.inputList[i].lower():
				direc="~/Desktop"
				break;
			elif "home" in l1.inputList[i].lower():
				direc="~/"
				break;
			elif "downloads" in l1.inputList[i].lower():
				direc="~/Downloads"
				break;
			else:
				direc=os.getcwd()

		for i in range(len(l1.inputList)):
				if l1.inputList[i].lower() not in fillers and  l1.inputList[i].lower() not in mkdirList and "/" not in l1.inputList[i] and l1.inputList[i].lower() not in findList and l1.inputList[i].lower() not in lsList and l1.inputList[i].lower() not in superList:
					fileName=l1.inputList[i]
					break;
				else:
					fileName="Untitled"
		
		mkState="mkdir %s/%s" % (direc,fileName)
		if l1.mkdirScore >=2:		
			os.system(mkState)
			print "Created a new folder called "+fileName+" in "+direc+"\n"
		else:
			answer= raw_input("Do you want to make a new folder "+fileName+" in "+direc+" ?\n");
			if answer.lower() == "yes" :
				os.system(mkState)
				print "Created a new folder called "+fileName+" in "+direc+"\n"
			else:
				l1.userInput(self);
				l1m.userIntent(self);
				
	def superFunc(self):
		if l1.superScore >=2:
			print "Enter root password\n"
			os.system("sudo -i")
		else:
			answer= raw_input("Do you want to gain root privileges?");
			if answer.lower() == "yes" :
				print "Enter root password\n"
				os.system("sudo -i")
			else:
				l1.userInput(self);
				l1.userIntent(self);
		
	def lsFunc(self):
		for i in range(len(l1.inputList)):
			if "/" in l1.inputList[i]:
				direc=l1.inputList[i]
				break;
			elif "desktop" in l1.inputList[i].lower():
				direc="~/Desktop"
				break;
			elif "home" in l1.inputList[i].lower():
				direc="~/"
				break;
			elif "downloads" in l1.inputList[i].lower():
				direc="~/Downloads"
				break;
			else:
				direc=os.getcwd()
		
		lsState="ls %s" % (direc)
		if l1.lsScore >=2:		
			print "List of files in "+direc+"\n"
			os.system(lsState)
		else:
			answer= raw_input("Do you want to look in " +direc+" ?\n");
			if answer.lower() == "yes" :
				print "List of files in "+direc+"\n"
				os.system(lsState)
			else:
				l1.userInput(self);
				l1.userIntent(self);
				
	def findFunc(self):
		for i in range(len(l1.inputList)):
			if "/" in l1.inputList[i]:
				direc=l1.inputList[i]
				break;
			elif "desktop" in l1.inputList[i].lower():
				direc="~/Desktop"
				break;
			elif "home" in l1.inputList[i].lower():
				direc="~/"
				break;
			elif "downloads" in l1.inputList[i].lower():
				direc="~/Downloads"
				break;
			else:
				direc="~/"
		
		for i in range(len(l1.inputList)):
				if l1.inputList[i].lower() not in fillers and  l1.inputList[i].lower() not in mkdirList and "/" not in l1.inputList[i] and l1.inputList[i].lower() not in findList and l1.inputList[i].lower() not in lsList and l1.inputList[i].lower() not in superList:
					fileName=l1.inputList[i]
					break;
				else:
					fileName="Untitled"
					
		findState='find netcdf 2>/dev/null %s -iname "%s*"' % (direc,fileName)
		if l1.findScore >=2:		
			print "File "+fileName+" might be in ..."
			os.system(findState)
		else:
			answer= raw_input("Do you want to Search in " +direc+" for file "+fileName+" ?\n");
			if answer.lower() == "yes" :
				print "File "+fileName+" might be in ..."
				os.system(findState)
			else:
				l1.userInput(self);
				l1.userIntent(self);
				
	def timeFunc(self):
		if l1.timeScore >=2:
			print "Current time and date is \n"
			os.system("date")
		else:
			answer= raw_input("Do you want to know the date or time?");
			if answer.lower() == "yes" :
				print "Current time and date is \n"
				os.system("date")
			else:
				l1.userInput(self);
				l1.userIntent(self);
		
	def eventFunc(self):
		eString=""
		n=0
		eDate=0
		apx=0
		final=0
		eventFile = open("calendar.txt","r+")
		eventString = eventFile.read()
		eventList1= eventString.split('\n')
		
		for i in range(len(l1.inputList)):
			if l1.inputList[i] not in fillers and l1.inputList[i] not in eventList:
				eString = eString+" "+l1.inputList[i]
		
		eStringList = eString.split()
	
		for i in range(len(eStringList)):
			for j in range(len(eventList1)):
				if eStringList[i].lower() in eventList1[j].lower():
					if i<((len(eStringList))-1):
						for x in range(i+1,len(eStringList)):
							if eStringList[x].lower() in eventList1[j].lower():
								final=j
								break;
							elif final==0:
								apx=1
					else:
						apx=1
						
		if final>0:
			print "Your answer is ..."
			print eventList1[final]
		elif apx==1:
			print "This is all the data I could find"
			for i in range(len(eStringList)):
				for j in range(len(eventList1)):
					if eStringList[i].lower() in eventList1[j].lower():
						print eventList1[j]
			
	def personalFunc(self):
		x1 = int(random.random() * len(personalQ))
		print personalQ[x1]
	def teachFunc(self):
		print "To do"
							
	def callFunc(self):
		if l1.personalScore>0 and l1.superScore==0 and l1.mkdirScore==0 and l1.lsScore==0 and l1.findScore==0 and l1.timeScore==0 and l1.eventScore==0:
			l1.personalFunc(self)
			
		if l1.personalScore==0 and l1.superScore==0 and l1.mkdirScore==0 and l1.lsScore==0 and l1.findScore==0 and l1.timeScore==0 and l1.eventScore==0:
			print "Intention Score"
			print "super %d   mkdir %d   ls %d  find %d  time %d  event %d  personal %d" % (l1.superScore,l1.mkdirScore,l1.lsScore,l1.findScore,l1.timeScore,l1.eventScore,l1.personalScore)
			reply=raw_input("I didn't get that, if you are willing to teach I am willing to learn. Yes or No?\n")
			if reply.lower()=="yes" or reply.lower()=="y":
				l1.teachFunc(self)
			
				
		print "Intention Score"
		print "super %d   mkdir %d   ls %d  find %d  time %d  event %d  personal %d" % (l1.superScore,l1.mkdirScore,l1.lsScore,l1.findScore,l1.timeScore,l1.eventScore,l1.personalScore)
		if l1.superScore > l1.mkdirScore and l1.superScore > l1.lsScore and l1.superScore > l1.findScore and l1.superScore > l1.timeScore and l1.superScore > l1.eventScore:
				l1.superFunc(self)
			
		if l1.mkdirScore > l1.superScore and l1.mkdirScore > l1.lsScore and l1.mkdirScore > l1.findScore and l1.mkdirScore > l1.timeScore and l1.mkdirScore > l1.eventScore:
				l1.mkdirFunc(self)
						
		if l1.lsScore > l1.superScore and l1.lsScore > l1.mkdirScore and l1.lsScore > l1.findScore and  l1.lsScore > l1.timeScore and l1.lsScore > l1.eventScore:
				l1.lsFunc(self)
				
		if l1.findScore > l1.superScore and l1.findScore > l1.mkdirScore and l1.findScore > l1.lsScore and l1.findScore > l1.timeScore and l1.findScore > l1.eventScore:
				l1.findFunc(self)
				
		if l1.timeScore > l1.superScore and l1.timeScore > l1.mkdirScore and l1.timeScore > l1.lsScore and l1.timeScore > l1.findScore and l1.timeScore > l1.eventScore:
				l1.timeFunc(self)
		
		if l1.eventScore > l1.superScore and l1.eventScore > l1.mkdirScore and l1.eventScore > l1.lsScore and l1.eventScore > l1.findScore and l1.eventScore > l1.timeScore:
				l1.eventFunc(self)
		
				
t=l1()
#I am pretty smart for a single night of code.
print "Hello my name is L\n\nI can do tasks like make a folder,tell you the time,show files,find files,search events etc"
while 1:
	t.userInput();	
	t.userIntent();
	t.callFunc();

