
def isValid(s: str) -> bool:
    dict1 = {')': '(', '}': '{', ']': '['}
    list1 = []
    if s[0] in '{[(' and s[len(s) - 1] in ')}]':
        for a in s:
            if a in '{[(':
                list1.append(a)
            elif len(list1) != 0:
                if list1[len(list1) - 1] == dict1[a]:
                    list1.pop(len(list1) - 1)
                else:
                    return False
            elif len(list1) == 0 and a not in '{[(':
                return False

        if len(list1) == 0:
            return True
        else:
            return False
    else:
        return False

print(isValid('(()){[]}{)'))
s1 = '()[]('
# -------------------------------------------------------------

def isValid(s: str) -> bool:
    stack = []
    closetoopen = {')': '(', '}': '{', ']': '['}
    for i in s:
        if i in closetoopen:
            if stack and stack[-1] == closetoopen[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False

print(isValid('(()){[]}{)'))

# ----------------------------------------------------------------

def isValid(s: str) -> bool:
    dict1 = {')': '(', '}': '{', ']': '['}
    list1 = []
    if s[0] in '{[(' and s[-1] in ')}]':
        for a in s:
            if a in dict1:
                if len(list1) !=0 and list1[-1] == dict1[a]:
                    list1.pop(len(list1) - 1)
                else:
                    return False
            # elif len(list1) == 0 and a not in '{[(':
            #     return False
            else:
                list1.append(a)
        return True if not list1 else False
        # if len(list1) == 0:
        #     return True
        # else:
        #     return False
    else:
        return False

print(isValid('(())'))
