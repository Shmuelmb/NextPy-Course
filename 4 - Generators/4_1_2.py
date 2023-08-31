# 4.1.2

def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in',
             'gato': 'cat', 'casa': 'house', 'el': 'the'}
    return ' '.join((words[word] if word in words else word for word in sentence.split()))


print(translate('el gato esta en la casa'))
