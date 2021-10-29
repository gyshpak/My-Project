
# def dirReduc(arr):
#     my_pair = []
#     my_pair.append("0,0")
#     x = 0
#     y = 0
#     for i in arr:
#         delt_x = 0
#         delt_y = 0
#         if i == 'WEST':
#             delt_x = -1
#         elif i == "EAST":
#             delt_x = 1
#         elif i == "NORTH":
#             delt_y = 1
#         else:
#             delt_y = -1
#         x += delt_x
#         y += delt_y
#         my_pair.append(f"{x},{y}")
#     return my_pair



# my_list = ["NORTH", "WEST", "SOUTH", "EAST"]
# my_simply_lisy = dirReduc(my_list)
# print(my_simply_lisy)

# def dirReduc(arr):
    # for i in range(len(arr)):
    #     if arr[i] == "NORTH":
    #         arr[i] = 1
    #     if arr[i] == "SOUTH":
    #         arr[i] = -1
    #     if arr[i] == "WEST":
    #         arr[i] = 2
    #     if arr[i] == "EAST":
    #         arr[i] = -2
    
    # for i in range(len(arr)):
    #     if abs(arr[i])==abs(arr[i+1]):

# def dirReduc(arr):
#     n = 0
#     i = 0
#     while n == 0:
#         if len(arr) < 2:
#             return arr
#         n = 1
#         if arr[i] == 'NORTH' and arr[i+1] == "SOUTH" or arr[i] == 'SOUTH' and arr[i+1] == "NORTH" or \
#             arr[i] == 'WEST' and arr[i+1] == "EAST" or arr[i] == 'EAST' and arr[i+1] == "WEST":
#             del arr[i:i+2]
#             n = 0
#             i = 0
#             continue
#         if i+2 < len(arr):
#             i += 1
#             n = 0
#     print("vozvrat", "n=", n)
#     return arr

# my_list = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# my_simply_lisy = dirReduc(my_list)
# print(my_simply_lisy)


# def find_nb(m):
#     n = 0
#     i = 0
#     while m > i:
#         i += n**3
#         n += 1
#     if m == i:
#         return n - 1
#     else:
#         return "-1"

# m = 1071225
# m = 91716553919377
# m = 24723578342962
# print(find_nb(m))

# def permutations(string):
#     my_str = []
#     out_str = []
#     tmp_list = [i for i in string]
#     # print(tmp_list)
#     if len(string) == 1:
#         return list(string)
#     while string != my_str:
#     # for j in range(len(string)):
#         for i in range(len(string)-1):
#             tmp_list[i], tmp_list[i+1] = tmp_list[i+1], tmp_list[i]
#             my_str = ''.join(tmp_list)
#             out_str.append(my_str)
#             # print(out_str)
#             print(my_str)
#         # string = my_str
#     #out_str = list(set(out_str))
#     return out_str


# first_str = 'abcd'
# first_str = 'aabb'
# first_str = 'a'
# first_str = 'ijbcf'
# # print(permutations(first_str))
################################################################
# out_str = []
# def permutations(string):
#     global out_str
#     if len(string) > 1:
#         tmp_list = [string[0], string[1:]]
#         out_str.append(tmp_list)

#         print(''.join(tmp_list))
#         if len(string[1:])>1:
#             out_str = permutations(string[1:])
    
#     return out_str


# first_str = 'abcd'
# first_str = 'aabb'
# first_str = 'an'
# first_str = 'ijbcf'
# print(permutations(first_str))
####################################################################

def permutations(string):
    my_len_str = len(string)
    my_set = list(set(string))
    my_count_el = len(my_set)
    # my_summ = str(my_count_el-1)*my_len_str
    # my_summ_x = int(my_summ,my_count_el)
    # my_sort = sorted(string)
    my_sort = []
    # tmp_sort = ['d','t']
    tmp_sort = []
    # tmp_sort.append(my_sort)
    # my_start_str = {i: my_set[i] for i in range(my_count_el)}
    # i = my_summ_x
    # for j in range(my_len_str):
    for i in range(my_len_str):
        my_sort[i] = my_set[0]

    j = 0
    i = 0
    while j < my_len_str:
        while i < my_count_el:
            my_sort[j] = my_set[i]
            a = list(my_sort)
            tmp_sort.append(a)
            i =+ 1
            if j>0 and i<my_count_el:
                j -= 1
                i = 0
                
        i = 0    
        j += 1
        

    return tmp_sort

# # first_str = 'abcd'
# # first_str = 'aabb'
first_str = 'abc'
# # first_str = 'ijbcf'
print(permutations(first_str))
# permutations(first_str)

