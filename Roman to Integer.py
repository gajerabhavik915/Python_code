import time

a = 'MMMMCMLXXXV'
dict1 = {'I': 1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D' : 500,'M':1000}
start_time = time.perf_counter()
len1 = len(a)-1
val = 0

while len1 > 0:
    if dict1[a[len1]] > dict1[a[len1-1]]:
        val += dict1[a[len1]] - dict1[a[len1-1]]
        len1 = len1 - 2
    elif a[len1]==a[len1-1]:
        val += dict1[a[len1]] + dict1[a[len1-1]]
        len1 = len1 - 2
    else:
        val += dict1[a[len1]]
        len1 = len1 - 1

if len1 == 0:
    val = val + dict1[a[0]]
end_time = time.perf_counter()

print(val)
print(f"Total execution time is {(end_time - start_time)*1e6:.2f} microseconds.")
# -----------------------------------------------------------------

# def romanToInt(s: str) -> int:
s = 'MMMMCMLXXXV'
dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
start_time = time.perf_counter()
b = len(s) - 1
res = 0
for i in range(len(s)):
    if i < len(s) - 1 and dict1[s[i]] < dict1[s[i + 1]]:
        res -= dict1[s[i]]
    else:
        res += dict1[s[i]]
end_time = time.perf_counter()

print(res)
print(f"Total execution time is {(end_time - start_time)*1e6:.2f} microseconds.")
#
# ------------------------------------------------------------------------------------------

s = 'MMMMCMLXXXV'
dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
start_time = time.perf_counter()
i = len(s) - 1    #8
res = 0
while i >= 0:
    if i < len(s) - 1 and dict1[s[i]] < dict1[s[i + 1]]:
        res -= dict1[s[i]]
    else:
        res += dict1[s[i]]
    i-=1

end_time = time.perf_counter()

print(res)
print(f"Total execution time is {(end_time - start_time)*1e6:.2f} microseconds.")


