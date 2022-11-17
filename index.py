import bs4 as bs #Bibliteca utilizada para lidar com os arquivos XML vindos do SOUP que iremos extrair da Wikipedia
import urllib.request #Realizar requests no python
import re #Interpretador de expressões regulares
import nltk #Processamento e ordenação de tokens
import heapq #Ordenação de arrays

#Extração de dados da web, utilizamos Wikipedia pela pratica em sala
source = urllib.request.urlopen("https://en.wikipedia.org/wiki/Xenomorph_(band)").read()

#Extração de arquivos de XML para o formato de texto
soup = bs.BeautifulSoup(source,'lxml')
text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

#Removeremos caracteres indesejados vindos da Wikipedia como numerações, etc. e os lematizamos
text = re.sub(r'[[0-9]*]',' ', text)
text = re.sub(r's+',' ', text)

clean_text = text.lower()
clean_text = re.sub(r'W', ' ', clean_text)
clean_text = re.sub(r'd', ' ', clean_text)
clean_text = re.sub(r's+', ' ', clean_text)

#Realizada a tokenização para a manipulação de dados
sentences = nltk.sent_tokenize(clean_text)
stop_words = nltk.corpus.stopwords.words('english')
print(clean_text)

#Usar os dados pré processados para contarmos a frequencia das palavras
word2count = {}
for word in nltk.word_tokenize(clean_text):
    if word not in stop_words:
      if word not in word2count.keys():
         word2count[word] = 1
      else:
         word2count[word] += 1 #conta a frequência das palavras
         for key in word2count.keys():
            word2count[key] = word2count[key] /max(word2count.values()) #transforma em porcentagem

#De acordo com a frequencia as palavras serão pontuadas
sent2score = {}

for sentence in sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word2count.keys():
            if len(sentence.split(' ')) < 30:
                if sentence not in sent2score.keys():
                    sent2score[sentence] = word2count[word]
                else:
                    sent2score[sentence] += word2count[word]

#As sentenças de palavras com pontuações mais altas serão utilizadas para ordenação
best_sentences = heapq.nlargest(10, sent2score,key=sent2score.get)

print("-------------------------------------------------------------")
for sentence in best_sentences:
    print(sentence)