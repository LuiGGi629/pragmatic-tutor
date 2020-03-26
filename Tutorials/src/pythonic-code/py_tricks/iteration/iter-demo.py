class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


def sentence_gen(sentence):
    for word in sentence.split():
        yield word


my_sentence = Sentence('This is a test')
for i in my_sentence:
    print(i)
