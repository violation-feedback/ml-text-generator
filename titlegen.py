from os import listdir
from os.path import isfile, join

import markovify, io

def getTextFiles():
    return [f for f in listdir('.') if isfile(f) and f.endswith('.txt')]

class TitleGenerator:
    _textModel = None

    def __init__(self):
        corpus = ''
        for fname in getTextFiles():
            with io.open(fname, 'r', encoding='utf-8') as f:
                corpus += f.read()
        self._textModel = markovify.NewlineText(corpus)

    def generateTitle(self):
        return self._textModel.make_sentence(tries=100)

if __name__ == '__main__':
    gen = TitleGenerator()
    for _ in range(5):
        print(gen.generateTitle())