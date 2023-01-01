def levenstein_distance(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    s = []
    for i in range(max(l1,l2)):
        s.append([0]*min(l1,l2))
    app = 1
    for i in range(max(l1,l2)):
        s[i].insert(0,app)
        app += 1
    s.insert(0,[i for i in range(min(l1,l2)+1)])
    for i in range(1,max(l1,l2)+1):
        for j in range(1,min(l1,l2)+1):
            a,b,c = s[i-1][j]+1,s[i][j-1]+1,s[i-1][j-1]
            try:
                if s1[j-1] != s2[i-1]:
                    c+=1
            except:
                if s1[i-1] != s2[j-1]:
                    c+=1
            s[i][j] = min(a,b,c)
    return s[max(l1,l2)][min(l1,l2)]

str1 = input()
str2 = input()
print(levenstein_distance(str1,str2))