# f=open('exam/file2.py','x')
# print(f.write("Hello"))

# f=open('exam/file2.py','w')
# print(f.write('Python'))

# f=open('exam/file2.py','r')
# print(f.read)

# f=open('Exam/demo.txt','x')
# print(f.write('hello \nwelcome \nhiii'))


f=open('Exam/demo.txt','r')
l=len(f.readlines())
f.seek(0)
longest_word=' '
for i in range(l):
    a=f.readline().strip()
    s=a.split(' ')
    for i in s:
        if i!=' ':
          if len(i)>len(longest_word):
           longest_word=i
print("Longest Word :",longest_word)        

'''
Longest Word : hiiiiiii 
'''



