import telebot
from telebot import types

bot = telebot.TeleBot('5531709190:AAF2N3Iub65stGhSnVh5RLXUfKciOgMbJkc')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    messag = f'Здравствуйте, <b>{message.from_user.first_name} <em>{message.from_user.last_name}</em></b>!'
    bot.send_message(message.chat.id, messag, parse_mode='html')
    bot.send_message(message.chat.id, 'Вас приветствует <b><em>Бот</em></b>, который может ответить на часто задаваемые вопросы', parse_mode='html')
       
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton(text="Как сделать заказ?", callback_data="item1")
    item2 = types.InlineKeyboardButton(text="Как оплатить заказ?", callback_data="item2")
    item3 = types.InlineKeyboardButton(text="Актуальны ли цены на сайте?", callback_data="item3")
    item4 = types.InlineKeyboardButton(text="Можно ли получить у вас консультацию или помощь по настройке купленного оборудования?", callback_data="item4")
    item5 = types.InlineKeyboardButton(text="Возможна ли доставка наложенным платежем?", callback_data="item5")
    item6 = types.InlineKeyboardButton(text="Могу ли я взять товар «На пробу»?", callback_data="item6")
    item7 = types.InlineKeyboardButton(text="Вы предоставляете гарантию на все товары?", callback_data="item7")
    item8 = types.InlineKeyboardButton(text="Могу ли я вернуть купленный товар, обменять его на другую модель?", callback_data="item8")
    item9 = types.InlineKeyboardButton(text="Как я могу вернуть или обменять купленный товар?", callback_data="item9")
    item10 = types.InlineKeyboardButton(text="Что значит статус товара «Под заказ»?", callback_data="item10")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
    bot.send_message(message.chat.id, 'Выберите интересующий Вас вопрос из списка ниже', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "item1":
        bot.send_message(call.message.chat.id, 'Как сделать заказ? ➤ Заказ вы можете сделать у нас на сайте')
    elif call.data == "item2":
        bot.send_message(call.message.chat.id, 'Как оплатить заказ? ➤ Оплатить Ваш заказ, возможно наличным и безналичным расчетом.')
    elif call.data == "item3":
        bot.send_message(call.message.chat.id, 'Актуальны ли цены на сайте? ➤ Да, именно по этим ценам вы можете приобрести товар прямо сейчас.')
    elif call.data == "item4":
        bot.send_message(call.message.chat.id, 'Можно ли получить у вас консультацию или помощь по настройке купленного оборудования? ➤ Наши менеджеры обязательно проконсультируют вас по выбору оптимального оборудования для ваших задач.')
    elif call.data == "item5":
        bot.send_message(call.message.chat.id, 'Возможна ли доставка наложенным платежем? ➤ Да, Вы можете оплатить товар при получении на складе перевозчика.')
    elif call.data == "item6":
        bot.send_message(call.message.chat.id, 'Могу ли я взять товар «На пробу»? ➤ Нет, использовать товар можно, только купив его.')
    elif call.data == "item7":
        bot.send_message(call.message.chat.id, 'Вы предоставляете гарантию на все товары? ➤ Подавляющее большинство товаров, представленных у нас, подлежит гарантийной замене и ремонту.')
    elif call.data == "item8":
        bot.send_message(call.message.chat.id, 'Могу ли я вернуть купленный товар, обменять его на другую модель? ➤ Да, в течение 14 дней вы можете обменять или вернуть купленное оборудование.')
    elif call.data == "item9":
        bot.send_message(call.message.chat.id, 'Как я могу вернуть или обменять купленный товар? ➤ Для возврата или обмена товара обращайтесь к нам в офис.')
    elif call.data == "item10":
        bot.send_message(call.message.chat.id, 'Что значит статус товара «Под заказ»? ➤ Это означает, что данный товар можно купить только при полной предоплате.')
    else:
        bot.send_message(call.message.chat.id, 'Ошибка, попробуйте еще раз')
                                                  

bot.polling(none_stop=True)