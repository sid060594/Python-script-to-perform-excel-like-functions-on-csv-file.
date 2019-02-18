# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 18:31:13 2019

@author: Siddharth 
"""

import datetime
#Reading CSV file
import csv

#Finding list of unique tickers
with open('C:/Users/sid06/Desktop/work stuffs/Bank.csv','r') as f:
    reader = csv.reader(f)
    output=[]
    #Finding unique ticker elements
    for row in reader:
        if (row[6]=='D' and row[5].upper() not in output): 
            output.append(row[5])
        ticker_copy=output.copy()

#Finding list of years        
with open('C:/Users/sid06/Desktop/miku stuffs/Bank.csv','r') as f:
    year_reader = csv.reader(f)
    years=[]  
    #Finding year counts and putting that in a list
    for row in year_reader:
        if (row[6]=='D' and (datetime.datetime.strptime(row[8], "%m/%d/%Y")).year not in years): 
            years.append((datetime.datetime.strptime(row[8], "%m/%d/%Y")).year)
            years = sorted(years)
    #print(years)        
            
#Main Operation: Finding Total Shares            
with open('C:/Users/sid06/Desktop/miku stuffs/Bank.csv','r') as f:
    new_reader = csv.reader(f) 
    new_list=[]
    write_list=[['Ticker','Year','Quarter','Total_Shares']]
    for each in ticker_copy:
        for item in years:
            ticker=each
            mylist = []
            quarter = [1,2,3,4]
            i=1
            j=i+1
            k=j+1
            for x in quarter:
                mylist = []
                for row in new_reader:
                    if (row[6]=='D' and row[5].upper()==ticker):
                        date = datetime.datetime.strptime(row[8], "%m/%d/%Y") 
                        
                        if(date.year == item and (date.month == i or date.month==j or date.month==k)):
                            mylist.append(float(row[9]))
                new_list = [ticker,item,x,sum(mylist)]
                
                if (new_list not in write_list):
                    write_list.append(new_list)
                    #print(write_list)
         
                print('Total_Shares_of_'+ticker+' in '+str(item)+' for Quarter '+str(x)+': ', sum(mylist))
                
                #resetting the file to beginning so that we can read again
                f.seek(0)
                #Incrementing quarter values
                i=i+3   
                j=j+3
                k=k+3
            print('                                                                                 ')
        print('====================== END OF '+ str(each)+' TICKER ======================================')          
        print('                                                                                 ')    
                
with open('C:/Users/sid06/Desktop/miku stuffs/Shares_Test.csv', 'w', newline='') as f:
    writer=csv.writer(f)
    for record in write_list:
        writer.writerow(record)
                        
