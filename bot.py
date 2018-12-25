# -*- coding: utf-8 -*-
import sys
import config
import datetime
import asyncio
import threading
from time import sleep
import time
import random
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
message_with_inline_keyboard = None




def tick():
    if int(config.stamina)!=int(config.maxstamina):
        t = threading.Timer(5.0, tick)
        t.start()
        config.stamina+=1
        print(config.stamina)
async def stats(chat_id, msg):
    await bot.sendMessage(chat_id, '\u2623\ufe0f Статистика:\n\n\U0001f468\U0001f3fb\u200d\U0001f3a4 %s'% msg["from"].get("username")+'\n\U0001f396 Уровень: %s'% config.level+'\n\U0001f52e Опыт : %s'% config.exp+'/%s'% config.expto+'\n\U0001f4b5 Деньги: %s'% config.money+'\n\U0001f50b Запас сил: %s'% config.stamina+' / %s'%config.maxstamina+'\n\u23f1 Восстановление: %s'% config.timestamina+' сек'+'\n/suicide')
async def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type)

    print('Chat:', content_type, chat_type, chat_id, datetime.datetime.fromtimestamp(int(msg['date'])).strftime('(%Y-%m-%d %H:%M:%S)'))
    
    if content_type != 'text':
        if content_type == 'sticker':
            print(msg['sticker'].get('file_id'))
    elif content_type == 'text':      
        print(msg['text'].encode('unicode-escape').decode('ascii'))
        f = open('bd.txt', 'r')
        if msg['text'].lower() == '/start': 
            if f.read(1)=='1':
                dintro=' Приветствуем в Пустоши. Ты просыпаешься, сразу проверяешь обрез под подушкой. Внимательно осматриваешь местность из окна. Вчера ты нашёл этот заброшенный домик для ночлега, но долго тут оставаться не вариант, ведь запасы воды и еды не бесконечные. Выбери действие:'
                f = open('bd.txt', 'w')
                img1=open('img1.jpg','rb')
                markup = ReplyKeyboardMarkup(keyboard=[
                         ['Осмотреть шкафчики в поиске провизии'],
                         ['Не тратить время на поиски и выйти']], resize_keyboard=True)
                await bot.sendMessage(chat_id, 'Над радиационными тучами встаёт солнце...')
                await bot.sendPhoto(chat_id, photo=img1, caption='Здравствуй, %s!'% msg["from"].get("first_name")+dintro, reply_markup=markup)
                f = open('bd.txt', 'w')
                f.close()
                img1.close()
                #=============Основной цикл игры==========
                tick()
                
                
                #=========================================
            
            else:
                print(msg["from"].get("last_name"))
                if msg["from"].get("username")=="None":
                    await bot.sendMessage(chat_id, "Эй, %s!" % msg["from"].get("first_name")+' Ты ведь уже начал игру.. Хуле старт клацаешь?\U0001F44A')
                else:
                    await bot.sendMessage(chat_id, "Эй, %s!" % msg["from"].get("username")+' Ты ведь уже начал игру.. Хуле старт клацаешь?\U0001F44A')
                
                 
      
