word_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

list_count = []
for word in range(len(word_list)):
    box = []
    plus = None
    count = word
    for i in word_list[word]:
        if '0' <= i <= '9':
            box.append(i)
        if i == '+':
            plus = i
    if len(box) > 0:
        t = f"{''.join(box):0>2}"
        if plus:
            t = plus + t
        word_list[count] = t
        list_count.append(t)

s = 0
while s < len(word_list):
    if word_list[s] in list_count:
        word_list.insert(s, '"')
        word_list.insert(s + 2, '"')
        s += 2
    s += 1

print(word_list)
text = ' '.join(word_list)
print(text)
