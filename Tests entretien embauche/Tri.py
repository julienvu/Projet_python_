#tri par sélection
import random
l = [ 5,8, 10, 2, 1]

#V
#[1,5, 8, 10, 2]
#sorted/unsorted

#V
#[1, 2, 5, 8, 10]


#V
#[1, 2 , 5, 8, 10]

print("UNSORTED", l)
def generate_random_list(n, min, max):
    l=[]
    for i in range(n):
        e=random.randint(min,max)
        l.append(e)
    return l






def selection_sort(l):
    for unsorted_index in range(0, len(l)):
        min=l[unsorted_index]
        min_index= unsorted_index
        for i in range(unsorted_index, len(l)):
            if l[i] < min:
                min=l[i]
                min_index= i   #V
            
        # in-place
        
        l[min_index] = l[unsorted_index] # [5, 8, 10, 2, 5]
        l[unsorted_index]= min # [1, 8, 10, 2, 5]


l=generate_random_list(100,-1000,1000)
print("UNSORTED:", l)


selection_sort(l)
print("SORTED", l)
