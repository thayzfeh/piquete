import requests
from bs4 import BeautifulSoup
import re
import turma

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

# 3. Busca
data = {
    't': 'alunos',
    'nome': '',
    'amigos': 'f',
    'id_oferecimento': '374148',
    'tpres': '1',
    'p': '1',
    'buscar': '',
}

response = session.post(
    'https://grade.daconline.unicamp.br/ajax/busca.php',
    data=data,
    headers={
        'X-CSRFP-TOKEN': cookies["csrfptoken"],
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://grade.daconline.unicamp.br/oferecimento/374148/',
    }
)

print(response.status_code)
print(turma.get_courses_page(response))