import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from capmonster_python import RecaptchaV2Task, ImageToTextTask
import threading 
import phone_iso3166.country as countries
import time
import phonenumbers  , random , os
from selenium.webdriver.common.proxy import Proxy, ProxyType
from colorama import Fore,Style,init

help_ = '''<h1 id="ap_cnep_header" class="a-spacing-small">
  
    
    
      Connexion et sécurité
    
  
</h1>'''

countries_dic = {'Afghanistan +93':0,
'Afrique du Sud +27':1,
'Albanie +355':2,
'Algérie +213':3,
'Allemagne +49':4,
'Andorre +376':5,
'Angola +244':6,
'Antigua-et-Barbuda +1':7,
'Arabie saoudite +966':8,
'Argentine +54':9,
'Arménie +374':10,
'Aruba +297':11,
'Australie +61':12,
'Autriche +43':13,
'Azerbaïdjan +994':14,
'Bahamas +1':15,
'Bahreïn +973':16,
'Bangladesh +880':17,
'Barbade +1':18,
'Belgique +32':19,
'Belize +501':20,
'Bermudes +1':21,
'Bhoutan +975':22,
'Biélorussie +375':23,
'Bolivie +591':24,
'Bosnie-Herzégovine +387':25,
'Botswana +267':26,
'Brunéi Darussalam +673':27,
'Brésil +55':28,
'Bulgarie +359':29,
'Burkina Faso +226':30,
'Burundi +257':31,
'Bénin +229':32,
'Cambodge +855':33,
'Cameroun +237':34,
'Canada +1':35,
'Cap-Vert +238':36,
'Chili +56':37,
'Chine +86':38,
'Chypre +357':39,
'Colombie +57':40,
'Comores +269':41,
'Congo-Brazzaville +242':42,
'Congo-Kinshasa +243':43,
'Corée du Nord +850':44,
'Corée du Sud +82':45,
'Costa Rica +506':46,
'Croatie +385':47,
'Cuba +53':48,
'Curaçao +599':49,
'Côte d’Ivoire +225':50,
'Danemark +45':51,
'Djibouti +253':52,
'Dominique +1':53,
'El Salvador +503':54,
'Espagne +34':55,
'Estonie +372':56,
'Fidji +679':57,
'Finlande +358':58,
'France +33':59,
'Gabon +241':60,
'Gambie +220':61,
'Ghana +233':62,
'Gibraltar +350':63,
'Grenade +1':64,
'Groenland +299':65,
'Grèce +30':66,
'Guadeloupe +590':67,
'Guam +1':68,
'Guatemala +502':69,
'Guinée +224':70,
'Guinée équatoriale +240':71,
'Guinée-Bissau +245':72,
'Guyana +592':73,
'Guyane française +594':74,
'Géorgie +995':75,
'Haïti +509':76,
'Honduras +504':77,
'Hong Kong +852':78,
'Hongrie +36':79,
'Inde +91':80,
'Indonésie +62':81,
'Irak +964':82,
'Iran +98':83,
'Irlande +353':84,
'Islande +354':85,
'Israël +972':86,
'Italie +39':87,
'Jamaïque +1':88,
'Japon +81':89,
'Jordanie +962':90,
'Kazakhstan +7':91,
'Kenya +254':92,
'Kirghizistan +996':93,
'Kiribati +686':94,
'Kosovo +383':95,
'Koweït +965':96,
'La Réunion +262':97,
'Laos +856':98,
'Lesotho +266':99,
'Lettonie +371':100,
'Liban +961':101,
'Libye +218':102,
'Libéria +231':103,
'Liechtenstein +423':104,
'Lituanie +370':105,
'Luxembourg +352':106,
'Macao +853':107,
'Macédoine +389':108,
'Madagascar +261':109,
'Malaisie +60':110,
'Malawi +265':111,
'Maldives +960':112,
'Mali +223':113,
'Malte +356':114,
'Maroc +212':115,
'Martinique +596':116,
'Maurice +230':117,
'Mauritanie +222':118,
'Mexique +52':119,
'Moldavie +373':120,
'Monaco +377':121,
'Mongolie +976':122,
'Montserrat +1':123,
'Monténégro +382':124,
'Mozambique +258':125,
'Myanmar +95':126,
'Namibie +264':127,
'Nauru +674':128,
'Nicaragua +505':129,
'Niger +227':130,
'Nigéria +234':131,
'Niue +683':132,
'Norvège +47':133,
'Nouvelle-Calédonie +687':134,
'Nouvelle-Zélande +64':135,
'Népal +977':136,
'Oman +968':137,
'Ouganda +256':138,
'Ouzbékistan +998':139,
'Pakistan +92':140,
'Palaos +680':141,
'Panama +507':142,
'Papouasie-Nouvelle-Guinée +675':143,
'Paraguay +595':144,
'Pays-Bas +31':145,
'Pays-Bas caribéens +599':146,
'Philippines +63':147,
'Pologne +48':148,
'Polynésie française +689':149,
'Porto Rico +1':150,
'Portugal +351':151,
'Pérou +51':152,
'Qatar +974':153,
'Roumanie +40':154,
'Royaume-Uni +44':155,
'Russie +7':156,
'Rwanda +250':157,
'République centrafricaine +236':158,
'République dominicaine +1':159,
'République tchèque +420':160,
'Saint-Christophe-et-Niévès +1':161,
'Saint-Marin +378':162,
'Saint-Martin (partie néerlandaise) +1':163,
'Saint-Pierre-et-Miquelon +508':164,
'Saint-Vincent-et-les-Grenadines +1':165,
'Sainte-Lucie +1':166,
'Samoa +685':167,
'Samoa américaines +1':168,
'Sao Tomé-et-Principe +239':169,
'Serbie +381':170,
'Seychelles +248':171,
'Sierra Leone +232':172,
'Singapour +65':173,
'Slovaquie +421':174,
'Slovénie +386':175,
'Somalie +252':176,
'Soudan +249':177,
'Soudan du Sud +211':178,
'Sri Lanka +94':179,
'Suisse +41':180,
'Suriname +597':181,
'Suède +46':182,
'Swaziland +268':183,
'Syrie +963':184,
'Sénégal +221':185,
'Tadjikistan +992':186,
'Tanzanie +255':187,
'Taïwan +886':188,
'Tchad +235':189,
'Territoires palestiniens +970':190,
'Thaïlande +66':191,
'Timor oriental +670':192,
'Togo +228':193,
'Tonga +676':194,
'Trinité-et-Tobago +1':195,
'Tunisie +216':196,
'Turkménistan +993':197,
'Turquie +90':198,
'Tuvalu +688':199,
'Ukraine +380':200,
'Uruguay +598':201,
'Vanuatu +678':202,
'Venezuela +58':203,
'Vietnam +84':204,
'Yémen +967':205,
'Zambie +260':206,
'Zimbabwe +263':207,
'Égypte +20':208,
'Émirats arabes unis +971':209,
'Équateur +593':210,
'Érythrée +291':211,
'États fédérés de Micronésie +691':212,
'États-Unis +1':213,
'Éthiopie +251':214,
'Île Norfolk +672':215,
'Îles Caïmans +1':216,
'Îles Cook +682':217,
'Îles Féroé +298':218,
'Îles Malouines +500':219,
'Îles Marshall +692':220,
'Îles Salomon +677':221,
'Îles Turques-et-Caïques +1':222,
'Îles Vierges britanniques +1':223,
'Îles Vierges des États-Unis +1':224,
'Îles Åland +358':225}

