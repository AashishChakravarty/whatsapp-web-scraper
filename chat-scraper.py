from selenium import webdriver
import csv

driver = webdriver.Chrome('C:/Users/Aashish/Downloads/chromedriver_win32/chromedriver')

driver.get('http://web.whatsapp.com')

print("Whatsapp web opened successfully")
input("Enter anything after loading page")
message = ''
a = ''

for user in driver.find_elements_by_xpath("//div[@class='RLfQR']"):
    user = driver.find_element_by_xpath('//span[@class = "_1wjpf"]')
    a=driver.find_element_by_xpath('//span[@class = "_1wjpf"]').text
    message+=''.join(a)
    message+= ","
    user.click()
    
    for messages in driver.find_elements_by_xpath("//div[@class='copyable-area']"):
        try:
            a = messages.find_element_by_xpath(
                ".//span[@class='selectable-text invisible-space copyable-text']"
            ).text
        except:
            try:
                message += messages.find_element_by_xpath(
                    ".//span[@class='emojitext selectable-text invisible-space copyable-text']"
                ).text
            except:
                pass
        message+=''.join(a)
    print(message)
    with open('chats.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(message)
        csvFile.close()
    print("done")
