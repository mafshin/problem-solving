input_number = int(input('enter the number: '))
list_1 = []
list_2 = []
for c in range(0,input_number-1):
    list_1.append(input('enter the text: '))
input_text = input('enter the text: ').split(' ')
for a in input_text:
    for b in range(1,len(a)+1):
        start = 0
        end = b
        while len(a)+1 != end:
            r = 1
            for d in list_1:
                if a[start:end] in d:
                    r += 1
            if r == input_number:
                list_2.append(a[start:end])
            start += 1
            end += 1
print(list_2)
# some yes ok
# yes will some do it
# it is somehow good yes
# yes someone found it