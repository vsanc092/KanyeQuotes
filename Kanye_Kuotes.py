import requests
import random
import telebot
from bs4 import BeautifulSoup as b

URL = 'https://github.com/ajzbc/kanye.rest/blob/master/quotes.json'
API = '5975959258:AAF7gmkM7KFvB54H6FWMur7unkaobFOEd dE'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    quotes = soup.find_all('span', class_='pl-s')
    return [c.text for c in quotes]

list_of_quotes = parser(URL)
random.shuffle(list_of_quotes)

bot = telebot.TeleBot(API)
@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, 'Enter any number 0-9:')

@bot.message_handler(content_types=['text'])
def quotes(message):
    if message.text.lower() in '0123456789':
        bot.send_message(message.chat.id, 'Kanye says:')
        bot.send_message(message.chat.id, list_of_quotes[0])
        del list_of_quotes[0]
    else:
        bot.send_message(message.chat.id, 'Try ANOTHER one:')
bot.polling()
