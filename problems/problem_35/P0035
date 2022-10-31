input_number = int(input('enter the  number: '))
list_1 = []
list_2 = []
list_3 = []
input_text = input('enter the text: ')
for b in range(0,input_number-1):
    list_1.append(input('enter the text: '))
for a in range(1,len(input_text)):
    start = 0
    end = a
    while end != len(input_text):
        p = 1
        for c in list_1:
            if input_text[start:end] in c:
                p += 1
        if p == input_number:    
            list_2.append(input_text[start:end])
        start += 1
        end += 1
for d in list_2:
    y = 0
    for e in list_2:
        if len(d) > len(e) or len(d) == len(e):
            y += 1
    if y == len(list_2):
        t = d
list_3.append(input_text.index(t))
for s in list_1:
    list_3.append(s.index(t))
print((max(list_3)-list_3[0])*'#'+input_text)
for q in range(0,len(list_1)):
    print((max(list_3)-list_3[q+1])*'#'+list_1[q])
# some yes ok
# yes will some do it
# it is somehow good yes
# yes someone found it