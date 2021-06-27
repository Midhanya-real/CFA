"""class App():
    _configeration_app = configeration_app();
    _client_request = client_request();
    _client_error = client_error();

    def __init__(self):
        self._token = configeration_app;
        self._request = client_request;
        self._error = client_error;
    
    def bot(self):
        bot = telebot.TeleBot(self._token['toket']);
        return bot;

    @bot.message_handler(commands=['start'])  
    def start(self, message):
        bot.send_message(
            message.chat.id,
            self._request['client_data_step_1'],
        )
"""

        # status = call.message;
        
        # bot.send_message(
        #     call.message.chat.id,
        #     request['client_data_step_6'],
        # );

        # bot.register_next_step_handler(call.message, data_collection);
import sys
sys.path.append("D:\Projects\PyProjects\CFAC_V1\DataBase");

from DataBase.clientDataBase import add;

add([1234561111, 'asgassg', 21, 'dgljjadnskg', 'sdgdsg', 'djkghkdbg']);
