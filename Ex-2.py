def makeDict(k,v):
    # Create an empty dictionary
    D={}
    for i in range(len(k)):
        D[k[i]] =v[i]
    return D
#set the two tuple
k=('korean','math','english','science')
v = ('73.5','94.2','63.7','88.4')
#check the size
if len(k)==len(v):
    D = makeDict(k,v)
    print(D)
    #check the value obtained from D is correct
    for i in k:
        if i in D:
            print(f"Value for {i} is obtained: {D[i]}")
        else:
            print(f"Value for {i} is not obtained")
else:
    print('different size!!')