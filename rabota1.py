d = {}  # създаваме си структура - речник, в която да се съхраняват данните

while True:

    text = input().split(' ') # разделяме текста
    command = text[0].lower() #намаляваме шрифта , за да може if командата да зачете дори когато
                            #потребителят е въвел Exit
    if command == 'exit':#прекратява програмата при въведен Изход
        break

    elif command == "set": # добавяме новите елементи към речника
        text1 = text[1]
        text2 = text[2]
        print(f"Saved {text1} = {text2}")
        d[text1] = text2

    elif command == "get": #изважда ни търсения елемент от речника, ако съществува

        k = False#въвеждаме си булева променлива, която ни проверява дали търсеният елемент съшествува в речника
        text1 = text[1]
        for i in d.keys():
            if i == text1:
                k = True
                print(f"{text1} = {d[text1]}")
        if not k:   #ako не съществува ни съобщава за грешка
            print(f"Err: no value for {text1}")
        k = False

    elif command == "load":
        file_name = text[1]#отделяме името на файла
        file = open(file_name, 'r')

        for line in file.readlines():#четем информацията от файла и добавяме данните към речника
            line = line.strip()
            key, value = line.split("=")#разделяме по = двата елемента
            d[key] = value
        file.close()    # затваряме файла
        print(f"Data from {file_name} is loaded")

    elif command == "save":
        file_name1 = text[1]
        file = open(file_name1, 'w') #отваряме файла за писане и елементите и ключовете от речника ги презаписваме там
        for i in d.keys():
            file.write(f"{i}={d[i]}\n")
        print(f"Data exported to {file_name1}")
        file.close()

    elif command == "reverse":#обръщаме текста наобратно
        texto = ' '.join(x for x in text[1:len(text)])
        string = ''
        for i in range(len(texto) - 1, -1, -1):
            string += texto[i]
        print(string)

    elif command == "count-words":
        count_words = 0
        file_name2 = text[1]
        file = open(file_name2, 'r')#отваряме файла за четене и разделяме по празно място всеки ред
                                    # и съответно броим думите на всеки ред

        for line in file.readlines():
            line1 = line.split()
            count_words += len(line1)#броя думи на един ред
        file.close()
        print(f"Words in {file_name2}: {count_words}")


    else:   #когато не е въведена валидна команда ни извежда грешка
        print(f"Error - enter a new command!")
