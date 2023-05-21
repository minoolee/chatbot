# Chatbot

import random

# Greeting chatbot
GREETING_INPUTS = ["hallo", "hi", "hey", "servus"]
GREETING_RESPONSES =["Hallo", "Hi", "Hey", "Servus"]

# Standert answer if Chatbot are not working
UNKNOWN_RESPONSES = ["Excuse me, I did not understand that", "Can you repeat please?", "I am not sure what did you mean."]

# class for Chatbot

class Chatbot:
    def __int__(self):
        pass

    # function to choose one answer from list
    def get_random_response(self, responses):
        return random.choice(responses)

    # function for processing the input
    def process_user_input(self, user_input):
        if user_input.lower() in GREETING_INPUTS:
            # When user send the greeting
            bot_response = self.get_random_response(GREETING_RESPONSES)
        else:
            # when the Bot do not understand
            bot_response = self.get_random_response(UNKNOWN_RESPONSES)

        return bot_response

def main():
    chatbot = Chatbot()

    while True:
        user_input = input("You: ")
        bot_response = chatbot.process_user_input(user_input)
        print("Chatbot:", bot_response)

# start the Programe
if __name__ == "__main__":
    main()