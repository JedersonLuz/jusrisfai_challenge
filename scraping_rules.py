from bs4 import BeautifulSoup
from requests_html import HTMLSession

class ScrapingRules(object):
    def find_titulo(self, soup):
        title = soup.find_all('table')
        title = title[-1].find_all('p')
        return title[-1].get_text().strip()

    def find_artigo(self, soup, artigo):
        results = soup.find_all('p')
        index = 0
        content = ''
        for i in range(len(results)):
            if (f'Art. {artigo}.' in results[i].get_text()) \
                or (f'Art. {artigo}º' in results[i].get_text()) \
                or (f'Art . {artigo}.' in results[i].get_text()):
                
                index, content = i, results[i].get_text()
            
            if (f'Art. {int(artigo)+1}.' in results[i].get_text()) \
                or (f'Art. {int(artigo)+1}º' in results[i].get_text()) \
                or (f'Art . {int(artigo)+1}.' in results[i].get_text()):

                return (index, content, i)

        return (0, 'Artigo não encontrado', 0)

    def find_paragrafo(self, soup, paragrafo, index, end):
        results = soup.find_all('p')
        if (end - index) > 1:
            for i in range(index, end):
                if paragrafo == '1':
                    if (f'§ {paragrafo}º' in results[i].get_text()) or ('Parágrafo único' in results[i].get_text()):
                        return (i, results[i].get_text())
                else:
                    if f'§ {paragrafo}º' in results[i].get_text():
                        return (i, results[i].get_text())
        
        return (index, '')

    def find_inciso(self, soup, inciso, index, end):
        results = soup.find_all('p')
        if (end - index) > 1:
            for i in range(index, end):
                if f'{inciso}-' in results[i].get_text() \
                    or f'{inciso} -' in results[i].get_text() \
                    or f'{inciso} –' in results[i].get_text():
                    return (i, results[i].get_text())
        
        return (index, '')

    def find_alinea(self, soup, alinea, index, end):
        results = soup.find_all('p')
        if (end - index) > 1:
            for i in range(index, end):
                if f'{alinea})' in results[i].get_text() \
                    or f'{alinea}.' in results[i].get_text() \
                    or f'{alinea} -' in results[i].get_text() \
                    or f'{alinea} –' in results[i].get_text():
                    return (i, results[i].get_text())
        
        return (index, '')

    def find_rule(self, lei, artigo, paragrafo, inciso, alinea):
        ## URL param
        url = f'http://www.planalto.gov.br/ccivil_03/leis/l{lei}.htm'

        ## Request
        print('Request initialized')
        print('Wait for a moment...')
        session = HTMLSession()
        resp = session.get(url)
        resp.html.render()

        if resp.status_code == 200:
            #print('Status code 200')

            soup = BeautifulSoup(resp.html.html, "lxml")

            print(f'Lei {lei}: {self.find_titulo(soup)}')

            index, artigo_text, end = self.find_artigo(soup, artigo)
            print(artigo_text)

            if paragrafo:
                index, paragrafo_text = self.find_paragrafo(soup, paragrafo, index, end)
                if paragrafo_text: print(paragrafo_text)

            if inciso:
                index, inciso_text = self.find_inciso(soup, inciso, index, end)
                if inciso_text: print(inciso_text)

            if alinea:
                index, alinea_text = self.find_alinea(soup, alinea, index, end)
                if alinea_text: print(alinea_text)

        else:
            print('No internet')
            print('Try:')
            print('Checking the network cables, modem, and router')
            print('Reconnecting to Wi-Fi')


## Inputs
lei = '9504'
#lei = input('Informe um número de lei: ')

artigo = '4'
#artigo = input('Informe um artigo: ')

paragrafo = ''
#paragrafo = input('Informe um parágrafo (deixe em branco para desconsirar esse argumento): ')

inciso = ''
#inciso = input('Informe um inciso (deixe em branco para desconsirar esse argumento): ').upper()

alinea = ''
#alinea = input('Informe uma alínea (deixe em branco para desconsirar esse argumento): ')

## Main
scraping_rules = ScrapingRules()
scraping_rules.find_rule(lei, artigo, paragrafo, inciso, alinea)
