p=input("camelCase: ")


def converter(p):
    snake=" "
    for i in p:
        if i.isupper() :
            snake=snake+'_'+ i.lower()
        else:
            snake=snake+i
    print("snake_case: ",snake)
converter(p)

