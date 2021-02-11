from selenium import webdriver
import time
from datetime import datetime
browser = webdriver.Chrome()
instock = False

page = input("Please enter the link for the item: ")
def menu():
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
        print(f"[{datetime.now()}]: Item is in stock")
        instock = True
    except:
        print(f"[{datetime.now()}]: Out of stock")  
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
    check_stock(chk_page)
    while not instock:
        check_stock(chk_page)
        browser.refresh()
        time.sleep(60)
    if instock == True:
        add_cart(chk_page)
        time.sleep(5)
        elem = browser.find_element_by_xpath('//button[text()="Checkout"]')
        elem.click()
        time.sleep(10)
menu()