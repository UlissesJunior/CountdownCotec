from calendar import month
import time
import tweepy
import os

from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

api = tweepy.Client(
    consumer_key= CONSUMER_KEY or os.getenv("CONSUMER_KEY"),
    consumer_secret=  CONSUMER_SECRET or os.getenv("CONSUMER_SECRET"),
    access_token= ACCESS_TOKEN or os.getenv("ACCESS_TOKEN"),
    access_token_secret= ACCESS_TOKEN_SECRET or os.getenv("ACCESS_TOKEN_SECRET")
)

x = time.localtime()
year = x[0]
month = x[1]
day = x[2]

d1 = datetime.strptime(str(year)+'-'+str(month)+'-'+str(day), '%Y-%m-%d')
d2 = datetime.strptime('2022-12-03', '%Y-%m-%d')
counter = abs((d2 - d1).days)

restante = ""
if year == 2022:
    if month == 9:
        if day == 19:
            restante = "Início da Semana de Provas do 3º Bimestre 🙏🏻"
        if day == 20:
            restante = "Dia 2 da Semana de Provas do 3º Bimestre 🙏🏻"
        if day == 21:
            restante = "Dia 3 da Semana de Provas do 3º Bimestre 🙏🏻"
        if day == 22:
            restante = "Dia 4 da Semana de Provas do 3º Bimestre 🙏🏻"
        if day == 23:
            restante = "Fim da Semana de Provas do 3º Bimestre 🙏🏻\n Menos pra Mec que tem prova no sábado 🤣🤣🤣"
        if day == 26:
            restante = "Começou o último bimestre, graças a deus fml🥳"
    if month == 10:
       
        if day == 12:
            restante = "Hoje você não vai pra escola, é feriado da padroeira 🙏🏻"
        if day == 15:
            restante = "É sábado? Sim, mas hoje tem porta abertas, levanta dessa cama e vai mostrar que o seu curso é melhor que o do amiguinho  ⚙️⚡🤖🔌"
        if day == 24:
            restante = "Chegou a semana de saco cheio 🥳🥳🥳 \n Aproveita pra estudar, eu sei que você tá devendo nota pro Areco 🤣"
        if day == 25:
            restante = "Dia 2 da semana de saco cheio"
        if day == 26:
            restante = "Dia 3 da semana de saco cheio"
        if day == 27:
            restante = "Dia 4 da semana de saco cheio"
        if day == 28:
            restante = "Dia 5 da semana de saco cheio"
        if day == 29:
            restante = "Acabou a semana de saco cheio, aproveita o domingo amanhã que as aula vão voltar daqui 2 dias!"
        if day == 31:
            restante = "Olá novamente, volta pra escola, os dias de glória acabaram senhor"
    if month == 11:
        if day == 2:
            restante = "Tão sabotando as quartas, hoje você não vai pra escola dnv, feriado de finados 🙏🏻" 
        if day == 7:
            restante = "Começou a semana de tecnologia 🤖"
        if day == 8:
            restante = "Dia 2 da semana de tecnologia 🤖"
        if day == 9:
            restante = "Dia 3 da semana de tecnologia 🤖"
        if day == 10:
            restante = "Dia 3 da semana de tecnologia 🤖"
        if day == 11:
            restante = "Acabou a semana de tecnologia 🤖"
        if day == 14:
            restante = "Que vidinha mole ein, feriado de amanhã imendou com o de hoje, sorte pra alguns e tristeza pra quem foi pro Enem ontem e vai pra Unesp amanhã fazer prova 🤣"
        if day == 15:
            restante = "Proclamação da República salvando no feriado \n Boa sorte pra quem for fazer a prova da UNESP!"
        if day == 21:
            restante= "Isso mesmo, você fez o Enem ontem, mas hoje já começa a última semana de provas do ano, azar o seu, quem mandou estudar no cotec 🤣"
        if day == 22:
            restante= "Dia 2 da semana de provas do 4º Bimestre"
        if day == 23:
            restante= "Dia 3 da semana de provas do 4º Bimestre"
        if day == 24:
            restante= "Dia 4 da semana de provas do 4º Bimestre"
        if day == 25:
           restante = "APITA O JUIZ!! Fim de jogo pra você que passou em tudo, aproveite suas férias ou sua vida de desempregado se você for do 3°. \n Quem não passou direto, ergue essa cabeça que semana que vem tem recuperação bimestral, eu confio mlk, vai que dá!!"
        if day == 28:
            restante= "Começou a última rec bimestral, vamo rpzd, ergue essa cabeça e gabarita essas provas aí 🫡"
        if day == 29:
            restante= "Dia 2 da semana de recuperação bimestral"
        if day == 30:
            restante= "Dia 3 da semana de recuperação bimestral"
    if month == 12:
        if day == 1:
            restante = "Dia 4 da semana de recuperação bimestral"
        if day == 2:
            restante = "Dia 5 da semana de recuperação bimestral"
        if day == 3:
            restante = "Fim do segundo tempo!! \n Você que passou na rec bimestral, parabéns!! Aproveite o restinho do ano agora. \n Você que ainda não passou, levanta dessa cama, não fica triste, estuda e vai na fé, pq ainda tem a rec final 🙏🏻"

# Início do for do countdown
m = 9
i = 1
for m in range(9, 12):
    if year == 2022 and month == m:
        for i in range(1, 32):
            if day == i:
                counter_tweet = "Faltam " + \
                    str(counter) + " dias para o fim do ano letivo no Cotec"
                try:
                    tweet = api.create_tweet(
                        text=counter_tweet + "\n" + restante)
                    print(tweet)
                except:
                    print("Deu errado animal")