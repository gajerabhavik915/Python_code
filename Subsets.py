
a = [1,2,3,4]

result = [[]]

# result = result + [[1]]
for i in a:
    result = result + [l + [i] for l in result]
print(result)
