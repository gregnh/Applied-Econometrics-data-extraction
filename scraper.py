# -*- coding: utf-8 -*-
"""
 Applied Econometrics
 Collecting data
 
 Website scraped:
     Basketball reference
     
"""

import selenium

import pandas as pd
import numpy as np
import random as rd

#needed to convert unicode to numeric
import unicodedata

import csv

import time
import os

path = 'C:\\Users\\namhe\\Documents\\\M1\\Applied\\Project\\Data'
os.chdir(path)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# For explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Actions
from selenium.webdriver.common.action_chains import ActionChains

# Exception
from selenium.common.exceptions import NoSuchElementException

# Open Chrome browser
driver = webdriver.Chrome()
driver.implicitly_wait(5) # open the browser within 5sec


url='http://www.basketball-reference.com/leagues'
driver.get(url)


########## Functions ################

def get_boxscore( row, month):
    global game
    ind = str(row)
        
    time.sleep( round(rd.uniform(0.7, 1.1),3 ))
                
    bs_xpath ='//*[@id="schedule"]/tbody/tr['+ind+']/td[6]/a'
    driver.find_element_by_xpath(bs_xpath).click()# getting access to the boxscore row

    game += 1 #Game number x of the season

    driver.implicitly_wait(5)   
    date = driver.current_url[-17:-9]
        
    # Getting team abbreviation
    team1 = driver.find_element_by_xpath('//*[@id="line_score"]/tbody/tr[2]/td[1]/a').text
    team2 = driver.find_element_by_xpath('//*[@id="line_score"]/tbody/tr[3]/td[1]/a').text
                
    team1 = team1.lower()
    team2 = team2.lower()
                
    team1adv_xpath = '//*[@id="all_box_'+team1+'_advanced"]/div[1]/div/ul/li[1]/span'
    team2adv_xpath = '//*[@id="all_box_'+team2+'_advanced"]/div[1]/div/ul/li[1]/span'
        
    team1bas_xpath = '//*[@id="all_box_'+team1+'_basic"]/div[1]/div/ul/li[1]/span'        
    team2bas_xpath = '//*[@id="all_box_'+team2+'_basic"]/div[1]/div/ul/li[1]/span'    
        

    name1 = driver.find_element_by_xpath('//*[@id="all_box_'+team1+'_basic"]/div[1]/h2').text 
    name2 = driver.find_element_by_xpath('//*[@id="all_box_'+team2+'_basic"]/div[1]/h2').text 

    # Create folder 
    newpath = path+'\\'+str(season)+'\\'+month+'\\'+'Game '+str(game)+' - '+name1+'_v_'+name2
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    # Team 1
        
    ## Basic Box score
        
    # Click on Share & More
    driver.implicitly_wait(5)
    time.sleep(1.01)
        
    driver.find_element_by_xpath(team1bas_xpath).click()
    #team1_bbs.click()
                
    # Get table as CSV
    time.sleep(round(rd.uniform(0.4,1.1) , 3))
    driver.implicitly_wait(5)
                
    team1bas_xpath_tocsv = '//*[@id="all_box_'+team1+'_basic"]/div[1]/div/ul/li[1]/div/ul/li[3]/button'
    driver.find_element_by_xpath(team1bas_xpath_tocsv).click()
    #team1_bbs.click()

    # Select csv text
    team1bas_xpath_csv = '//*[@id="csv_box_'+team1+'_basic"]'
    team1_csv_bas = driver.find_element_by_xpath(team1bas_xpath_csv).text
    team1_csv_bas =  "\n".join(team1_csv_bas.split('\n')[1:]) #  remove la premiere ligne
        
    # Put it into a csv file
    list = team1_csv_bas.split('\n')
        
        
    filename = 'Game'+str(game)+'_'+str(date)+'_'+team1+'_bas'
    newpath1 = newpath+'\\'+filename+'.csv'    
    myfile=  open(newpath1, mode = 'w') # 'w' for writing 
    wr = csv.writer(myfile, delimiter=',', lineterminator='\r\n')
    wr.writerows( [x.split(',') for x in list] )
    myfile.close()

    
    ## Advanced box score
        
    # Click on Share & More
    driver.implicitly_wait(5)
    time.sleep(round(rd.uniform(0.5,1) , 3))
    
    driver.find_element_by_xpath(team1adv_xpath).click()
    #team1_abs.click()
                
    # Get table as CSV
    time.sleep(round(rd.uniform(0.4,1.1) , 3))
    driver.implicitly_wait(5)
                
    team1adv_xpath_tocsv = '//*[@id="all_box_'+team1+'_advanced"]/div[1]/div/ul/li[1]/div/ul/li[3]/button'
    driver.find_element_by_xpath(team1adv_xpath_tocsv).click()
    #team1_abs.click()

    # Select csv text
    team1adv_xpath_csv = '//*[@id="csv_box_'+team1+'_advanced"]'
    team1_csv_adv = driver.find_element_by_xpath(team1adv_xpath_csv).text
    team1_csv_adv =  "\n".join(team1_csv_adv.split('\n')[1:]) #  remove la premiere ligne
        
    # Put it into a csv file
    list = team1_csv_adv.split('\n')
    
    
    filename = 'Game'+str(game)+'_'+str(date)+'_'+team1+'_adv'
    newpath1 = newpath+'\\'+filename+'.csv'    
    myfile=  open(newpath1, mode = 'w') # 'w' for writing 
    wr = csv.writer(myfile, delimiter=',', lineterminator='\r\n')
    wr.writerows( [x.split(',') for x in list] )
    myfile.close()
        
        
    # Team 2
        ## Basic Box score
        
    # Click on Share & More
    driver.implicitly_wait(5)
    time.sleep(round(rd.uniform(0.5,1) , 3))
        
    driver.find_element_by_xpath(team2bas_xpath).click()
    #team2_bbs.click()
                
    # Get table as CSV
    time.sleep(round(rd.uniform(0.4,1.1) , 3))
    driver.implicitly_wait(5)
                
    team2bas_xpath_tocsv = '//*[@id="all_box_'+team2+'_basic"]/div[1]/div/ul/li[1]/div/ul/li[3]/button'
    driver.find_element_by_xpath(team2bas_xpath_tocsv).click()
    #team2_bbs.click()

    # Select csv text
    team2bas_xpath_csv = '//*[@id="csv_box_'+team2+'_basic"]'
    team2_csv_bas = driver.find_element_by_xpath(team2bas_xpath_csv).text
    team2_csv_bas =  "\n".join(team2_csv_bas.split('\n')[1:]) #  remove la premiere ligne
        
    # Put it into a csv file
    list = team2_csv_bas.split('\n')
    
    
    filename = 'Game'+str(game)+'_'+str(date)+'_'+team2+'_bas'
    newpath1 = newpath+'\\'+filename+'.csv'    
    myfile=  open(newpath1, mode = 'w') # 'w' for writing 
    wr = csv.writer(myfile, delimiter=',', lineterminator='\r\n')
    wr.writerows( [x.split(',') for x in list] )
    myfile.close()
          
        
    ## Advanced box score
    
    time.sleep(round(rd.uniform(0.5,1) , 3))    
    driver.implicitly_wait(5)
    
    
    # Click on Share & More
    driver.find_element_by_xpath(team2adv_xpath).click()
    #team2_abs.click()
                
    # Get table as CSV
    time.sleep(round(rd.uniform(0.4,1.1) , 3))
    driver.implicitly_wait(5)
    team2adv_xpath_tocsv = '//*[@id="all_box_'+team2+'_advanced"]/div[1]/div/ul/li[1]/div/ul/li[3]/button'
    driver.find_element_by_xpath(team2adv_xpath_tocsv).click()
    #team2_abs.click()
                
    # Select csv text
    team2adv_xpath_csv = '//*[@id="csv_box_'+team2+'_advanced"]'
    team2_csv_adv = driver.find_element_by_xpath(team2adv_xpath_csv).text
    team2_csv_adv =  "\n".join(team2_csv_adv.split('\n')[1:]) #  remove la premiere ligne (advanced stat ...)
        
    # Put it into a csv file
    list = team2_csv_adv.split('\n')
    
    
    filename = 'Game'+str(game)+'_'+str(date)+'_'+team2+'_adv'
    newpath1 = newpath+'\\'+filename+'.csv'      
    myfile=  open(newpath1, mode = 'w') # 'w' for writing 
    wr = csv.writer(myfile, delimiter=',', lineterminator='\r\n')
    wr.writerows( [x.split(',') for x in list] )
    myfile.close()
        
    time.sleep(round(rd.uniform(0.4,0.9) , 3))
    print( 'row ='+ind,'Game number '+str(game))
    driver.back()
    
    ######################################################## timeout
    
    
