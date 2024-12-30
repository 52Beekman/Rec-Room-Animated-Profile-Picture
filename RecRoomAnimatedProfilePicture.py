''' Stuff you need to update for this to work '''
'Enter your username here'
user = 'csgroup'
'Enter your password here'
passwd = 'csgsMp17892'



image1 = 'https://media-hosting.imagekit.io//43e03334995a4948/CSG_Round.png?Expires=1735690493&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=q20n-UI5JPXqwYd9S5YtlcsONchpwUYN8LarF8C2gigFETv31VVht4h-tgoArrXGgQKY7dL~JMh-Mt1PD0AQOu0~66Tx77ILwCMkf11y4mxzMWIW0elrQaMpLLIgK~qPsWY6TipKHZZDBilCX-T8nTU0MpnPDetihigS6SXKPUXyPDPGh8AW3so6lkcryZtdR6NAXo4msgAByicx-Uq5RDtqsl5UuNSHMzkv9ytf0J4XZhm8tFl483naYVbBG8I0sMduoNwxVK7QsvHUEw0JUzO60ExwX878KyAu-j12-0~oRU8hhQq4HTpperZQZb2t-gmIOuTaFdaIPJMa8Er1Kw__'
" ^ You need to change EACH of these to whatever you want the 3 pics to be (Currently set to a waving red zigzag)"

''' Stuff that will change how the program works '''
speed = 0.2
"^ As you can probably guess, this changes how long the PFP stays on each image"

import time
try:
    import requests
except:
    print('''You do not have the requests library installed, you need to install it via the following command:
        pip install requests
    Thank you!''')
try:
    import recnetlogin as rnl
except:
    print('''You do not have the RecNetLogin package installed, you need to install it via the following command:
        python -m pip install git+https://github.com/Jegarde/RecNet-Login.git#egg=recnetlogin
    Thank you!''')

''' Just Initializing some values '''
login = rnl.login_to_recnet(username=user,password=passwd)
x = 0
BToken = ''

''' Making the strings into the format read by the rec.net image api '''
imageName1 = 'imageName=' + image1

''' Initial token request '''
BToken = login.access_token

print(BToken)

''' The loop program that actually makes the picure move '''
while 1 == 1:
    
    ''' The HTTP header for changing your In-Game pfp '''
    Headers = {'sec-ch-ua':'";Not A Brand";v="99", "Chromium";v="88"',
          'Accept' : '*/*',
          'sec-ch-ua-mobile' : '?0',
          'Authorization' : BToken,
          'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
          'Origin' : 'https://rec.net',
          'Sec-Fetch-Site' : 'same-site',
          'Sec-Fetch-Mode' : 'cors',
          'Sec-Fetch-Dest' : 'empty',
          'Referer' : 'https://rec.net/',
          'Accept-Encoding' : 'gzip, deflate',
          'Accept-Language' : 'en-US,en;q=0.9',
          }
    ''' The easy way to edit what pfp plays after what '''
    def i1():
        r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers, data = imageName1)
        print(str(r) + " num of requests: " + str(x))
        time.sleep(speed)

    ''' Requests a new auth token when that one is no longer valid '''
    r = requests.put('https://accounts.rec.net/account/me/profileImage', headers = Headers)

    if r.status_code == 401:
        print('Invalid Token')
        login = rnl.login_to_recnet(username=user,password=passwd)
        BToken = login.access_token

        print(BToken)
