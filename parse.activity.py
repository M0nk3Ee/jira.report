#!/usr/bin/python

from xml.dom.minidom import parse, parseString
from datetime import date, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import collections, smtplib, sys


#create report for the past XX days
number_of_days_to_report = 4 

#Class used to hold information for each ticket
class item(object):
   def __init__(self, ticketno, desc, date):
    self.ticketno = ticketno
    self.desc = desc
    self.date = date
    
#dict used to store all jira tickets
tickets_dict = collections.defaultdict(list)


# READ XML into 3 lists.
#doc = parse('my.activity.xml')
doc = parse(str(sys.argv[1]))
item_ticketnums = doc.getElementsByTagName('key')
item_summaries = doc.getElementsByTagName('summary')
item_dates = doc.getElementsByTagName('updated')


#read all tickets from parse XML into dict["date_as_string"][list_of_item_objects]

x=0
for i in item_dates:
    dict_key = item_dates[x].firstChild.nodeValue.split()[1] + " " + item_dates[x].firstChild.nodeValue.split()[2] 
    a = item(item_ticketnums[x].firstChild.nodeValue, item_summaries[x].firstChild.nodeValue, item_dates[x].firstChild.nodeValue)
    tickets_dict[dict_key].append(a)
    x=x+1

# PRINT SUMMARY 
print " "
print "Ticket Summary"
print "Total number of tickets parsed from XML : " + str(len(item_ticketnums))

#USED for debugging
#print "ticket_dict keys : "
#for key in tickets_dict.keys():
#   print key 

days_ago = number_of_days_to_report 
while True:
 date_to_find_as_str=(date.today()-timedelta(days=days_ago)).ctime()
 #print date_to_find_as_str
 date_to_find_month_as_str=date_to_find_as_str.split()[1]
 date_to_find_day_as_str=date_to_find_as_str.split()[2]
 dict_key = date_to_find_day_as_str + " " + date_to_find_month_as_str
 print dict_key + " : " + str(len(tickets_dict[dict_key])) 
 if days_ago == 0: #we have now reached todays date - end
     break
 days_ago = days_ago - 1 #decrement
 

# PRINT INDIVIDUAL TICKETS

days_ago = number_of_days_to_report 
print " "
while True:
 date_to_find_as_str=(date.today()-timedelta(days=days_ago)).ctime()
 print date_to_find_as_str
 date_to_find_month_as_str=date_to_find_as_str.split()[1]
 date_to_find_day_as_str=date_to_find_as_str.split()[2]
 dict_key = date_to_find_day_as_str + " " + date_to_find_month_as_str

 i=0
 print dict_key + " :"
 while i < len(tickets_dict[dict_key]):
    print "  " + tickets_dict[dict_key][i].ticketno + "   " + tickets_dict[dict_key][i].date
    print "     " + tickets_dict[dict_key][i].desc
    i=i+1

 if days_ago == 0: #we have now reached todays date - end
     break
 days_ago = days_ago - 1 #decrement

print " "
print " "
print "-------------------------"
print "FORMAT FOR EMAIL BELOW"
print " "
# PRINT INDIVIDUAL TICKETS
print "FM OTG Networks Weekly Report"
days_ago = number_of_days_to_report
print " "
print "Date         Ticket Numbers"    
while True:
 date_to_find_as_str=(date.today()-timedelta(days=days_ago)).ctime()
 #print date_to_find_as_str
 date_to_find_month_as_str=date_to_find_as_str.split()[1]
 date_to_find_day_as_str=date_to_find_as_str.split()[2]
 dict_key = date_to_find_day_as_str + " " + date_to_find_month_as_str

 i=0
 tickets_string = " "
 while i < len(tickets_dict[dict_key]):
    tickets_string = tickets_string + "  " + tickets_dict[dict_key][i].ticketno
    i=i+1

 print " "
 print dict_key + " :  " + tickets_string


 if days_ago == 0: #we have now reached todays date - end
     break
 days_ago = days_ago - 1 #decrement


# We should extend this to send the email automatically

