import re
import long_response as long

def message_probability(user_message, recognised_words, singe_response=False, required_words=[]):
    message_certainty = 0
    has_required = True
#Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
#Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing the response system
while True:
    print('Bot: ' + get_response(input('You')))