# Get boxscores for the entire month
def get_boxscores( start, total, month):
    for i in range(start, total+1):
        get_boxscore( i , month)
    
    
# Select the season and click on it
def pick_year( year):    # 2016 for the season 15-16, 2015 for 14-15 # till 1977
    tab_for_xpath = [i for i in range(2,43)]
                 
    
    year_list = sorted([i for i in range(1977,2018)], reverse = True)# sorting in ascending order
    
    if year in year_list:
        year_tab = np.column_stack(( year_list ,tab_for_xpath))
        
        a = year_list.index(year)
        i = year_tab[a][1] #in order to get the row associated to the year
    
        time.sleep(round(rd.uniform(0.8,1.5) , 3))
    
        ind = str(i)
    
        season_xpath='//*[@id="stats_clone"]/tbody/tr['+ind+']/th/a'
        driver.find_element_by_xpath(season_xpath).click()
    else:
        print('Choose a year between 1977 and 2018')
    
    
    
#################################################

game = 0 #game number initialisation

# Select the season
pick_year(2013) 
    
season = driver.current_url[-9:-5]
    
# Create season folder
newpath = path+'\\'+season
if not os.path.exists(newpath):
    os.makedirs(newpath)
        

# Click on 'schedule & results'
driver.implicitly_wait(4)
driver.find_element_by_xpath('//*[@id="inner_nav"]/ul/li[3]/a').click()

    
# Count nb of months during the selected season
driver.implicitly_wait(4)
nbmonth = driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div')
nbmonth = len(nbmonth)
tillApril = nbmonth-2
    

