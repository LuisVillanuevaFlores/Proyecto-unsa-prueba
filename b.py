from a import multiple_saludo


def loop_regard():
    for i in range (10):
        a = multiple_saludo("Juan ", "cuidate")
        print(a)

def concate_message(text):
    loop_regard()
    print('@'*10)
    b = multiple_saludo("pedro ", "adios")