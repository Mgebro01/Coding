


def text_to_morse(text):
    morse_dict = {' ': '|'}
    with open("../lessons/morsecode.txt", "r") as morse:
        for i in morse:
            let, mor = i.split('\t')
            morse_dict[let] = mor[:-1]

    result = ''
    for i in text.upper():
        result += f'{morse_dict[i]} '

    return result



#--------------------------


def morse_to_text(text):
    morse_dict = {'|': ' '}

    morse_dict[' '] = ''
    with open("../lessons/morsecode.txt", "r") as morse:
        for i in morse:
            let, mor = i.split('\t')
            morse_dict[mor[:-1]] = let




    result = ''
    text_list = []
    text_list = text.split()

    for i in text_list:
        result += f'{morse_dict[i]}'

    return result


Question_1 = input('what you want, morse to text or text to morse:>')

if Question_1 == 'morse to text':
    print(morse_to_text(input('input morse code:')))

if Question_1 == 'text to morse':
    print(text_to_morse(input('input text:')))
