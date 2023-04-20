from selenium import webdriver
import time
import random
web = webdriver.Chrome()
namelist=[    'Aarushi Gupta',    'Aditi Singh',    'Ahana Patel',    'Akanksha Mehta',    'Alia Desai',    'Amrita Shah',    'Ananya Joshi',    'Anjali Krishnan',    'Anushka Varma',    'Aparna Nair',    'Aradhya Bhatia',    'Archana Menon',    'Asha Kaur',    'Avantika Chakraborty',    'Bhavya Choudhary',    'Charu Sharma',    'Devika Iyer',    'Diya Kapoor',    'Esha Singh',    'Gauri Trivedi',    'Ishita Datta',    'Janhvi Patel',    'Jhanvi Agarwal',    'Kavya Gupta',    'Khushi Sharma',    'Kiara Bajaj',    'Krisha Shah',    'Lekha Nambiar',    'Mira Nair',    'Muskaan Khanna',    'Nandini Menon',    'Navya Rao',    'Neha Singhania',    'Niharika Reddy',    'Nithya Nair',    'Palak Shah',    'Pooja Sharma',    'Prerna Bajaj',    'Rashi Sharma',    'Rhea Chakraborty',    'Ritika Singh',    'Ruchi Verma',    'Sana Ali',    'Sanjana Gupta',    'Shalini Singh',    'Shivani Deshpande',    'Sneha Iyer',    'Tanvi Sharma',    'Trisha Choudhary',    'Vaishali Pandey']

# elements filling starts here
for i in range(50):
    web.get("https://docs.google.com/forms/d/e/1FAIpQLSfI3p42_EqRYZaeqWnnK_V7qHg4TCINvdNNTIjcjTOfcpgAbA/viewform?usp=sf_link")
    time.sleep(2)
    sname = random.choice(namelist)
    name = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys(sname)
    age_button= web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    age_button.click()
    use_button=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    use_button.click()
    gender_button=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span')
    gender_button.click()
    occupation_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    occupation_button.click()

    incomegroup_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    incomegroup_button.click()

    dailyproducts_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span')
    dailyproducts_button.click()

    otherproducts_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    otherproducts_button.click()

    quality_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    quality_button.click()

    loyal_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    loyal_button.click()

    advertisement_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    advertisement_button.click()

    satisfaction_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    satisfaction_button.click()

    often_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    often_button.click()

    motivation_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    motivation_button.click()

    availability_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    availability_button.click()

    future_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    future_button.click()
    submit=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()
    filled_list=[]
    filled_list.append(sname)
    namelist.remove(sname)


    time.sleep(1)
print(filled_list)