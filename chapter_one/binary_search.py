def binary_search(list, item):

    # pointers to keep track of section of list to be sarched in
    low = 0
    high = len(list) - 1


    while low <= high:
        # checking middle element
        mid = (low + high) / 2
        guess = list[mid]
        # guess was correct return ans
        if guess == item:
            return mid
        # guess was too hgiht
        if guess > item:
            high = mid - 1
        # guess was to low so we up out low variable
        else:
            low = mid + 1
    # item not found
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))