
a = 'leetcode'
dict = ['lee','le', 'tco', 'de', 'cod']

def wordBreak(s, Dict):
    for i in Dict:
        if i[:] == s[:len(i)]:
            return True

print(wordBreak(a,dict))



