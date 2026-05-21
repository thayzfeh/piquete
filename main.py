import requests

def gen_cookies():
    with open('cookies.txt','r') as file:
        content = file.read()
        content = content.split()    
        return {
            "gdes" : content[0],
            "gde_token" : content[1],
            "csrfptoken" : content[2]
        }

cookies = gen_cookies()

session = requests.Session()

cookies = gen_cookies()

session.cookies.update({
    'GDES' : cookies["gdes"],
    'gde_token' : cookies["gde_token"],
    'csrfptoken' : cookies["csrfptoken"]
})

response = session.get('https://grade.daconline.unicamp.br/')

print("Status:", response.status_code)

if "Thaís" in response.text:
    print("✓ Cookies funcionando, sessão ativa!")
else:
    print("✗ Não autenticado, cookies provavelmente expiraram.")