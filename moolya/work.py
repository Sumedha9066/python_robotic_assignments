
cp=[50,10,60]
sp=[60,5,80]
p=zip(cp,sp) # combing the cp and sp using a zip commend
for c,s in p:
    if (s>c): # if sp is greater than cp  then this condition is statisfies .
        print("profit=",s-c)
    else:
        print("loss=",c-s)# if sp is less than sp this condition will statifies