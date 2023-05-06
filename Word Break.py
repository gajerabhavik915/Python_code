
a = 'leetcode'
dict = ['tco','lee','leett', 'de', 'cod']
# dict = ['lee','leett','tco', 'de', 'cod']


def wordBreak(a, Dict):
    a1 = a
    for num in range(len(Dict)):
        def rerun(a1, Dict):

            for i in Dict:
                if len(i) <= len(a1) and i == a1[:len(i)]:
                    a1 = a1[len(i):]
                    break

            return a1

        print(a1)
        a1 = rerun(a1,Dict)


print(wordBreak(a, dict))



    # if a1:
    #     srt = rerun(a1, Dict)
    # elif