class bot():
    def __init__(self,email,password,number,mode,mode_pro,proxy,count):
        self.mode_proxy = mode_pro
        self.proxy = proxy
        self.number = number
        self.mode = mode
        self.email,self.password = email,password
        self.count = count

        self.random_numbers = random.sample(range(1000), 1)
        captcha = open('captcha.txt').read()
        self.solver = TwoCaptcha(captcha)

    def start(self):
        # Setup The Browser
        if self.mode_proxy == 1:
            if self.mode == 1:    
                self.options = webdriver.ChromeOptions()    
                self.options.add_argument("start-maximized")
                self.options.add_argument('--headless')
                self.options.add_argument('--disable-gpu')
                proxy = Proxy()
                proxy_ip_port = self.proxy
                proxy.proxy_type = ProxyType.MANUAL
                proxy.http_proxy = proxy_ip_port
                proxy.ssl_proxy = proxy_ip_port
                capabilities = webdriver.DesiredCapabilities.CHROME
                proxy.add_to_capabilities(capabilities)
                self.options = webdriver.ChromeOptions()    
                
            elif self.mode == 2:
                self.options = webdriver.ChromeOptions()    
                proxy = Proxy()
                proxy_ip_port = self.proxy
                proxy.proxy_type = ProxyType.MANUAL
                proxy.http_proxy = proxy_ip_port
                proxy.ssl_proxy = proxy_ip_port
                capabilities = webdriver.DesiredCapabilities.CHROME
                proxy.add_to_capabilities(capabilities)
                self.options = webdriver.ChromeOptions()    

            self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
            browser = webdriver.Chrome(desired_capabilities=capabilities,options=self.options)
            browser.get('https://www.amazon.fr/ap/cnep?openid.return_to=https%3A%2F%2Fwww.amazon.fr%2Fyour-account&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=frflex&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

        elif self.mode_proxy == 2:
            if self.mode == 1:    
                self.options = webdriver.ChromeOptions()    
                self.options.add_argument("start-maximized")
                self.options.add_argument('--headless')
                self.options.add_argument('--disable-gpu')
                self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
                
            elif self.mode == 2:
                self.options = webdriver.ChromeOptions()    
                self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
            browser = webdriver.Chrome(options=self.options)
            browser.get('https://www.amazon.fr/ap/cnep?openid.return_to=https%3A%2F%2Fwww.amazon.fr%2Fyour-account&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=frflex&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
        
        
        if self.login_form(browser):
            self.check_captcha(browser)
            try:
                os.remove(f'module\chaptcha{self.random_numbers}.png')
            except:
                pass    
    def login_form(self,browser):
        self.browser = browser
        browser.implicitly_wait(10)
        try:
            self.browser.find_element(By.NAME, 'email').send_keys(self.email)
            self.browser.find_element(By.ID, 'continue').click()
            self.browser.find_element(By.NAME, 'password').send_keys(self.password)
            self.browser.find_element(By.ID, 'signInSubmit').click()
            return True
        except:
            print('[!] Error For Login')
            return False

    def check_captcha(self,browser):
        self.browser = browser
        try:
            browser.implicitly_wait(2)
            self.browser.find_element(By.ID, 'auth-captcha-image')
            self.browser.find_element(By.NAME, 'password').send_keys(self.password)
            self.solve_captcha(browser)
            return True
        except:
            if help_ in self.browser.page_source:
                print(Fore.LIGHTWHITE_EX+'[+] Login Done')
                self.start_call(self.browser)
            return False

    def fullter_number(self,num):
        test = "+" + str(num)
        x = phonenumbers.parse(test)
        phone_number = x.national_number
        country_code = x.country_code
        country_name = countries.phone_country(test)
        phonenumber = str(phone_number)
        x = '+20'
        for i in countries_dic.keys():
            if x in i:
                return countries_dic[i]+1,phonenumber
            
    def start_call(self,browser):
        self.browser = browser
        try:
            for i in range(int(self.count)):
                def get_number():
                    with open('numbers.txt','r') as ff:
                        one = ff.read().splitlines()
                    number = one[0]
                    numbers = one[1:]
                    with open('numbers.txt','w') as num:
                        for i in numbers:
                            num.write(i+'\n')
                        num.write(number+'\n')
                    return number
                num = get_number()
                id_country,phone = self.fullter_number(num)
                try:
                    self.browser.get('https://www.amazon.fr/ap/profile/mobilephone?appActionToken=lzZQPO2Uej2FqJYpbedj2BQFAkKrq2wj3D&appAction=CHANGE_MOBILE_PHONE&openid.return_to=ape%3AaHR0cHM6Ly93d3cuYW1hem9uLmZyL3lvdXItYWNjb3VudA%3D%3D&prevRID=ape%3ASDdFSkZNWkU5VEdLQzFIMDZXRlc%3D&email=ape%3AbW9oYW0ubWVkMTIuMzIwMDNtQGdtYWlsLmNvbQ%3D%3D&workflowState=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.nse3jkcdC7lqZk5VRLd3w00A3DgRrRt5zzcgNj3eFfYPcMLxo6Iu2g.9Pw0i7QaDd4Cpq6M.A8ORiQ4t4hcRVY5vYEDII0s5PpYhgMbGuPXX45g9WLY-EbGj2KVAIeMZd_n2Y-bTi0zJWON72OEAQyoAa4FcKlWjTlxNGosq-TPwcKirP0vEJhUlrS20KhdmJB6_Rvexqdqrg6PUEcn1QMmQD5JIosEcAkzecD2NefKyyxlT6FQIrZ2Pne5MvWkgp-mZnOzlUqch5RGVp2a0vex7czqcx0h2-_crS6iO7CJZTX6im97sgCbnguVZkKXV-9r3vs8HIik66G1ddgtMUDQzmjDhuDOl5HraBehr9APkepsZZqnKBBS3Vk8dj-9aRFa2oQq8S_utJWwuQGTEFd_XvHNFuYxtlPZCUsyETj-Ymvc8TsLEAQsjRYVj_UFO-3ENRjM7Bc38nfh2rzvYjFbS-yZq1aDWYNZZtw-ML6aCuGHOAuzLQ2QbCunDpkWjO5pBP2-T0JYt5qPkUN1k_97Qwf9cDP-o9lbqJ3O4kZ-fk-dzWVdB789PMd-zqb_keSSQbymY_XiLeG-eqq-42qkoK3RkM_qF0h1vGU-HRoxmKieYOB1O7OaQ7iffqb7gC_fo8YhbzXGEGX5e6e6qYFIfaecYql9qMeTNpbxopNxldCCDwcjb7pkC1jOYqVS3IHhGJDj87gIfBl01fzMjNNdD7ag9opM.5ItnTt63ZPEFwsB5232wcw&referringAppAction=CNEP')
                    self.browser.implicitly_wait(3.5)
                    self.browser.find_element(By.ID, 'ap_phone_number').send_keys(phone)
                    #open menu
                    self.browser.find_element(By.ID, 'a-autoid-0-announce').click()
                    self.browser.find_element(By.XPATH, f'//*[@id="a-popover-1"]/div/div/ul/li[{id_country}]').click()
                    self.browser.find_element(By.ID, 'auth-continue').click()
                    time.sleep(0.5)
                    self.browser.find_element(By.XPATH, '//*[@id="a-popover-content-2"]/div[4]/div[2]').click()
                    try:
                        self.browser.find_element(By.NAME, 'code')
                        print(Fore.GREEN+f'{num} Success')
                    except:
                        print(Fore.RED+f'{num} Failed')
                except:
                    pass
        except:
            print('[ Error To Find Call Button ]')

    def solve_captcha(self, browser):
        self.browser = browser
        try:
            # Save captcha image
            path = f'module\chaptcha{self.random_numbers}.jpeg'
            self.browser.implicitly_wait(5)
            image = self.browser.find_element(By.XPATH, '//*[@id="auth-captcha-image"]').get_attribute('src')
            imgdata = requests.get(image)
            with open(path, 'wb') as file:
                file.write(imgdata.content)

            task = ImageToTextTask(path, client_key='your_capmonster_api_key')  # Replace with your CapMonster API key
            task.create_task()

            # Poll for captcha solution
            solution = task.join()
            if solution.get('errorId') is None:
                captcha_text = solution.get('solution').get('text')
                self.browser.find_element(By.XPATH, '//*[@id="auth-captcha-guess"]').send_keys(captcha_text)
                self.browser.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()
                self.check_captcha()
            else:
                print(f'[Error] Captcha solving failed: {solution.get("errorCode")} - {solution.get("errorDescription")}')
        
        except Exception as e:
            print(f'[Error] Failed to solve captcha: {e}')

    def check_captcha(self):
        # Add your logic to check if captcha was successfully passed
        pass
def get_number():
    with open('numbers.txt','r') as ff:
        one = ff.read().splitlines()
    number = one[0]
    numbers = one[1:]
    with open('numbers.txt','w') as num:
        for i in numbers:
            num.write(i+'\n')
        num.write(number+'\n')
    return number

def get_account():
    with open('accounts.txt','r') as ff:
        one = ff.read().splitlines()
    number = one[0]
    numbers = one[1:]
    with open('accounts.txt','w') as num:
        for i in numbers:
            num.write(i+'\n')
    return number

def get_proxy():
    # Proxy
    with open('proxy.txt','r') as pr:
        proxiesss = pr.read().splitlines()
    proxy = proxiesss[0]
    proxies = proxiesss[1:]
    with open('proxy.txt','w') as pro:
        for proxyy in proxies:
            pro.write(proxyy+'\n')
        pro.write(proxy+'\n')
    return proxy

def intro():
    print(Fore.GREEN + '''
██ ██████   ██████  ██████   ██████  ██████   █████  
██      ██ ██       ██   ██ ██    ██ ██   ██ ██   ██ 
██  █████  ███████  ██████  ██    ██ ██   ██ ███████ 
        ██ ██    ██ ██   ██ ██    ██ ██   ██ ██   ██ 
██ ██████   ██████  ██████   ██████  ██████  ██   ██ 
                                                                                             
''')
    
    print(Fore.RED + 'MUSTAFA NASSER - Whattsapp [+201098974486]'+Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX)

if __name__ == '__main__':
    intro()
    try:
        browser_num = int(input('[ Number of browsers ]\n<> '))
        x = open('numbers.txt','r').read().splitlines()
        mode = int(input('[ Browser Headless ==> 1 ]\n[ Browser Non Headless ==> 2 ]\n<> '))
        prox = int(input('[ Browser Proxy ==> 1 ]\n[ Browser Non Proxy ==> 2 ]\n<> '))
        phone = int(input('[ Call for one account ]\n<> '))
        if len(x) % browser_num == 0:
            count_ = (len(x) // browser_num)
        else:
            count_ = (len(x) // browser_num) + 1
        for i in range(count_):
            threads = []
            for i in range(browser_num):
                if len(x) == 0 :
                    break
                num = get_number()
                accccs = get_account().split(':')
                mail = accccs[0]
                password = accccs[1]
                proxy = get_proxy()
                s = bot(mail,password,num,mode,prox,proxy,phone)
                t = threading.Thread(target=s.start,args=())
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        input(f'PRESS ENTER TO EXIT')        
    except Exception as e:
        print(e)
        input(f'PRESS ENTER TO EXIT')
