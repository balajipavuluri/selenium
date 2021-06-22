import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

@st.cache

st.title('codetantra login bot')
with st.form(key="form1"):
    mail=st.text_input("Enter mail")
    passw=st.text_input("Enter passw", type="password")
    #x=st.slider("class no",min_value=1,max_value=4)

    #x=st.text_input("enter class no")



    x = st.selectbox(
        'which class  you like to attend?',
         ('class-1', 'class-2','class-3', 'class-4'))



    action= st.selectbox(
        'which   you like to do?',
         ('listen', 'mute','microphone'))



    x=list(x)
    x=x[-1]
    #st.write(x)
    y=str(x)
    y='//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[{0}]/div'.format(x)

 
    submit=st.form_submit_button("click here")
    if submit:
        #driver = webdriver.Chrome(executable_path="E:/selenium/chromedriver")
        driver.maximize_window()

        driver.get("https://rvrjcce.codetantra.com")
        time.sleep(1)
        time.sleep(1)
        l=driver.find_element_by_link_text("Log in")
        l.click()
        time.sleep(1)

        
        m_btn= driver.find_element_by_name('loginId')
        m_btn.clear()
        #mail=m+'@gmail.com'
        m_btn.send_keys(mail)
        time.sleep(1)

        p_btn=driver.find_element_by_name('password')
        p_btn.clear()
        p_btn.send_keys(passw)
        time.sleep(1)


        sub=driver.find_element_by_xpath('//button[text()="Submit"]')
        sub.click()
        time.sleep(1)
        


        time.sleep(1)
        
        meet_path='/html/body/div[9]/div/div[1]/div/div/div[1]/div/div[2]/a'
        meet = driver.find_element_by_xpath(meet_path)
        meet.click()

            
        time.sleep(1)
          
       

        cl= driver.find_element_by_xpath(y) #c_d[x])

        cl.click()
        try:
            j=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/a')
        #j=driver.find_element_by_class_name('btn btn-primary btn-block btn-sm')
            j.click()
        except:
            st.write("Class not active:",x)
        #time.click(3)
        #audio = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i')
        #audio.click(3)
        try:
            #act=driver.find_element_by_class_name('label--Z12LMR3')
            act=driver.find_elements_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/span/button[2]')

            
            
            st.write(act)
            time.sleep(5)
            act.click()
        except:
            st.write('cannot click!')

    else:
       pass
