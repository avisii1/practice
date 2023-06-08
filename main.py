# def summation(a, b):
#     c = a + b + 3
#     return c
#
#
# print(f"sum is {summation(11, 11)}")
#
# assert summation(2, 3) == 5, 'there seems to be some issues'
# print("everything appears to be good")

def list_test(some_list):
    return some_list


check_info = list_test([2, 4, 5, 6, 22, 11])
print(check_info)

assert list_test([1, 2]) == [1, 2], 'issue is there'
print("Everything is alright")
