

def find(ordered_list, find_element):
    start_index =1
    end_index = len(ordered_list) -1
    
    print(ordered_list, find_element)
    

    while True:
        middle_index = int((start_index + end_index)/2)
        if middle_index == start_index or middle_index == end_index:
            if (ordered_list[middle_index] == find_element or ordered_list[end_index] == find_element):
                return True
            else:
                return False
            
        middle_element = ordered_list[middle_index]
        
        
        if middle_element == find_element:
            return True
        elif middle_element > find_element:
            end_index = middle_index
        else:
            start_index = middle_index


if __name__ == "__main__":

    l = [2, 4, 5, 8, 10]

    print(find(l, -1))
    print(find(l, 0)) 
    print(find(l, 2))
    print(find(l, 3))
    print(find(l, 4)) 
    print(find(l, 5)) 
    print(find(l, 6)) 
    print(find(l, 7))
    print(find(l, 8))
    print(find(l, 9))
    print(find(l, 10)) 
    print(find(l, 11))
    print(find(l, 6.5)) 


