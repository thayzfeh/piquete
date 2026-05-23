import httpx
async def fetch(client: httpx.AsyncClient, data, referer):
    return await client.post(
        'https://grade.daconline.unicamp.br/ajax/busca.php',
        data= data,
        headers= {
            'X-CSRFP-TOKEN': client.cookies.get('csrfptoken'),
            'Referer': referer
        }
    )


