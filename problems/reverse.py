# = [0,10,20,40]
#L[::-1]
#[40, 20, 10, 0]

def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]
print (reverse("Alex"))

def reverse(s):
  str = ""
  for i in s:
    str = i + str
    print(str)
  return str

print(reverse("Alex"))

l = [2,3,4,6]
l = [l[i] for i in range(len(l)-1, -1, -1)]
print(l)

l = [1, 2, 3, 4, 5]
i = len(l)
while i <= len(l)/2:
    l[i], l[len(l) - i - 1] = l[len(l) - i - 1], l[i]
print(l)

#https://www.quora.com/How-can-I-reverse-a-list-in-python