#==================================================    
        command = msg['text'].lower()
        
        if command == 'c' or msg['text'] == '\U0001f519 Назад':
            markup = ReplyKeyboardMarkup(keyboard=[
                         ['/start','/restart','/stats'],
                         ['admin','\U0001f3de Поселение','\U0001f3ec Магазин']], resize_keyboard=True)
            await bot.sendMessage(chat_id, 'Выбери действие: ', reply_markup=markup)
        elif msg['text'] == 'Ромочка':
            chat_id='624737506'
            while True:
                await bot.sendMessage(chat_id, msg['text'])
                
        #============Cюжетка=============================================
        elif msg['text'] == 'Осмотреть шкафчики в поиске провизии':
            img2=open('img2.jpg','rb')
            markup = ReplyKeyboardMarkup(keyboard=[
                         ['Засунуть руку подальше'],
                         ['Взять первые банки и уйти']], resize_keyboard=True)
            await bot.sendMessage(chat_id, 'Надеюсь, будет чем подкрепиться...')
            await bot.sendPhoto(chat_id, photo=img2, caption='Ты открываешь дверцу шкафа и видишь кучу банок с стёртыми названиями.', reply_markup=markup)
            img2.close()
        elif msg['text'] == 'Засунуть руку подальше':
            markup = ReplyKeyboardMarkup(keyboard=[
                         ['Сложить пожитки в рюкзак и уйти']], resize_keyboard=True)
            await bot.sendMessage(chat_id, 'Ничего полезного.. Срок годности некоторых продуктов закончился много лет назад, надо уходить.', reply_markup=markup)
            
        elif msg['text'] == 'Взять первые банки и уйти' or msg['text'] == 'Сложить пожитки в рюкзак и уйти':
            img5=open('img5.jpg','rb')
            markup = ReplyKeyboardMarkup(keyboard=[
                         ['Продолжить движение']], resize_keyboard=True)
            await bot.sendMessage(chat_id, 'Расставив найденное на стол, ты начинаешь проводить ревизию...')
            await bot.sendPhoto(chat_id, photo=img5, caption='\U0001f392 Рюкзак:\n\n+2 Консервы "Говяжий дошик"\n+1 Бутылка чистой воды ', reply_markup=markup)
            img5.close()
            
        elif msg['text'] == 'Не тратить время на поиски и выйти' or msg['text'] == 'Продолжить движение':
            img3=open('img3.jpg','rb')
            markup = ReplyKeyboardMarkup(keyboard=[
                         ['Подойти ближе, чтоб разглядеть врага'],
                         ['Потихоньку отойти назад и убежать']], resize_keyboard=True)
            await bot.sendMessage(chat_id, 'Вещи собраны и герой потихоньку двигается в сторону двери...')
            await bot.sendPhoto(chat_id,photo=img3,caption='Просторы пустоши были невероятно красивые. В этой атмосфере постапокалиптического утра чуствовалось что-то загадочное. Твоё внимание привлёк шелест кустов в ста метрах и рука опустилась на спусковые крючки обреза.', reply_markup=markup)       
            img3.close()
        #================================================================
                
        elif msg['text'].lower() == 'admin':
            print(msg['from'].get('username'))
            if msg['from'].get('username')=='xXZyzzXx':
                markup = ReplyKeyboardMarkup(keyboard=[
                             ['+exp','+Деньги','Бан'],
                             ['Код','Hide=h']], resize_keyboard=True)
                await bot.sendMessage(chat_id, 'Выбери действие: ', reply_markup=markup)
        #==============Поселение====       
        elif msg['text'] == '\U0001f3de Поселение' or msg['text'] == '\u2b05\ufe0f Назад':
            markup = ReplyKeyboardMarkup(keyboard=[
                         ['\U0001f3e1 Участок','\U0001f417 Животные','\U0001f6e0 Крафт'],
                         ['\U0001f527 Улучшения','\U0001f3d7 Строения','\U0001f519 Назад']], resize_keyboard=True)
            await bot.sendMessage(chat_id, 'Добро пожаловать в Ваше поселение! Дела пока идут хорошо..', reply_markup=markup)
        elif msg['text'] == '\U0001f3e1 Участок':
            markup = ReplyKeyboardMarkup(keyboard=[
                         ['\u2b05\ufe0f Назад']], resize_keyboard=True)
            await bot.sendMessage(chat_id, 'На участке временно пусто, найдите зерна а так же постройте грядки в разделе "Строения"', reply_markup=markup)
        elif msg['text'] == '\U0001f417 Животные':
            markup = ReplyKeyboardMarkup(keyboard=[
                         ['\u2b05\ufe0f Назад']], resize_keyboard=True)
            await bot.sendMessage(chat_id, 'В загоне сейчас '+str(config.animal)+' животных', reply_markup=markup)
        elif msg['text'] == '\U0001f6e0 Крафт':
            markup = ReplyKeyboardMarkup(keyboard=[
                         ['\u2b05\ufe0f Назад']], resize_keyboard=True)
            await bot.sendMessage(chat_id, 'Станок не готов, для постройки необходимо 20 ед. дерева! У тебя '+str(config.wood)+' ед. дерева.', reply_markup=markup)
        elif msg['text'] == '\U0001f527 Улучшения':
            markup = ReplyKeyboardMarkup(keyboard=[
                         ['\u2b05\ufe0f Назад']], resize_keyboard=True)
            await bot.sendMessage(chat_id, 'Временно нечего улучшать. Уходи..', reply_markup=markup)
        elif msg['text'] == '\U0001f3d7 Строения':
            markup = ReplyKeyboardMarkup(keyboard=[
                         ['\u2b05\ufe0f Назад']], resize_keyboard=True)
            await bot.sendMessage(chat_id, 'Возможность постройки открывается дальше по сюжету.', reply_markup=markup)
        #===================
        elif msg['text'] == '/restart':
            f = open('bd.txt', 'w')
            f.write('1')
        elif msg['text'] == '/stats':
            await stats(chat_id, msg)
        elif msg['text'] == '+exp':
            config.exp+=10
            print(config.exp)
        elif command == 'h':
            markup = ReplyKeyboardRemove()
            await bot.sendMessage(chat_id, 'Hide custom keyboard', reply_markup=markup)
        elif command == 'f':
            markup = ForceReply()
            await bot.sendMessage(chat_id, 'Хуле хочешь', reply_markup=markup)
        '''
        elif command == 'i':
            markup = InlineKeyboardMarkup(inline_keyboard=[
                         [dict(text='Telegram URL', url='https://core.telegram.org/')],
                         [InlineKeyboardButton(text='Callback - show notification', callback_data='notification')],
                         [dict(text='Callback - show alert', callback_data='alert')],
                         [InlineKeyboardButton(text='Callback - edit message', callback_data='edit')],
                         [dict(text='Switch to using bot inline', switch_inline_query='initial query')],
                     ])

            global message_with_inline_keyboard
            message_with_inline_keyboard = await bot.sendMessage(chat_id, 'Inline keyboard with various buttons', reply_markup=markup)
        '''

async def on_callback_query(msg):
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    print('Callback query:', query_id, from_id, data)

    if data == 'notification':
        await bot.answerCallbackQuery(query_id, text='Notification at top of screen')
    elif data == 'alert':
        await bot.answerCallbackQuery(query_id, text='Alert!', show_alert=True)
    elif data == 'edit':
        global message_with_inline_keyboard

        if message_with_inline_keyboard:
            msg_idf = telepot.message_identifier(message_with_inline_keyboard)
            await bot.editMessageText(msg_idf, 'NEW MESSAGE HERE!!!!!')
        else:
            await bot.answerCallbackQuery(query_id, text='No previous message to edit')


TOKEN = config.token

bot = telepot.aio.Bot(TOKEN)
answerer = telepot.aio.helper.Answerer(bot)

loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot, {'chat': on_chat_message,
                                   'callback_query': on_callback_query,}).run_forever())
print('Listening ...')
#===================================================


loop.run_forever()
