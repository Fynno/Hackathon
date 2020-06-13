def Nmaxelements(list1, N,dataSplit): 
    final_list = [] 
    words = list(set(dataSplit))
    for i in range(0, N):  
        max1 = 0
        position = [0, 0]
        for j in range(len(list1)):
            for k in range(len(list1[0])):
                if list1[j][k] > max1: 
                    max1 = list1[j][k]; 
                    position = [j,k]
        list1[position[0]][position[1]]=0;
        final_list.append([max1, [words[position[0]],words[position[1]]]]) 
          
    return final_list