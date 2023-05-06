
a = 'leetcode'
# dict = ['tco','leet','leet', 'de', 'cod']
dict = ['lee','code','leeet']

# a ="applepenapple"
# dict = ["le","app","pen", "appl"]


def wordBreak(a, Dict):
    a1 = a
    first_ele = a[0]
    pos = []
    for loc,i in enumerate(dict):
        if i[0] == first_ele:
            pos.append(loc)
    # print(pos)

    for i1 in pos:
        a1 = a
        if len(dict[i1]) <= len(a1) and dict[i1] == a1[:len(dict[i1])]:
            a1 = a1[len(dict[i1]):]
            # print(a1)

        for num in range(len(a)//2):
            def rerun(a1, Dict):

                for i in Dict:
                    if len(i) <= len(a1) and i == a1[:len(i)]:
                        a1 = a1[len(i):]
                        break

                return a1

            print(a1)
            if len(a1) == 0:
                return False if a1 else True
            else:
                a1 = rerun(a1, Dict)
    return False if a1 else True



print(wordBreak(a, dict))












