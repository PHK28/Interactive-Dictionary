import json
from difflib import get_close_matches

data_file = open('data.json')

dictionary_data = json.load(data_file)

# print(dictionary_data['Natasha'])
# print(dictionary_data.keys())

def translate(word):
    l_word = word.lower()
    msg = 'Sorry word doesn\'t exist. Please double check it'
    if l_word in dictionary_data:
        return dictionary_data[l_word]
    else:
        close_match = get_close_matches(l_word,dictionary_data.keys())
        if len(close_match) > 0:
            ans = input('Did you mean {} ? Please enter Y or N : '.format(close_match[0]))
            if ans.upper() == 'Y':
                return dictionary_data[close_match[0]]
            elif ans.upper() == 'N':
                return msg
            else:
                return 'Sorry, we didn\'t understand your entry'
        else:
            return msg

word = input('Please enter word you want to find definition for : ')

output = translate(word)

if isinstance(output,list):
    for definition in output:
        print('  -> {}'.format(definition))
else:
    print(output)
