import random
def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return("Wena pelao")
    if p_message == "roll":
        return str(random.randinit(1,6))

    return("Que wuea?")
