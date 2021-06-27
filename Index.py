import telebot;
from typing import Text;
from string import Template;
from telebot import types; 
from Config.config import configeration_app, client_request, client_error;
from DataBase.clientDataBase import add;


configeration = configeration_app();
request = client_request();
error = client_error();


bot = telebot.TeleBot(configeration['toket']);


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        request['welcome_words'],
    );

    bot.send_message(
        message.chat.id,
        request['client_data_step_1'],
    );

    bot.register_next_step_handler(message, data_collection_name);

@bot.message_handler(content_types=['text'])
def data_collection_name(message):
    if message.text.isdigit():
        bot.send_message(
            message.chat.id,
            error['error_name'],
        );
        bot.register_next_step_handler(message, data_collection_name);
    else:
        global name, t_id;
        name = str(message.text);
        t_id = int(message.from_user.id);

        bot.send_message(
            message.chat.id,
            request['client_data_step_2'],
        );
    
        bot.register_next_step_handler(message, data_collection_age);


def data_collection_age(message):
    if message.text.isdigit():
        global age;
        age = int(message.text);

        bot.send_message(
            message.chat.id,
            request['client_data_step_3'],
        );

        bot.register_next_step_handler(message, data_collection_city);
    else:
        bot.send_message(
            message.chat.id,
            error['error_age'],
        );

        bot.register_next_step_handler(message, data_collection_age);

def data_collection_city(message):
    if message.text.isdigit():
        bot.send_message(
            message.chat.id,
            error['error_city'],
        );

        bot.register_next_step_handler(message, data_collection_city);
    else:
        global city; 
        city = str(message.text);

        bot.send_message(
            message.chat.id,
            request['client_data_step_4'],
        );
        bot.register_next_step_handler(message, data_collection_about);

def data_collection_about(message):
    global about;
    about = str(message.text);

    keyboard = types.InlineKeyboardMarkup();

    key_fun = types.InlineKeyboardButton(text='Общение', callback_data='fun');
    key_only_fun = types.InlineKeyboardButton(text='На одну ночь', callback_data='only_fun');
    key_work = types.InlineKeyboardButton(text='Ищу работу/работника', callback_data='work');

    if age >= 18:
        keyboard.add(key_fun);
        keyboard.add(key_only_fun);
        keyboard.add(key_work);
    else:
        keyboard.add(key_fun);
        keyboard.add(key_work);

    question = request['client_data_step_5'];
    bot.send_message(message.chat.id, text=question, reply_markup=keyboard);


@bot.callback_query_handler(func=lambda call:True) #блок ответственный за call.data
def data_collection_status_call(call):
    global status;

    if call.data == 'fun':
        status = 'общение';
    elif call.data == 'only_fun':
        status = 'на одну ночь';
    else:
        status = 'ищу работу/работника';
    
    response = bot.send_message(
        call.message.chat.id,
        request['client_data_step_6'],
    );

    bot.register_next_step_handler(response, data_collection_add);  


@bot.message_handler(content_types=['text, photo'])
def data_collection_add(message):
    data = [t_id, name, age, about, status, city];

    for value in data:
        if value == None:
            bot.send_message(
                message.chat.id,
                error['client_data_error'],
            );

            bot.register_next_step_handler(message, data_collection_add);
        else:
            add(data);

    try:

        file_info = bot.get_file(message.document.file_id);

        try:
            downloaded_file = bot.download_file(file_info.file_path);
            src = u'D:\\Projects\\PyProjects\\CFAC_V1\\Images\\image' +'_'+f'{str(t_id)}'+'_'+message.document.file_name;
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file);
                bot.send_message(message.chat.id, request['true_result']);
        except:
            bot.reply_to(message, error['error_image']);
    except:
        bot.send_message(message.chat.id, request['not_found_image']);
        bot.send_message(message.chat.id, request['true_result']);
        




bot.polling(none_stop=True, interval=0);