m=input("Enter a number:")
m=int(m)
numbers=[1,2,3,4,5,6,7,8,9,10]                
in_words=["one","two","three","four","five","six","seven","eight","nine","ten"]
for i in range (len(numbers)) : 
   if m==numbers[i]:
     print(in_words[i])    
        