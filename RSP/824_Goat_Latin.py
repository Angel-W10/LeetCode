class Solution:
    def to_goat(self, s, i):
        additions = i*'a'
        if s[0].lower() in {'a', 'e', 'i', 'o', 'u'}:
            s += 'ma'
            return s + additions
    
        else:
            f = s[0]
            s = s[1:] + f
            s += 'ma'
            return s + additions



    def toGoatLatin(self, sentence: str) -> str:
        '''
        go through the string sentence
        add each char to another str until find a space
        keep a count of the word from 1 to ...
        convert the word to goat language
        add it to a new str out and keep adding rest words

        O(len(str))
        '''
        temp = ""
        words=[]
        for i in sentence:
            if i != " ":
                temp+=i
            else:
                words.append(temp)
                temp = ""
        words.append(temp)
        out = ""
        for i, word in enumerate(words):
            print(i, word)
            out += self.to_goat(word, i+1) + " "
        out = out[:-1]
        return out