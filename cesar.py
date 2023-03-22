import sys

def indexis_punct(text):        # высчитываем несдвигаемые индексы (знаков препинания, пробелов, заглавных букв)
    spets = [' ', '!', '#', '$', '%', '&', '*', '+', '-', '=', '?', '@', '^', '_', '.', ',', '<', '>', '"', "'"]
    [spets.append(str(i)) for i in range(10)]
    symb = [i for i in range(len(text)) for j in range(len(spets)) if text[i] == spets[j]]
    upper = [i for i in range(len(text)) if text[i] != text[i].lower()]
    return symb, upper

def dict_index(txt, symb):                  # Функция зарисовки индексов в словарь для цикличного шифрования.
    dictind = {}
    for i in range(len(txt)):
        for j in symb:
            if i == j:
                dictind.update({j: txt[i]})
    return dictind


def gen_eng_abc():              # генерация английского словаря
    return [chr(i) for i in range(97, 123)]


def gen_rus_abc():              # генерация русского словаря
    return [chr(i) for i in range(1072, 1104)]

def question(q, ans='ВВОДИТЕ ТОЛЬКО: (у/n)', t='y', f='n'):         # Функция вопросов и ответов.
    while True:
        quest = input(q)
        if quest == t:
            return True
        elif quest == f:
            return False
        else:
            print(ans)

def question_dig(start, end, qd, ans):                              # Функция вопросов по цифрам.
    while True:
        quest = input(qd, )
        if quest[0] != '-':
            if not quest.isdigit():
                print(ans)
            elif int(quest) < start or int(quest) > end:
                print(ans)
            else:
                return int(quest)
        elif not quest[1::].isdigit():
            print(ans)
        elif int(quest) < start or int(quest) > end:
            print(ans)
        else:
            return int(quest)

def crypter(txt, ssymb, dict, shift, uppl):                 # Функция расшифровки по заданным сдвигам.
    outtext = []
    for i in range(len(txt)):
        if i in ssymb:
            outtext.append(txt[i])
            continue
        for j in range(len(dict)):
            if txt[i].lower() == dict[j]:
                if j + shift > len(dict)-1:
                    j = j - len(dict)
                outtext.append(dict[j+shift])
                break
    for a in range(len(outtext)):                       # Расставляем обратна заглавные буквы по индексам как лежало! )
        if a in uppl:
            outtext.insert(a, outtext[a].upper())
            outtext.pop(a + 1)
    return outtext

def cicle_cryptor(txt, dict, dicind, uppl, vec='r'):              # Функция для цикличного шифрования/дешифрования
    outtext, spltext = [], ''
    for i in range(len(txt)):
        if i in dicind:
            if txt[i] != ' ':
                continue
        spltext += txt[i]
    if vec == 'r':
        for t in spltext.split():
            for i in range(len(t)):
                for j in range(len(dict)):
                    if t[i].lower() == dict[j]:
                        if j + len(t) > len(dict)-1:
                            j = j - len(dict)
                        outtext.append(dict[j+len(t)])
                        break
    if vec == 'l':
        for t in spltext.split():
            for i in range(len(t)):
                for j in range(len(dict)):
                    if t[i].lower() == dict[j]:
                        if j - len(t) > len(dict)-1:
                            j = j + len(dict)
                        outtext.append(dict[j-len(t)])
                        break
    for e in range(len(outtext)+len(dicind)):       # Расставляем обратна спецсимволы и пробелы по индексам как лежало!)
        if not e in dicind.keys():
            continue
        for f in dicind.keys():
            if e == f:
                outtext.insert(e, dicind[f])
                break
    for a in range(len(outtext)):                       # Расставляем обратна заглавные буквы по индексам как лежало! )
        if a in uppl:
            outtext.insert(a, outtext[a].upper())
            outtext.pop(a + 1)
    return outtext


question_lang = 'Какой текст будем зашифровывать/расшифровывать? Английский или русский? (е/r): '
ans_lang = 'ВВОДИТЕ ТОЛЬКО: (e/r)'
if question(question_lang, ans_lang, 'e', 'r'):
    abc = gen_eng_abc()
else:
    abc = gen_rus_abc()
    question_yo = 'Добавить ли к словарю букву "ё"? (y/n): '
    if question(question_yo):
        abc.insert(6, 'ё')

question_force = 'Хотите попробовать расшифровать текст перебором сдвигов? (y/n)'
if question(question_force):
    crypt_text = input('Введите текст который нужно расшифровать: ')
    spsymb, upplets = indexis_punct(crypt_text)     # Собираем индексы у неперемещаемых символов и заглавных букв!
    for i in range(-len(abc), len(abc)):
        outtext = crypter(crypt_text, spsymb, abc, i, upplets)
        print('дешифрованный текст сдвиг: ' + str(i) + '\n', *outtext, sep='')
    sys.exit()                          # Прерываем программу, так как перебор закончился, и делать тут больше неча. )

question_cicle = 'Хотите попробовать зашифровать/расшифровать текст цикличными сдвигами? (y/n): '
if question(question_cicle):
    crypt_text = input('Введите текст который нужно расшифровать/зашифровать: ')
    spsymb, upplets = indexis_punct(crypt_text)     # Собираем индексы у неперемещаемых символов и заглавных букв!
    dictsymb = dict_index(crypt_text, spsymb)       # Собираем словарь индексов
    question_vect_cicle = 'укажите направление шифрования/дешифрования, влево по алфавиту или вправо (l/r): '
    question_vect_ans = 'вводим только l или r!'
    if question(question_vect_cicle, question_vect_ans, 'l', 'r'):
        outtext = cicle_cryptor(crypt_text, abc, dictsymb, upplets)
        print('Ведённый вами текст:\n', crypt_text, sep='')
        print('дешифрованный/зашифрованный текст:\n', *outtext, sep='')
        sys.exit()                        # Прерываем программу, так как перебор закончился, и делать тут больше неча. )
    else:
        outtext = cicle_cryptor(crypt_text, abc, dictsymb, upplets, vec='l')
        print('Ведённый вами текст:\n', crypt_text, sep='')
        print('дешифрованный/зашифрованный текст:\n', *outtext, sep='')
        sys.exit()                        # Прерываем программу, так как перебор закончился, и делать тут больше неча. )


question_shift = 'Введите шаг сдвига от '+ str(-abs(len(abc))) +' до ' + str(len(abc)) + ': '
ans_shift = 'Вводим только числа от '+ str(-abs(len(abc))) +' до ' + str(len(abc)) + '!'
shift = question_dig(-abs(len(abc)), len(abc), question_shift, ans_shift)


crypt_text = input('Введите текст который нужно зашифровать/расшифровать: ')
spsymb, upplets = indexis_punct(crypt_text)         # Собираем индексы у неперемещаемых символов и заглавных букв!
outtext = crypter(crypt_text, spsymb, abc, shift, upplets)          #Закидываем в функцию собранные параметры и Гоу!
print()
print('Ведённый вами текст:\n', crypt_text, sep='')
print('Шифрованный/дешифрованный текст:\n', *outtext, sep='')