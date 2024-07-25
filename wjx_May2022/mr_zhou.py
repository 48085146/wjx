# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 19:44:31 2021

@author: RODNEY

https://blog.csdn.net/qq_45717425/article/details/119737648

https://www.freesion.com/article/78571260093/

"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

import pandas as pd

import datetime
from datetime import date
import time

import decimal
import random


def check_element_exists_xpath(xpath):

    result = True
    try:
        driver.find_element_by_xpath(xpath)
    except:
        print("element not exists", xpath)
        result = False
    finally:
        return result


##########################################
def get_track(distance):
##########################################    

    track = []
    current = 0
    #t = 0.2
    t = random.random()
    if  t < 0.3:
        t = 0.5 + t
    elif t < 0.5:
        t = 0.3 + t
    else:
        pass 
    v = 0
    while current < distance:
        a = 50
        v0 = v
        v = v0 + a*t
        move = v0*t + a*t
        current += move

        track.append(round(move))

    return track

##########################################
def move_to_gap(slider, tracks):
##########################################

    ActionChains(driver).click_and_hold(slider).perform()
    for x in tracks:
        ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
    time.sleep(0.1)
    ActionChains(driver).release().perform()

    return


##########################################
def manipulate_data():
##########################################    
    
    try:
        # Q1: 性别 (2 options)
        print("Q1:")
        q1_xpath = ''
        float_q1 = random.random()
        if  float_q1 > 0 and float_q1 <= 0.5:
            # q1_xpath = '//*[@id="q1_1"]'
            q1_xpath = '//*[@id="div1"]/div[2]/div[1]/span/a'
            
        else:
            # q1_xpath = '//*[@id="q1_2"]'
            q1_xpath = '//*[@id="div1"]/div[2]/div[2]/span/a'
                    
        q1 = driver.find_element_by_xpath(q1_xpath)
        q1.click()    
    
    
        # Q2: 你会在意你的虚拟形象吗 (3 options)
        print("Q2:")
        q2_xpath = ''
        float_q2 = random.random()
        if  float_q2 > 0 and float_q2 <= 0.33:
            # q2_xpath = '//*[@id="q2_1"]'
            q2_xpath = '//*[@id="div2"]/div[2]/div[1]/span/a'
        elif  float_q2 > 0.33 and float_q2 <= 0.66:
            # q2_xpath = '//*[@id="q2_2"]'
            q2_xpath = '//*[@id="div2"]/div[2]/div[2]/span/a'
        else:
            # q2_xpath = '//*[@id="q2_3"]'
            q2_xpath = '//*[@id="div2"]/div[2]/div[3]/span/a'
        
        q2 = driver.find_element_by_xpath(q2_xpath)
        q2.click()
            
        
        # Q3: 你是否经常换形象 (4 options)
        print("Q3:")
        q3_xpath = ''
        float_q3 = random.random()
        if  float_q3 > 0 and float_q3 <= 0.25:
            q3_xpath = '//*[@id="div3"]/div[2]/div[1]/span/a'
        elif float_q3 > 0.25 and float_q3 <= 0.5:
            q3_xpath = '//*[@id="div3"]/div[2]/div[2]/span/a'
        elif float_q3 > 0.5 and float_q3 <= 0.75:
            q3_xpath = '//*[@id="div3"]/div[2]/div[3]/span/a'
        else:
            q3_xpath = '//*[@id="div3"]/div[2]/div[4]/span/a'
            
        q3 = driver.find_element_by_xpath(q3_xpath)
        q3.click()
    
    
        # Q4: 你换形象的时候会与什么有关系 (5 options)
        q4_xpath = ''
        print("Q4:")
        float_q4 = random.random()
        if  float_q4 > 0 and float_q4 <= 0.2:
            q4_xpath = '//*[@id="div4"]/div[2]/div[1]/span/a'
        elif float_q4 > 0.2 and float_q4 <= 0.4:
            q4_xpath = '//*[@id="div4"]/div[2]/div[2]/span/a'
        elif float_q4 > 0.4 and float_q4 <= 0.6:
            q4_xpath = '//*[@id="div4"]/div[2]/div[3]/span/a'
        elif float_q4 > 0.6 and float_q4 <= 0.8:
            q4_xpath = '//*[@id="div4"]/div[2]/div[4]/span/a'
        else:
            q4_xpath = '//*[@id="div4"]/div[2]/div[5]/span/a'
        
        q4 = driver.find_element_by_xpath(q4_xpath)
        q4.click()
    
    
        # Q5: 你希望你的虚拟形象被别人关注到吗？ (3 options)    
        print("Q5:")
        q5_xpath = ''

        float_q5 = random.random()
        if  float_q5 > 0 and float_q5 <= 0.2:
            q5_xpath = '//*[@id="div5"]/div[2]/div[1]/span/a'
        elif float_q5 > 0.2 and float_q5 <= 0.4:
            q5_xpath = '//*[@id="div5"]/div[2]/div[2]/span/a'
        else:
            q5_xpath = '//*[@id="div5"]/div[2]/div[3]/span/a'
        
        q5 = driver.find_element_by_xpath(q5_xpath)
        q5.click()
    
        
        # Q6: 你喜欢的虚拟形象类型是 (8 options)
        print("Q6:")
        q6_xpath = ''
        float_q6 = random.random()
        if  float_q6 > 0 and float_q6 <= 0.1:
            q6_xpath = '//*[@id="div6"]/div[2]/div[1]/span/a'
        elif  float_q6 > 0.1 and float_q6 <= 0.2:
            q6_xpath = '//*[@id="div6"]/div[2]/div[2]/span/a'
        elif  float_q6 > 0.2 and float_q6 <= 0.3:
            q6_xpath = '//*[@id="div6"]/div[2]/div[3]/span/a'
        elif  float_q6 > 0.3 and float_q6 <= 0.4:
            q6_xpath = '//*[@id="div6"]/div[2]/div[4]/span/a'
        elif  float_q6 > 0.4 and float_q6 <= 0.5:
            q6_xpath = '//*[@id="div6"]/div[2]/div[5]/span/a'
        elif  float_q6 > 0.5 and float_q6 <= 0.6:
            q6_xpath = '//*[@id="div6"]/div[2]/div[6]/span/a'
        elif  float_q6 > 0.6 and float_q6 <= 0.7:
            q6_xpath = '//*[@id="div6"]/div[2]/div[7]/span/a'
        else:
            q6_xpath = '//*[@id="div6"]/div[2]/div[8]/span/a'
        q6 = driver.find_element_by_xpath(q6_xpath)
        q6.click()    
        
        # Q7: 你为什么会用这种类型的图作为头像 (6 options)
        print("Q7:")
        q7_xpath = ''
        float_q7 = random.random()
        if  float_q7 > 0 and float_q7 <= 0.2:
            q7_xpath = '//*[@id="div7"]/div[2]/div[1]/span/a'
        elif  float_q7 > 0.2 and float_q7 <= 0.4:
            q7_xpath = '//*[@id="div7"]/div[2]/div[2]/span/a'
        elif  float_q7 > 0.4 and float_q7 <= 0.6:
            q7_xpath = '//*[@id="div7"]/div[2]/div[3]/span/a'
        elif  float_q7 > 0.6 and float_q7 <= 0.8:
            q7_xpath = '//*[@id="div7"]/div[2]/div[4]/span/a'
        elif  float_q7 > 0.8 and float_q7 <= 0.9:
            q7_xpath = '//*[@id="div7"]/div[2]/div[5]/span/a'
        else:
            q7_xpath = '//*[@id="div7"]/div[2]/div[6]/span/a'
        
        q7 = driver.find_element_by_xpath(q7_xpath)
        q7.click()    
        
        
        # Q8: 在什么情况下你会采用自己真实的照片作为个人形象 (6 options)
        print("Q8:")
        q8_xpath = ''
        float_q8 = random.random()
        if  float_q8 > 0 and float_q8 <= 0.2:
            q8_xpath = '//*[@id="div8"]/div[2]/div[1]/span/a'
        elif  float_q8 > 0.2 and float_q8 <= 0.4:
            q8_xpath = '//*[@id="div8"]/div[2]/div[2]/span/a'
        elif  float_q8 > 0.4 and float_q8 <= 0.6:
            q8_xpath = '//*[@id="div8"]/div[2]/div[3]/span/a'
        elif  float_q8 > 0.6 and float_q8 <= 0.8:
            q8_xpath = '//*[@id="div8"]/div[2]/div[4]/span/a'
        elif  float_q8 > 0.8 and float_q8 <= 0.9:
            q8_xpath = '//*[@id="div8"]/div[2]/div[5]/span/a'
        else:
            q8_xpath = '//*[@id="div8"]/div[2]/div[6]/span/a'
        q8 = driver.find_element_by_xpath(q8_xpath)
        q8.click()    
             
        
        # Q9: 你用自己真实头像的用意是什么 (5 options)
        print("Q9:")
        q9_xpath = ''
        float_q9 = random.random()
        if  float_q9 > 0 and float_q9 <= 0.2:
            q9_xpath = '//*[@id="div9"]/div[2]/div[1]/span/a'
        elif  float_q9 > 0.2 and float_q9 <= 0.4:
            q9_xpath = '//*[@id="div9"]/div[2]/div[2]/span/a'
        elif  float_q9 > 0.4 and float_q9 <= 0.6:
            q9_xpath = '//*[@id="div9"]/div[2]/div[3]/span/a'
        elif  float_q9 > 0.6 and float_q9 <= 0.8:
            q9_xpath = '//*[@id="div9"]/div[2]/div[4]/span/a'
        else:
            q9_xpath = '//*[@id="div9"]/div[2]/div[5]/span/a'
        
        q9 = driver.find_element_by_xpath(q9_xpath)
        q9.click()    
    

        # Q10: 你用自己真实头像的用意是什么 (4 options)
        print("Q10:")
        q10_xpath = ''
        float_q10 = random.random()
        if  float_q10 > 0 and float_q10 <= 0.25:
            q10_xpath = '//*[@id="div10"]/div[2]/div[1]/span/a'
        elif  float_q10 > 0.25 and float_q10 <= 0.5:
            q10_xpath = '//*[@id="div10"]/div[2]/div[2]/span/a'
        elif  float_q10 > 0.5 and float_q10 <= 0.75:
            q10_xpath = '//*[@id="div10"]/div[2]/div[3]/span/a'
        else:
            q10_xpath = '//*[@id="div10"]/div[2]/div[4]/span/a'
        
        q10 = driver.find_element_by_xpath(q10_xpath)
        q10.click()    



        # Q11: 你认为真实的头像会泄露隐私吗 (3 options)
        print("Q11:")
        q11_xpath = ''
        float_q11 = random.random()
        if  float_q11 > 0 and float_q11 <= 0.33:
            q11_xpath = '//*[@id="div11"]/div[2]/div[1]/span/a'
        elif  float_q11 > 0.33 and float_q11 <= 0.66:
            q11_xpath = '//*[@id="div11"]/div[2]/div[2]/span/a'
        else:
            q11_xpath = '//*[@id="div11"]/div[2]/div[3]/span/a'
        
        q11 = driver.find_element_by_xpath(q11_xpath)
        q11.click()


        # Q12: 你担心会泄露隐私信息吗 (4 options)
        print("Q12:")
        q12_xpath = ''
        float_q12 = random.random()
        if  float_q12 > 0 and float_q12 <= 0.25:
            q12_xpath = '//*[@id="div12"]/div[2]/div[1]/span/a'
        elif  float_q12 > 0.25 and float_q12 <= 0.5:
            q12_xpath = '//*[@id="div12"]/div[2]/div[2]/span/a'
        elif  float_q12 > 0.5 and float_q12 <= 0.75:
            q12_xpath = '//*[@id="div12"]/div[2]/div[3]/span/a'
        else:
            q12_xpath = '//*[@id="div12"]/div[2]/div[4]/span/a'
        
        q12 = driver.find_element_by_xpath(q12_xpath)
        q12.click()


        # Q13: 如果会泄露隐私信息，最让你担心的是什么 (4 options)
        print("Q13:")
        q13_xpath = ''
        float_q13 = random.random()
        if  float_q13 > 0 and float_q13 <= 0.25:
            q13_xpath = '//*[@id="div13"]/div[2]/div[1]/span/a'
        elif  float_q13 > 0.25 and float_q13 <= 0.5:
            q13_xpath = '//*[@id="div13"]/div[2]/div[2]/span/a'
        elif  float_q13 > 0.5 and float_q13 <= 0.75:
            q13_xpath = '//*[@id="div13"]/div[2]/div[3]/span/a'
        else:
            q13_xpath = '//*[@id="div13"]/div[2]/div[4]/span/a'
        
        q13 = driver.find_element_by_xpath(q13_xpath)
        q13.click()


        time.sleep(5)
        print("Submit 1: 提交")
        # button_submit_xpath = '//*[@id="divSubmit"]/div[1]/div/a'
        button_submit_xpath = '//*[@id="ctlNext"]'
        button_submit = driver.find_element_by_xpath(button_submit_xpath)
        button_submit.click()        
        time.sleep(3)        


        # 模拟点击智能验证按钮
        # 先点确认
        button_confirm_xpath = "//button[text()='确认']"
        if  check_element_exists_xpath(button_confirm_xpath) == True:
            driver.find_element_by_xpath(button_confirm_xpath).click()
            time.sleep(5)        
        else:
            print("'确认' button not exists")
            pass
            
        # 再点智能验证提示框，进行智能验证
        driver.find_element_by_xpath("//div[@id='captcha']").click()

        time.sleep(3)
        #滑块处理 begin
        print("slider:")
        slider_xpath = '//*[@id="nc_1_n1z"]'
        ind_slider = check_element_exists_xpath(slider_xpath)
        i = 0
        while(ind_slider):
            slider = driver.find_element_by_xpath(slider_xpath)
            move_to_gap(slider, get_track(260))
            time.sleep(5)
            i = i + 1
            a_refresh_xpath = '//*[@id="nc_' + str(i) + '_refresh1"]'
            if  check_element_exists_xpath(a_refresh_xpath) == True:
                a_refresh = driver.find_element_by_xpath(a_refresh_xpath)
                a_refresh.click()
                time.sleep(5)
            else:
                pass

            # <div id="alert_box" style="display: none;">
            div_alert_invisible_xpath = '//div[@id="alert_box" and @style="display: none;"]'
            if  check_element_exists_xpath(div_alert_invisible_xpath) == True:
                print("button confirm not visible")
                pass
            else:
                print("button confirm is visible")
                print("click the button confirm")
                button_confirm = driver.find_element_by_xpath(button_confirm_xpath)
                button_confirm.click()
                time.sleep(5)


            # print("button confirm:")
            # button_confirm_xpath = '//*[@id="alert_box"]//button[text()="确认"]'
            # if  check_element_exists_xpath(button_confirm_xpath) == True:
            #     # div_confirm_invisible_xpath = '//div[@id="alert_box" and contains(@display, none)]'
            #     div_confirm_invisible_xpath = '//div[@id="alert_box" and @style="display: none;"]'
            #     if  check_element_exists_xpath(div_confirm_invisible_xpath) == True:
            #         pass
            #         print("button confirm not visible")
            #     else:
            #         print("click the button confirm")
            #         button_confirm = driver.find_element_by_xpath(button_confirm_xpath)
            #         button_confirm.click()
            #         time.sleep(5)
            # else:
            #     pass

            slider_xpath = '//*[@id="nc_' + str(i+1) + '_n1z"]'
            print("next slider xpath: ", slider_xpath)
            ind_slider = check_element_exists_xpath(slider_xpath)

        #滑块处理 end

        print("Submit 2: 提交")
        time.sleep(1)        
        button_submit_xpath = '//*[@id="ctlNext"]'
        if  check_element_exists_xpath(button_submit_xpath) == True:
            print("Click Submit 2: 提交")
            button_submit = driver.find_element_by_xpath(button_submit_xpath)
            button_submit.click()        
            time.sleep(3)
        else:
            pass

        # after click "Submit 2", there may keep poping the confirm button as well as the slider with the id keep increasing nc_<i>_n1z
        # action="https://www.wjx.cn/joinnew/processjq.ashx?shortid=wv0m1ff"
        # style="overflow:hidden;"
        # id="form1"
        # method="post"

        time.sleep(3)        
        
        print("Return:")

        return
    
    except Exception as exception:
        print('Exception', exception)
        return     


