'''
arr[5] = {12, 2, 4, 5, 6}
        100  104 108 112
Indexing starts from 0 because when its written arr[2] it is actually meant by *(address of that memory location),
address is calculated by= base address(where the indexing starts) + (index * size), for arr[2] address = 100 + 2*4 = 108
hence the value at 108 is 4 that is the index 2, starts from 0  
'''
