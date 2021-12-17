print("Hola amigo como estas")
def saludar (text):
    return "Hola "+ text

def multiple_saludo(text,anotherText):
    message = saludar(text)
    final_message = message + " " + anotherText
    return final_message

a = multiple_saludo("Luis ", "cuidate")
