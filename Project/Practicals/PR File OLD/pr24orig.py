print("Title Case")  #Title
A , state , a = input("Enter String: ") , 0, []
for iter in range(0,len(A)):   #convert string to mutable list
    a.append(A[iter])
a[0] = a[0].upper()            #Exception handling for first term
for j in range(0,len(A)):      #Uppercase after each Spacebar
    if(a[j]==" "):
        a[j+1] = a[j+1].upper()
    print(a[j],end="")
