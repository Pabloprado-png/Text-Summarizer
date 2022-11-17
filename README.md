A sumarização de texto é o processo de criar um texto mais curto sem remover a estrutura semântica do texto.
A ideia é pegar o texto e simplificá-lo ao máximo, mantendo sua consistência, com a finalidade de deixar mais otimizado, fazendo com que seja menos excessivo os termos utilizados. De certa forma, podemos fazer com que a sumarização para ser realizada tenha alguns preceitos, sendo eles, saber a ideia do texto para que tenhamos algo a que comparar, se faz sentido ou não. Reconhecer os padrões utilizados nos textos, para sabermos se possui pleonasmo ou não, conectivos, palavras chaves e outros. 
A sumarização de textos possui uma gama de áreas onde podemos aplicá-las, não apenas em grandes textos, mas também em frases que motores de pesquisa possam utilizar e auxiliar o texto sumarizado na procura de respostas mais precisas, apesar de sua principal função ser reduzir e resumir um texto ao máximo.

De que forma podemos fazer esta sumarização textual em uma aplicação de forma simples e sucinta? Bom, primeiro nesta atividade, nós iremos realizar da seguinte forma: 
1.	Obter dados da Web (Wikipedia);
2.	Faremos a conversão dos dados recebidos em XML pelo BeautifullSoup;
3.	Tokenização de sentenças para podermos avaliar cada palavra e sua frequência para sabermos sua importância;
4.	Construir um histograma e calcular a pontuação de cada palavra para descobrir sua frequência;
5.	As palavras com a maior frequência serão utilizadas para montarmos o escopo da frase eliminando termos inúteis.


Primeiro faremos a importação das bibliotecas utilizadas

Em seguida realizaremos a extração de dados de uma página web, sendo esta, a página da Wikipedia sobre uma banda chamada Xenomorph (Recomendamos páginas pequenas para um fim didático, mais produtivo e simples devido à demora de processamento, porém pode ser qualquer página).

Após estes passos, nós iremos realizar uma limpeza no texto extraído. Tais como retirar alguns caracteres daWikipedia, como colchetes com numerações, parágrafos e padronizar o formato dos textos como deixando todas aspalavras em minúsculo. 

Utilizaremos o texto que limpamos anteriormente e o armazenaremos em “tokens de contagem”, aos quais vamos utilizar para medir a porcentagem de vezes que estas palavras aparecem em nosso texto extraído na web.

E agora para finalizarmos, iremos “pontuar” a frequência de cada palavra utilizada no texto para assim, as palavras que tiverem a menor frequência serem removidas, e as palavras mais relevantes e de maior destaque sejam redigidas.
