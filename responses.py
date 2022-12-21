import random

def hanle_response(message) -> str:
    p_message = message.lower()

    if p_message == "bot":
        return "it's me"

    # if p_message == 'hello':
    #     return 'hey there'

    # if p_message == 'roll':
    #     return str(random.randint(1, 6))

    if p_message == '!help':
        return "`This is a help message that you can modify.`"

    # return " I don't know what you said"