##########################################
if  __name__ == '__main__':
##########################################

    output_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    check_time_00 = datetime.datetime.now()

    for i in range (0, 5):
        
        print ("i is: ", i)
        options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")
        # options.add_argument("--disable-blink-features=BlockCredentialedSubresources")
    
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--headless')
        # options.add_argument("--window-size=1920,1080")
        
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
    
        driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
        })
        
        driver.implicitly_wait(1)
        
        #go to the website
        driver.get('https://www.wjx.cn/vm/wv0m1ff.aspx')
        time.sleep(1)
        
        manipulate_data()
    
        driver.quit()

    check_time_99 = datetime.datetime.now()
    elapsed_time = check_time_99 - check_time_00
    print("check end: ", str(check_time_99), " , elapsed for: ", str(elapsed_time))
    
"""    
proxy_arr = [
     '--proxy-server=http://171.35.141.103:9999',
     '--proxy-server=http://36.248.132.196:9999',
     # '--proxy-server=http://125.46.0.62:53281',
     '--proxy-server=http://219.239.142.253:3128',
     '--proxy-server=http://119.57.156.90:53281',
     '--proxy-server=http://60.205.132.71:80',
     '--proxy-server=https://139.217.110.76:3128',
     '--proxy-server=https://116.196.85.150:3128'
 ]



chrome_options = Options()

proxy = random.choice(proxy_arr)  # 随机选择一个代理
print(proxy) #如果某个代理访问失败,可从proxy_arr中去除

chrome_options.add_argument(proxy)  # 添加代理    
"""