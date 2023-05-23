#Authors: Cortez e Nadja

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select

vetor = []
for i in range(len(vetor)):
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.maximize_window()
    driver.get('https://directa.natal.rn.gov.br/')
    time.sleep(5)
    driver.get('https://directa.natal.rn.gov.br/main.jsp?sys=DIR&a=qxG6rejnY45ft&firstLoad=true#');
                
    time.sleep(5)

    main_page = driver.current_window_handle
    print(main_page)
    time.sleep(5)

    action = webdriver.ActionChains(driver)
    element = driver.find_element(By.XPATH, '//*[@id="limenu1"]/div/a[16]') # or your another selector here
    action.move_to_element(element)
    action.perform()

    time.sleep(5)

    #action = webdriver.ActionChains(driver)
    #element = driver.find_element(By.XPATH, '//*[@id="formsmenu248"]/li/a/span') # or your another selector here
    #action.move_to_element(element)
    #action.perform()

    #driver.element.click()

    driver.find_element(By.XPATH, '//*[@id="formsmenu248"]/li/a/span').click()

    time.sleep(2)

    #login_page = None
            

    driver.get('https://directa.natal.rn.gov.br/openform.do?sys=DIR&action=openform&formID=464568467&align=0&mode=-1&goto=-1&filter=&scrolling=no#')
    time.sleep(2)
    #driver.find_element(By.XPATH, '//*[@id="lay"]/div[2]/div[2]/div[11]/div[2]/input')

    elem1 = driver.find_element(By.XPATH, '//*[@id="lay"]/div[2]/div[2]/div[11]/div[2]/input')
    elem1.clear()
    elem1.send_keys(vetor[i][0])

    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="lay"]/div[2]/div[2]/div[9]/div[2]/div/div/table/tbody/tr/td').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="lookupInput"]/option[27]').click()
    time.sleep(1)


    elem2 = driver.find_element(By.XPATH, '//*[@id="lay"]/div[2]/div[2]/div[13]/div[2]/input')
    elem2.clear()
    elem2.send_keys(vetor[i][1])
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="lay"]/div[2]/div[2]/div[12]/div/table/tbody/tr/td').click()

    time.sleep(4)


    for handle in driver.window_handles:
        print(handle)


    driver.switch_to.window(main_page)
    time.sleep(2)

    element = driver.find_element(By.XPATH, '//*[@id="grid741909.data.item:0.item:2"]').text
    status = driver.find_element(By.XPATH, '//*[@id="grid741909.data.item:0.item:4"]').text
    #driver.find_element(By.XPATH, '//*[@id="formsmenu248"]/li').click

    #driver.find_element(By.ID, 'side_nav').click()


    #driver.find_element(By.XPATH, '//*[@id="menu_info"]/ul/li[3]/a').click()

    #time.sleep(5) # Let the user actually see something!

    #elem1 = driver.find_element(By.XPATH, '//*[@id="username"]')

    #elem1.clear()
    #elem1.send_keys('eldio.cortez.700')


    #elem2 = driver.find_element(By.XPATH, '//*[@id="password"]')

    #elem2.clear()
    #elem2.send_keys('xozh=X9NwFAK')


    #driver.find_element(By.XPATH, '//*[@id="login-form"]/button').click()

    #time.sleep(10)
    #driver.click(driver.find_element(By.XPATH, '//*[@id="formsmenu248"]/li'))

    #driver.find_element(By.XPATH, '//*[@id="j_id_jsp_191874576_1"]/table/tbody/tr/td/table/tbody/tr[2]/td[4]/a').click()

    #time.sleep(10)



    #time.sleep(5)
    #select.select_by_visible_text('Consultar Minhas Notas')

    #driver.find_element(By.XPATH, '//*[@id="cmSubMenuID1"]/table/tbody/tr[1]/td[2]').click()


    #search_box.click()

    #search_box.submit()

    time.sleep(10) # Let the user actually see something!

    nome_do_arquivo = '20230147136' + '.txt'
    registrar = False
    try:
        arquivo = open(nome_do_arquivo, 'x')
        registrar = True
    except:
        arquivo = open(nome_do_arquivo)
        for line in arquivo:
            if line == element:
                print("Não houve atualização")
                registrar = False
            else:
                print("Nova entrada será registrada...")
                registrar = True

    arquivo.close()

    if (registrar):
        arquivo = open(nome_do_arquivo, 'w')
        arquivo.write(element)

                
    arquivo.close()
    #csv

    nome_do_arquivocsv = '20230147136' + '.csv'
    registrar = False
    try:
        arquivo = open(nome_do_arquivocsv, 'x')
        registrar = True
    except:
        arquivo = open(nome_do_arquivocsv)
        for line in arquivo:
            if line == element:
                print("Não houve atualização")
                registrar = False
            else:
                print("Nova entrada será registrada...")
                registrar = True

    arquivo.close()

    hora = str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec)
    data = str(time.localtime().tm_mday) + "/" + str(time.localtime().tm_mon) + "/" + str(time.localtime().tm_year)
    print(data + "   " +hora)

    if (registrar):
        arquivo = open(nome_do_arquivocsv, 'w')
        arquivo.write('matricula,status,dataatualizacao,nomecliente\n')
        arquivo.write(vetor[i][0]+','+status+','+element+','+vetor[i][2]+'\n')
        arquivo.write("Última atualização: " + data + "   "+hora+'\n')

                
    arquivo.close()


    #arquivo = open(nome_do_arquivo, 'w')

    #arquivo.write('Última atualização: ' + element)

    driver.quit()

