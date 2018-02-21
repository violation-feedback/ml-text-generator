from os import listdir
from os.path import isfile

import markovify, io

def getTextFiles():
    return [f for f in listdir('.') if isfile(f) and f.endswith('.txt')]

class TitleGenerator:
    def __init__(self, tlen=200):
        self.titleLength = tlen
        models = []
        for fname in getTextFiles():
            dots = fname.split('.')
            with io.open(fname, 'r', encoding='utf-8') as f:
                models.append((markovify.NewlineText(f.read(), state_size=2), int(dots[-2]) if len(dots) > 2 else 100))
        self.textModel = markovify.combine([a for a, b in models], [b for a, b in models])

    def generateTitle(self):
        return self.textModel.make_short_sentence(self.titleLength, tries=100, max_overlap_ratio=0.6)

if __name__ == '__main__':
    gen = TitleGenerator()
    for _ in range(5):
        print(gen.generateTitle())