# 1st month games    
#Create month folder
month = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/a').text
newpath = path+'\\'+str(season)+'\\'+month
if not os.path.exists(newpath):
    os.makedirs(newpath)
        
# Count nb of games in that month
nbrows = driver.find_elements_by_xpath('//*[@id="schedule"]/tbody/tr')
nbrows = len(nbrows)  
        
get_boxscores(1, nbrows, month)
    
        
# Other months but April     
for mois in range(4,tillApril):
    m = str(mois)
    driver.implicitly_wait(4)
    
    month_xpath = '//*[@id="content"]/div[2]/div['+m+']/a'        
    month = driver.find_element_by_xpath(month_xpath).text
        
    newpath = path+'\\'+season+'\\'+month
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        
    time.sleep(round(rd.uniform(0.4,1.5) , 3))
        
    month_xpath = '//*[@id="content"]/div[2]/div['+m+']/a'
    driver.find_element_by_xpath(month_xpath).click()
            
    driver.implicitly_wait(5)
    nbrows = driver.find_elements_by_xpath('//*[@id="schedule"]/tbody/tr')
    nbrows = len(nbrows)
        
    get_boxscores(1 , nbrows, month)
    
    driver.implicitly_wait(4)
    
    driver.execute_script("window.scrollTo(0, 10);")

# April
time.sleep(round(rd.uniform(0.6,1.2) , 3))
    
newpath = path+'\\'+season+'\\April'
if not os.path.exists(newpath):
    os.makedirs(newpath)
    
april_xpath = '//*[@id="content"]/div[2]/div['+str(tillApril)+']/a'
driver.find_element_by_xpath(april_xpath).click()
    
driver.implicitly_wait(5)
nbrows = driver.find_elements_by_xpath('//*[@id="schedule"]/tbody/tr')
nbrows = len(nbrows)
    
for row in range(1, nbrows + 1):
    try :
        if driver.find_element_by_xpath('//*[@id="schedule"]/tbody/tr['+str(row)+']/td[6]/a'):
            get_boxscore( row , month = 'April' )

        else:
            break
    except NoSuchElementException:
        break
        
    
