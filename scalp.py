from selenium import webdriver
import time
from datetime import datetime
import smtplib
#Email Setup
conn = smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('gpustockcheck12@gmail.com','gPuP@sSw0rD')
#Email Setup End
browser = webdriver.Chrome()
instock = False
curtime = datetime.now()
dt_string = curtime.strftime("%d/%m/%Y %H:%M:%S")
usremail = ""
page = input("Please enter the link for the item: ")
def menu():
    global usremail
    emailch = input("Do you want to enable email notifs? (Y/N)")
    if emailch == "Y":
        usremail = input("Please enter your email in the form 'example@example.com': ")
    cont = True
    while cont:
        global page
        print("Scalper Bot 10000000")
        print('*' * 20)
        print("     1) Check Stock")
        print("     2) Buy Item")
        print("     3) Check stock every minute")
        print("     4) Exit")
        choice = input("Please select an option: ")
        if choice == "1":
            check_stock(page)
        elif choice == "2":
            add_cart(page)
        elif choice == "3":
            time_check(page)
        elif choice == "4":
            cont = False
            
def check_stock(check_page):
    global browser
    global instock
    browser.get(check_page)
    try: 
        elem = browser.find_element_by_xpath('//button[text()="Add to Cart"]')
        print(f"[{dt_string}]: Item is in stock")
        instock = True
    except:
        print(f"[{dt_string}]: Out of stock")  
def add_cart(buy_page):
    global browser
    try: 
        elem = browser.find_element_by_xpath('//button[text()="Add to Cart"]')
        elem.click()
        print("Item is in stock and has been added to cart")
    except:
        print("Out of stock")  
def time_check(chk_page):
    global browser
    global usremail
    check_stock(chk_page)
    while not instock:
        check_stock(chk_page)
        browser.refresh()
        time.sleep(60)
    if instock == True:
        send_email()
        
        add_cart(chk_page)
        time.sleep(5)
        elem = browser.find_element_by_xpath('//button[text()="Checkout"]')
        elem.click()
        time.sleep(10)

def send_email():
    global usremail
    conn.sendmail('gpustockchecker12@gmail.com', usremail, 'Subject: INSTOCK NOTIFICATION \n\n Your item that you were following is in stock. Please go to your machine and enter payment info to secure the item. \n\n This is an automated email, please do not reply.')
    print(f"An email has been sent to {usremail}")
menu()