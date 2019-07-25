import operator

def sort_unique_chars(S):
    if len(S) == 0:
        return 
    
    dict = {}
    for i in range(len(S)):
        if S[i].isalpha() or S[i].isdigit():
            if S[i] in dict.keys():
                dict[S[i]] = dict[S[i]] + 1
            else:
                dict[S[i]] = 1
    
    sorted_x = []
    sorted_x = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    for key, value in sorted_x:
        print(str(key)+'='+str(value))
        
    
sort_unique_chars("The dog ran with the cat.")
