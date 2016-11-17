# coding=utf-8
from resolvers import kalinin_resolver, albert_resolver, tema_resolver, geva_resolver, stas_resolver, ban_resolver, \
    net_resolver, debug_resolver, zaebal_resolver, morning_resolver
from runserver import bot


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, u"Утро.")


@bot.message_handler(func=kalinin_resolver)
def kalinin_pidor(message):
    bot.send_message(message.chat.id, u'Калинин пидор')


@bot.message_handler(func=albert_resolver)
def albert_pidor(message):
    bot.send_message(message.chat.id, u'Альберт тоже пидор')


@bot.message_handler(func=tema_resolver)
def tema_pidor(message):
    bot.send_message(message.chat.id, u'Да и Тема пидор')


@bot.message_handler(func=geva_resolver)
def geva_pidor(message):
    bot.send_message(message.chat.id, u'Гева дизайнер')


@bot.message_handler(func=stas_resolver)
def stas_pidor(message):
    bot.send_message(message.chat.id, u'Стас по дефолту пидор')


@bot.message_handler(func=ban_resolver)
def ban(message):
    bot.send_message(message.chat.id, u'Бан')
    try:
        bot.kick_chat_member(message.chat.id, message.from_user.id)
    except Exception:
        pass


@bot.message_handler(func=net_resolver)
def net(message):
    bot.send_message(message.chat.id, u'ПИДОРА ОТВЕТ')


@bot.message_handler(func=debug_resolver)
def debug(message):
    bot.send_message(message.chat.id, u'Стас по дефолту пидор')


nicknames_dict = {
    u'Vaseev': u'Рома',
    u'Kalinin': u'Калинин',
    u'Hoffner': u'Альберт',
    u'Sten': u'Стас',
    u'Georgienko': u'Хома',
    u'Молчанов': u'Тёма',
    u'Rueda': u'Роб',
    u'Бафомет': u'Валя',
    None: u'Гева'
}


@bot.message_handler(func=zaebal_resolver)
def zaebal(message):
    try:
        name = nicknames_dict.get(message.from_user.last_name, message.from_user.first_name)
        bot.send_message(message.chat.id, u'%s, как ты заебал!(' % name)
    except Exception as e:
        print(e.message)
        try:
            print(message.from_user.last_name)
        except Exception:
            pass


@bot.message_handler(func=morning_resolver)
def morning(message):
    bot.send_message(message.chat.id, u'Утро.')
