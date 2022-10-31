# Aluno: Leonardo Ikeda

"""
Sua tarefa será  gerar a matriz termo documento, dos documentos recuperados da internet e
imprimir esta matriz na tela. Para tanto:
a) Considere que todas as listas de sentenças devem ser transformadas em listas de vetores,
onde cada item será uma das palavras da sentença.
b) Todos  os  vetores  devem  ser  unidos  em  um  corpus  único  formando  uma  lista  de  vetores,
onde cada item será um lexema.
c) Este único corpus será usado para gerar o vocabulário.
d) O  resultado  esperado  será  uma  matriz  termo  documento  criada  a  partir  da  aplicação  da
técnica bag of Words em todo o corpus.
"""

from bs4 import BeautifulSoup
import requests
import spacy
import numpy as np
import pandas as pd
import re

nlp = spacy.load("en_core_web_sm")


def adiciona_site(site, lsentencas):
    html = requests.get(site)
    soap = BeautifulSoup(html.content, 'html.parser')
    text=soap.get_text()
    token=re.findall('\w+', text)

    for word in token:
      lsentencas.append(word.lower())
    return lsentencas

lsentencas = []
sentencas1 = adiciona_site("https://en.wikipedia.org/wiki/Natural_language_processing", lsentencas)
sentencas2 = adiciona_site("https://www.ibm.com/cloud/learn/natural-language-processing", lsentencas)
sentencas3 = adiciona_site("https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html", lsentencas)
sentencas4 = adiciona_site("https://builtin.com/data-science/high-level-guide-natural-language-processing-techniques", lsentencas)
sentencas5 = adiciona_site("https://deepsense.ai/a-business-guide-to-natural-language-processing-nlp/", lsentencas)


bow = pd.DataFrame(0, index=np.arange(len(lsentencas)), columns=lsentencas)


def bowsum(bow):
    count = 0
    for i in lsentencas:
        bow.at[count, i] += 1
        count += 1
    return bow


newbow = bowsum(bow)
newbow
