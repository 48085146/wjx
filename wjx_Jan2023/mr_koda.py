# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 2023

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
        # Q1: 您的性别 (2 options)
        print("Q1:")
        q1_xpath = ''
        float_q1 = random.random()
        if  float_q1 > 0 and float_q1 <= 0.5:            
            q1_xpath = '//*[@id="div1"]/div[2]/div[1]/span/a'
            
        else:
            q1_xpath = '//*[@id="div1"]/div[2]/div[2]/span/a'
                    
        q1 = driver.find_element_by_xpath(q1_xpath)
        q1.click()    
    
    
        # Q2: 您的年龄 (5 options)
        print("Q2:")
        q2_xpath = ''
        float_q2 = random.random()
        if  float_q2 > 0 and float_q2 <= 0.2:
            q2_xpath = '//*[@id="div2"]/div[2]/div[1]/span/a'
        elif  float_q2 > 0.2 and float_q2 <= 0.4:
            q2_xpath = '//*[@id="div2"]/div[2]/div[2]/span/a'
        elif  float_q2 > 0.4 and float_q2 <= 0.6:
            q2_xpath = '//*[@id="div2"]/div[2]/div[3]/span/a'
        elif  float_q2 > 0.6 and float_q2 <= 0.8:
            q2_xpath = '//*[@id="div2"]/div[2]/div[4]/span/a'
        else:
            q2_xpath = '//*[@id="div2"]/div[2]/div[5]/span/a'
        
        q2 = driver.find_element_by_xpath(q2_xpath)
        q2.click()
            
        
        # Q3: 您的学历 (4 options)
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
    
    
        # Q4: 您的月度总支出 (5 options)
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
    
    
        # Q5: 您的婚姻状况 (2 options)    
        print("Q5:")
        q5_xpath = ''

        float_q5 = random.random()
        if  float_q5 > 0 and float_q5 <= 0.5:
            q5_xpath = '//*[@id="div5"]/div[2]/div[1]/span/a'
        else:
            q5_xpath = '//*[@id="div5"]/div[2]/div[2]/span/a'

        q5 = driver.find_element_by_xpath(q5_xpath)
        q5.click()
    
        
        # Q6: 您的新冠感染状态 (3 options)
        print("Q6:")
        q6_xpath = ''
        float_q6 = random.random()
        if  float_q6 > 0 and float_q6 <= 0.33:
            q6_xpath = '//*[@id="div6"]/div[2]/div[1]/span/a'
        elif  float_q6 > 0.33 and float_q6 <= 0.66:
            q6_xpath = '//*[@id="div6"]/div[2]/div[2]/span/a'
        else:
            q6_xpath = '//*[@id="div6"]/div[2]/div[3]/span/a'
        
        q6 = driver.find_element_by_xpath(q6_xpath)
        q6.click()    
        
        # Q7: 你为什么会用这种类型的图作为头像 (1~3 in 9 options)
        print("Q7:")
        q7_xpath = ''

        # start to process multiple choice
        list_q = [1,2,3,4,5,6,7,8,9]

        for i in range(0,3):

            #must do in the first loop, in the following depends on odds whether greater than 0.5
            if  i == 0:
                pass
            else:
                ind = random.random()
                if  ind > 0.5:
                    print("i is: ", i, "continue the processing. indicator is:", ind)
                    pass
                else:
                    print("i is: ", i, "skip the looping. indicator is:", ind)
                    continue
            
            x = random.choice(list_q)

            q7_xpath = '//*[@id="div7"]/div[2]/div['+ str(x) +']/span/a'

            list_q.remove(x)

            print("q7_xpath", q7_xpath)
            print("list_q", list_q)
            q7 = driver.find_element_by_xpath(q7_xpath)
            q7.click() 

            time.sleep(1)
        # end of looping processing


        # Q8: 在什么情况下你会采用自己真实的照片作为个人形象 (1~3 in 7 options)
        print("Q8:")
        q8_xpath = ''

        # start to process multiple choice
        list_q = [1,2,3,4,5,6,7]

        for i in range(0,3):

            #must do in the first loop, in the following depends on odds whether greater than 0.5
            if  i == 0:
                pass
            else:
                ind = random.random()
                if  ind > 0.5:
                    print("i is: ", i, "continue the processing. indicator is:", ind)
                    pass
                else:
                    print("i is: ", i, "skip the looping. indicator is:", ind)
                    continue
            
            x = random.choice(list_q)

            q8_xpath = '//*[@id="div8"]/div[2]/div['+ str(x) +']/span/a'
            #     q8_xpath = '//*[@id="div8"]/div[2]/div[6]/span/a'

            list_q.remove(x)

            print("q8_xpath", q8_xpath)
            print("list_q", list_q)
            q8 = driver.find_element_by_xpath(q8_xpath)
            q8.click() 

            time.sleep(1)
        # end of looping processing 
             
        
        # Q9: 你用自己真实头像的用意是什么 (1~3 in 9 options)
        print("Q9:")
        q9_xpath = ''

        # start to process multiple choice
        list_q = [1,2,3,4,5,6,7,8,9]

        for i in range(0,3):

            #must do in the first loop, in the following depends on odds whether greater than 0.5
            if  i == 0:
                pass
            else:
                ind = random.random()
                if  ind > 0.5:
                    print("i is: ", i, "continue the processing. indicator is:", ind)
                    pass
                else:
                    print("i is: ", i, "skip the looping. indicator is:", ind)
                    continue
            
            x = random.choice(list_q)

            q9_xpath = '//*[@id="div9"]/div[2]/div['+ str(x) +']/span/a'
            # q9_xpath = '//*[@id="div9"]/div[2]/div[5]/span/a'

            list_q.remove(x)

            print("q9_xpath", q9_xpath)
            print("list_q", list_q)
            q9 = driver.find_element_by_xpath(q9_xpath)
            q9.click() 

            time.sleep(1)
        # end of looping processing


        # Q10: 与疫情政策放开之前相比，您纯正餐饮消费支出将会 (5 options)
        print("Q10:")
        q10_xpath = ''
        float_q10 = random.random()
        if  float_q10 > 0 and float_q10 <= 0.2:
            q10_xpath = '//*[@id="div10"]/div[2]/div[1]/span/a'
        elif  float_q10 > 0.2 and float_q10 <= 0.4:
            q10_xpath = '//*[@id="div10"]/div[2]/div[2]/span/a'
        elif  float_q10 > 0.4 and float_q10 <= 0.6:
            q10_xpath = '//*[@id="div10"]/div[2]/div[3]/span/a'
        elif  float_q10 > 0.6 and float_q10 <= 0.8:
            q10_xpath = '//*[@id="div10"]/div[2]/div[4]/span/a'
        else:
            q10_xpath = '//*[@id="div10"]/div[2]/div[5]/span/a'

        q10 = driver.find_element_by_xpath(q10_xpath)
        q10.click()    



        # Q11: 与疫情政策放开前相比，您线下就餐的频率 (3 options)
        print("Q11:")
        q11_xpath = ''
        float_q11 = random.random()
        if  float_q11 > 0 and float_q11 <= 0.2:
            q11_xpath = '//*[@id="div11"]/div[2]/div[1]/span/a'
        elif  float_q11 > 0.2 and float_q11 <= 0.4:
            q11_xpath = '//*[@id="div11"]/div[2]/div[2]/span/a'
        elif  float_q11 > 0.4 and float_q11 <= 0.6:
            q11_xpath = '//*[@id="div11"]/div[2]/div[3]/span/a'
        elif  float_q11 > 0.6 and float_q11 <= 0.8:
            q11_xpath = '//*[@id="div11"]/div[2]/div[4]/span/a'
        else:
            q11_xpath = '//*[@id="div11"]/div[2]/div[5]/span/a'
        
        q11 = driver.find_element_by_xpath(q11_xpath)
        q11.click()


        # Q12: 疫情政策放开后，您会为了改善生活品质选择线下餐饮消费 (4 options)
        print("Q12:")
        q12_xpath = ''
        float_q12 = random.random()
        if  float_q12 > 0 and float_q12 <= 0.2:
            q12_xpath = '//*[@id="div12"]/div[2]/div[1]/span/a'
        elif  float_q12 > 0.2 and float_q12 <= 0.4:
            q12_xpath = '//*[@id="div12"]/div[2]/div[2]/span/a'
        elif  float_q12 > 0.4 and float_q12 <= 0.6:
            q12_xpath = '//*[@id="div12"]/div[2]/div[3]/span/a'
        elif  float_q12 > 0.6 and float_q12 <= 0.8:
            q12_xpath = '//*[@id="div12"]/div[2]/div[4]/span/a'
        else:
            q12_xpath = '//*[@id="div12"]/div[2]/div[5]/span/a'

        q12 = driver.find_element_by_xpath(q12_xpath)
        q12.click()


        # Q13: 疫情的长期封控会让您更渴望线下餐饮消费 (4 options)
        print("Q13:")
        q13_xpath = ''
        float_q13 = random.random()
        if  float_q13 > 0 and float_q13 <= 0.2:
            q13_xpath = '//*[@id="div13"]/div[2]/div[1]/span/a'
        elif  float_q13 > 0.2 and float_q13 <= 0.4:
            q13_xpath = '//*[@id="div13"]/div[2]/div[2]/span/a'
        elif  float_q13 > 0.4 and float_q13 <= 0.6:
            q13_xpath = '//*[@id="div13"]/div[2]/div[3]/span/a'
        elif  float_q13 > 0.6 and float_q13 <= 0.8:
            q13_xpath = '//*[@id="div13"]/div[2]/div[4]/span/a'
        else:
            q13_xpath = '//*[@id="div13"]/div[2]/div[5]/span/a'

        q13 = driver.find_element_by_xpath(q13_xpath)
        q13.click()


        # Q14: 疫情政策放开后，亲朋好友的推荐让您更愿意选择线下餐饮消费 (5 options)
        print("Q14:")
        q14_xpath = ''
        float_q14 = random.random()
        if  float_q14 > 0 and float_q14 <= 0.2:
            q14_xpath = '//*[@id="div14"]/div[2]/div[1]/span/a'
        elif  float_q14 > 0.2 and float_q14 <= 0.4:
            q14_xpath = '//*[@id="div14"]/div[2]/div[2]/span/a'
        elif  float_q14 > 0.4 and float_q14 <= 0.6:
            q14_xpath = '//*[@id="div14"]/div[2]/div[3]/span/a'
        elif  float_q14 > 0.6 and float_q14 <= 0.8:
            q14_xpath = '//*[@id="div14"]/div[2]/div[4]/span/a'
        else:
            q14_xpath = '//*[@id="div14"]/div[2]/div[5]/span/a'

        q14 = driver.find_element_by_xpath(q14_xpath)
        q14.click()


        # Q15: 疫情政策放开后，政府或商家 针对 性的消费券会让您更愿意选择线下餐饮消费 (5 options)
        print("Q15:")
        q15_xpath = ''
        float_q15 = random.random()
        if  float_q15 > 0 and float_q15 <= 0.2:
            q15_xpath = '//*[@id="div15"]/div[2]/div[1]/span/a'
        elif  float_q15 > 0.2 and float_q15 <= 0.4:
            q15_xpath = '//*[@id="div15"]/div[2]/div[2]/span/a'
        elif  float_q15 > 0.4 and float_q15 <= 0.6:
            q15_xpath = '//*[@id="div15"]/div[2]/div[3]/span/a'
        elif  float_q15 > 0.6 and float_q15 <= 0.8:
            q15_xpath = '//*[@id="div15"]/div[2]/div[4]/span/a'
        else:
            q15_xpath = '//*[@id="div15"]/div[2]/div[5]/span/a'

        q15 = driver.find_element_by_xpath(q15_xpath)
        q15.click()


        # Q16: 疫情政策放开后，餐厅的相关推送和“网红打卡”宣传会让您更愿意选择线下餐饮消费 (5 options)
        print("Q16:")
        q16_xpath = ''
        float_q16 = random.random()
        if  float_q16 > 0 and float_q16 <= 0.2:
            q16_xpath = '//*[@id="div16"]/div[2]/div[1]/span/a'
        elif  float_q16 > 0.2 and float_q16 <= 0.4:
            q16_xpath = '//*[@id="div16"]/div[2]/div[2]/span/a'
        elif  float_q16 > 0.4 and float_q16 <= 0.6:
            q16_xpath = '//*[@id="div16"]/div[2]/div[3]/span/a'
        elif  float_q16 > 0.6 and float_q16 <= 0.8:
            q16_xpath = '//*[@id="div16"]/div[2]/div[4]/span/a'
        else:
            q16_xpath = '//*[@id="div16"]/div[2]/div[5]/span/a'

        q16 = driver.find_element_by_xpath(q16_xpath)
        q16.click()


        # Q17: 疫情政策放开后，您会更加注重线下餐饮场所的消毒措施 (5 options)
        print("Q17:")
        q17_xpath = ''
        float_q17 = random.random()
        if  float_q17 > 0 and float_q17 <= 0.2:
            q17_xpath = '//*[@id="div17"]/div[2]/div[1]/span/a'
        elif  float_q17 > 0.2 and float_q17 <= 0.4:
            q17_xpath = '//*[@id="div17"]/div[2]/div[2]/span/a'
        elif  float_q17 > 0.4 and float_q17 <= 0.6:
            q17_xpath = '//*[@id="div17"]/div[2]/div[3]/span/a'
        elif  float_q17 > 0.6 and float_q17 <= 0.8:
            q17_xpath = '//*[@id="div17"]/div[2]/div[4]/span/a'
        else:
            q17_xpath = '//*[@id="div17"]/div[2]/div[5]/span/a'

        q17 = driver.find_element_by_xpath(q17_xpath)
        q17.click()


        # Q18: 疫情政策放开后，您会更加注重线下餐饮场所服务人员的口罩佩戴情况 (5 options)
        print("Q18:")
        q18_xpath = ''
        float_q18 = random.random()
        if  float_q18 > 0 and float_q18 <= 0.2:
            q18_xpath = '//*[@id="div18"]/div[2]/div[1]/span/a'
        elif  float_q18 > 0.2 and float_q18 <= 0.4:
            q18_xpath = '//*[@id="div18"]/div[2]/div[2]/span/a'
        elif  float_q18 > 0.4 and float_q18 <= 0.6:
            q18_xpath = '//*[@id="div18"]/div[2]/div[3]/span/a'
        elif  float_q18 > 0.6 and float_q18 <= 0.8:
            q18_xpath = '//*[@id="div18"]/div[2]/div[4]/span/a'
        else:
            q18_xpath = '//*[@id="div18"]/div[2]/div[5]/span/a'

        q18 = driver.find_element_by_xpath(q18_xpath)
        q18.click()


        # Q19: 疫情政策放开后，您会更加注重线下餐饮场所的座位间隔 (5 options)
        print("Q19:")
        q19_xpath = ''
        float_q19 = random.random()
        if  float_q19 > 0 and float_q19 <= 0.2:
            q19_xpath = '//*[@id="div19"]/div[2]/div[1]/span/a'
        elif  float_q19 > 0.2 and float_q19 <= 0.4:
            q19_xpath = '//*[@id="div19"]/div[2]/div[2]/span/a'
        elif  float_q19 > 0.4 and float_q19 <= 0.6:
            q19_xpath = '//*[@id="div19"]/div[2]/div[3]/span/a'
        elif  float_q19 > 0.6 and float_q19 <= 0.8:
            q19_xpath = '//*[@id="div19"]/div[2]/div[4]/span/a'
        else:
            q19_xpath = '//*[@id="div19"]/div[2]/div[5]/span/a'

        q19 = driver.find_element_by_xpath(q19_xpath)
        q19.click()


        # Q20: 疫情政策放开后，您对疫情发展情况更加关注 (5 options)
        print("Q20:")
        q20_xpath = ''
        float_q20 = random.random()
        if  float_q20 > 0 and float_q20 <= 0.2:
            q20_xpath = '//*[@id="div20"]/div[2]/div[1]/span/a'
        elif  float_q20 > 0.2 and float_q20 <= 0.4:
            q20_xpath = '//*[@id="div20"]/div[2]/div[2]/span/a'
        elif  float_q20 > 0.4 and float_q20 <= 0.6:
            q20_xpath = '//*[@id="div20"]/div[2]/div[3]/span/a'
        elif  float_q20 > 0.6 and float_q20 <= 0.8:
            q20_xpath = '//*[@id="div20"]/div[2]/div[4]/span/a'
        else:
            q20_xpath = '//*[@id="div20"]/div[2]/div[5]/span/a'

        q20 = driver.find_element_by_xpath(q20_xpath)
        q20.click()


        # Q21: 疫情政策放开后，您认为疫情对您生命健康威胁更大 (5 options)
        print("Q21:")
        q21_xpath = ''
        float_q21 = random.random()
        if  float_q21 > 0 and float_q21 <= 0.2:
            q21_xpath = '//*[@id="div21"]/div[2]/div[1]/span/a'
        elif  float_q21 > 0.2 and float_q21 <= 0.4:
            q21_xpath = '//*[@id="div21"]/div[2]/div[2]/span/a'
        elif  float_q21 > 0.4 and float_q21 <= 0.6:
            q21_xpath = '//*[@id="div21"]/div[2]/div[3]/span/a'
        elif  float_q21 > 0.6 and float_q21 <= 0.8:
            q21_xpath = '//*[@id="div21"]/div[2]/div[4]/span/a'
        else:
            q21_xpath = '//*[@id="div21"]/div[2]/div[5]/span/a'

        q21 = driver.find_element_by_xpath(q21_xpath)
        q21.click()


        # Q22: 疫情政策放开后，您认为疫情对您及家人工作生活的影响程度更深 (5 options)
        print("Q22:")
        q22_xpath = ''
        float_q22 = random.random()
        if  float_q22 > 0 and float_q22 <= 0.2:
            q22_xpath = '//*[@id="div22"]/div[2]/div[1]/span/a'
        elif  float_q22 > 0.2 and float_q22 <= 0.4:
            q22_xpath = '//*[@id="div22"]/div[2]/div[2]/span/a'
        elif  float_q22 > 0.4 and float_q22 <= 0.6:
            q22_xpath = '//*[@id="div22"]/div[2]/div[3]/span/a'
        elif  float_q22 > 0.6 and float_q22 <= 0.8:
            q22_xpath = '//*[@id="div22"]/div[2]/div[4]/span/a'
        else:
            q22_xpath = '//*[@id="div22"]/div[2]/div[5]/span/a'

        q22 = driver.find_element_by_xpath(q22_xpath)
        q22.click()


        # Q23: 外出线下就餐时，您更担心自己会被感染 (5 options)
        print("Q23:")
        q23_xpath = ''
        float_q23 = random.random()
        if  float_q23 > 0 and float_q23 <= 0.2:
            q23_xpath = '//*[@id="div23"]/div[2]/div[1]/span/a'
        elif  float_q23 > 0.2 and float_q23 <= 0.4:
            q23_xpath = '//*[@id="div23"]/div[2]/div[2]/span/a'
        elif  float_q23 > 0.4 and float_q23 <= 0.6:
            q23_xpath = '//*[@id="div23"]/div[2]/div[3]/span/a'
        elif  float_q23 > 0.6 and float_q23 <= 0.8:
            q23_xpath = '//*[@id="div23"]/div[2]/div[4]/span/a'
        else:
            q23_xpath = '//*[@id="div23"]/div[2]/div[5]/span/a'

        q23 = driver.find_element_by_xpath(q23_xpath)
        q23.click()


        # Q24: 疫情政策放开后，您的线下餐饮消费意愿为 (5 options)
        print("Q24:")
        q24_xpath = ''
        float_q24 = random.random()
        if  float_q24 > 0 and float_q24 <= 0.2:
            q24_xpath = '//*[@id="div24"]/div[2]/div[1]/span/a'
        elif  float_q24 > 0.2 and float_q24 <= 0.4:
            q24_xpath = '//*[@id="div24"]/div[2]/div[2]/span/a'
        elif  float_q24 > 0.4 and float_q24 <= 0.6:
            q24_xpath = '//*[@id="div24"]/div[2]/div[3]/span/a'
        elif  float_q24 > 0.6 and float_q24 <= 0.8:
            q24_xpath = '//*[@id="div24"]/div[2]/div[4]/span/a'
        else:
            q24_xpath = '//*[@id="div24"]/div[2]/div[5]/span/a'

        q24 = driver.find_element_by_xpath(q24_xpath)
        q24.click()


        # Q25: 疫情政策放开后，您认为线下餐饮消费的安全程度 (5 options)
        print("Q25:")
        q25_xpath = ''
        float_q25 = random.random()
        if  float_q25 > 0 and float_q25 <= 0.2:
            q25_xpath = '//*[@id="div25"]/div[2]/div[1]/span/a'
        elif  float_q25 > 0.2 and float_q25 <= 0.4:
            q25_xpath = '//*[@id="div25"]/div[2]/div[2]/span/a'
        elif  float_q25 > 0.4 and float_q25 <= 0.6:
            q25_xpath = '//*[@id="div25"]/div[2]/div[3]/span/a'
        elif  float_q25 > 0.6 and float_q25 <= 0.8:
            q25_xpath = '//*[@id="div25"]/div[2]/div[4]/span/a'
        else:
            q25_xpath = '//*[@id="div25"]/div[2]/div[5]/span/a'

        q25 = driver.find_element_by_xpath(q25_xpath)
        q25.click()


        time.sleep(5)
        print("Submit 1: 提交")
        # button_submit_xpath = '//*[@id="divSubmit"]/div[1]/div/a'
        button_submit_xpath = '//*[@id="ctlNext"]'
        button_submit = driver.find_element_by_xpath(button_submit_xpath)
        button_submit.click()        
        time.sleep(3)        


        # 模拟点击智能验证按钮
        # 先点确认
        # '//*[@id="layui-layer1"]/div[3]/a[1]'
        # in Jan 2023, found that the element is changed from button to href, xpath is modified accordingly
        button_confirm_xpath = "//a[text()='确认']"
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

    for i in range (0, 10):
        
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
        
        #go to the website: 疫情防控“新十条”下市民线下餐饮消费意愿及影响因素
        driver.get('https://www.wjx.cn/vm/PstF1ot.aspx')
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