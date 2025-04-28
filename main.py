import telegram
import random
import schedule
import time
import threading
import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telegram.Bot(token=TOKEN)

temas = [
    {"tema": "Introdução ao C++", "aula": "C++ é uma linguagem de programação de propósito geral que surgiu em 1983. É conhecida por seu desempenho e controle fino de recursos."},
    {"tema": "Configuração do Ambiente", "aula": "Para programar em C++https://github.com/piupepe/Estudos_bot/new/main, você precisa de um editor de código e um compilador como GCC ou Visual Studio."},
    {"tema": "Sintaxe Básica", "aula": "Em C++, cada instrução termina com um ponto e vírgula. Funções são declaradas com tipos de retorno e blocos são delimitados por chaves {}."},
    {"tema": "Arduino Básico", "aula": "Arduino é uma plataforma de prototipagem eletrônica baseada em hardware e software fáceis de usar."},
    {"tema": "Primeiro Programa em Arduino", "aula": "No Arduino, seu primeiro código provavelmente será o 'Blink', que pisca um LED. Use funções setup() e loop()."},
    {"tema": "Variáveis em Programação", "aula": "Variáveis armazenam valores que podem mudar ao longo da execução. Em C++ você define o tipo antes do nome."},
    {"tema": "Estruturas de Controle", "aula": "Comandos como if, else, while e for permitem tomar decisões ou repetir ações no programa."}
]

def enviar_mensagem():
    tema = random.choice(temas)
    mensagem = f"**Tema:** {tema['tema']}\n\n{tema['aula']}"
    bot.send_message(chat_id=CHAT_ID, text=mensagem, parse_mode=telegram.constants.ParseMode.MARKDOWN)

def agendar_envios():
    for _ in range(5):  # 5 mensagens por dia
        schedule.every(random.randint(1, 12)).hours.do(enviar_mensagem)

def rodar_agenda():
    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    agendar_envios()
    thread = threading.Thread(target=rodar_agenda)
    thread.start()
  
