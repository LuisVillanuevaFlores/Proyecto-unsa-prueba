from a import multiple_saludo


def loop_regard():
    for i in range (10):
        a = multiple_saludo("Juan ", "cuidate")
        print(a)

def other_message(text):
    loop_regard()
    x ='@ ' + text + "@"
    b = multiple_saludo("pedro ", "adios")
    return x