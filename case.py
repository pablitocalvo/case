from lxml import html
from lxml.cssselect import CSSSelector

import requests

indirizzo='http://www.immobiliare.it/Roma/vendita_case-Roma.html?criterio=rilevanza&idMZona[]=10151&idMZona[]=10152&idMZona[]=10165'

page = requests.get(indirizzo)
# print page.text  #la pagina in formato testuale


tree = html.fromstring(page.content)  

numeroAnnunci = tree.xpath('//span[@id="annListaCounter"]/text()')[0]

print int( numeroAnnunci.replace('.',''))
numeroPagine=int( numeroAnnunci.replace('.',''))/15

## for  pagine .....

indirizzoPagina=indirizzo+"&pag="+"1"
page = requests.get(indirizzoPagina)
#print page.text 

tree = html.fromstring(page.content)
annunci = tree.xpath('//div[@class="contenuto_box nuovo_formato_vetrina"]')

print "trovati " , len(annunci), "annunci"


##  for 1 .. 15 

annuncio=annunci[14] 

#prezzo 
tagprezzo = annuncio.xpath('//span[@class="price"]')
prezzo = tagprezzo[0].xpath('child::text()')
print prezzo[0]

#link
taglink = annuncio.xpath('./div/div/div/strong/a')


print taglink[0].get('href')




print html.tostring(taglink[0])












