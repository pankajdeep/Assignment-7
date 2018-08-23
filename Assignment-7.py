#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop.
dic={}
n=int(input("Enter size of Dictionary"))
for i in range(n):
    key=input("Enter key")
    value=input("Enter value")
    dic[key]=value
print("Dictionary is :",dic)
val=input("Enter value whose key you want to find")
for i,j in dic.items():
    if(j==val):
        print("The key of",val,"is",i)


#Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.
#Print the marks of a given student from that dictionary for every subject. 
#Hint: Use nested dictionary to store subjects marks.
d1={}
n=int(input("Enter the number of students"))
for i in range (n):
    name=input("Enter name of student")
    d2={}
    maths=int(input("Enter marks obtained in maths"))
    network=int(input("Enter marks obtained in networking"))
    os=int(input("Enter marks obtained in OS"))
    python=int(input("Enter marks obtained in Python"))
    d2['maths']=maths
    d2['networking']=network
    d2['OS']=os
    d2['Python']=python
    d1[name]=d2
inp=input("Enter the name of student whose marks you want to find")
for a,b in d1[inp].items():
    print(inp,"has got",b,"marks in",a)
    
