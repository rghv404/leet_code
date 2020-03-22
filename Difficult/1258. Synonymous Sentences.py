class Solution(object):
    
    def __init__(self):
        self.words = dict()
        self.res = set()
        self.visited = set()
        
    def generateSentences(self, synonyms, text):
        # creating dictionary to store synonyms mapping
        for syn in synonyms:
            self.words.setdefault(syn[0], []).append(syn[1])
            self.words.setdefault(syn[1], []).append(syn[0])
        #adding oriogianl string to result
        self.res.add(text)
        if len(self.words) < 1:
            return self.res
        inputs = text.split(" ")
        # dfs traversal
        self.dfs(inputs)
        # return sorted set
        return sorted((self.res))
            
    def dfs(self, inputstr):
        for i, word in enumerate(inputstr):
            # do anything if synonym exist
            if word in self.words:
                # create lit of texts depending on number of synonyms for the current word
                allStrList = [inputstr[:i] + [synonym] + inputstr[i+1:] for synonym in self.words[word]]
                # traverse all above sentences
                for currStrList in allStrList:
                    newStr = " ".join(currStrList)
                    # if text alerady traversed and added to res then break from this loop
                    if newStr not in self.res:
                        self.res.add(newStr)
                        self.dfs(currStrList)