import httpx
import asyncio
from bs4 import BeautifulSoup
import re
import turma
from manage_requests import fetch

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

base_url = "grade.daconline.unicamp.br"

async def main():

    cookies = gen_cookies()

    data = {
    't': 'alunos',
    'nome': '',
    'amigos': 'f',
    'id_oferecimento': '374148',
    'tpres': '1',
    'p': '1',
    'buscar': '',
    }

    async with httpx.AsyncClient() as client:

        client.cookies.set('GDES', cookies['gdes'], domain =base_url)
        client.cookies.set('gde_token',cookies['gde_token'],domain=base_url)
        client.cookies.set('csrfptoken',cookies['csrfptoken'],domain=base_url)

        response = await fetch(client, data, 'https://grade.daconline.unicamp.br/oferecimento/374148/')
        


#session.cookies.update({
#    'GDES' : cookies["gdes"],
#    'gde_token' : cookies["gde_token"],
#    'csrfptoken' : cookies["csrfptoken"]
#})

# 3. Busca


#response = session.post(
#    'https://grade.daconline.unicamp.br/ajax/busca.php',
#    data=data,
#    headers={
#        'X-CSRFP-TOKEN': cookies["csrfptoken"],
#        'Referer': 'https://grade.daconline.unicamp.br/oferecimento/374148/',
#    }
#)
#response = fetch(session, data, 'https://grade.daconline.unicamp.br/oferecimento/374148/')

#print(response.status_code)
#print(turma.get_courses_page(response))
asyncio.run(main())