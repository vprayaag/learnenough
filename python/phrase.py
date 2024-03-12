class Phrase():

    def __init__(self, content):
        self.content = content

    def ispalindrome(self):
        temp = self.content.lower()
        return temp == temp[::-1]

    def __iter__(self):
        self.phrase_iterator = iter(self.content)
        return self
    
    def __next__(self):
        return next(self.phrase_iterator)



if __name__ == '__main__':

    phrase = Phrase('abcddcba')

    print(phrase)
    print(phrase.content)

    for i, c in enumerate(phrase):
        print(f'Character number {i} in phrase is {c}')
