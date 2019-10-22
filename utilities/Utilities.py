from utilities.XLUtils import *

chromepath = "C:\Softwares&Drivers\WebDriver\chromedriver_win32\chromedriver.exe"
iepath = "C:\Softwares&Drivers\WebDriver\IEDriverServer.exe"
path = "C:/Users/HEM/PycharmProjects/Qfund/QfundTestData.xlsx"

############### Pages Data #############################################
url = readData(path, "LoginPage", 2, 1)
username = readData(path, "LoginPage", 2, 2)
password = readData(path, "LoginPage", 2, 3)
storeid = readData(path, "LoginPage", 2, 4)
############### Registration Data #######################################
ssn1 = readData(path, "Registration", 2, 1)
photoidnbr = readData(path, "Registration", 2, 2)
accountnbr = readData(path, "Registration", 2, 3)
ssn2 = readData(path, "Registration", 2, 4)
ssn3 = readData(path, "Registration", 2, 5)
state = readData(path, "Registration", 2, 6)
payfreq = readData(path, "Registration", 2, 7)
netincome = readData(path, "Registration", 2, 8)
grossincome = readData(path, "Registration", 2, 9)
birth_year = "1980"
dl_expiry_year = "2030"
pay_stub_year = "2019"
date = "01"
productname = readData(path, "NewLoan", 2, 1)

