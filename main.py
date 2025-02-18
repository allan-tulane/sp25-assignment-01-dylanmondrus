"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x<= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb
    pass

def longest_run(mylist, key):
    longest = 0
    current = 0

    for i in mylist:
        if i == key:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    if not mylist:
        return Result(0, 0, 0, False)

    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0,0,0, False)

    mid = len(mylist) // 2
    left_result = longest_run_recursive(mylist[:mid], key)
    right_result = longest_run_recursive(mylist[mid:], key)

    cross_run = 0
    if mylist[mid - 1] == key and mylist[mid] == key:
        cross_run = left_result.right_size + right_result.left_size

    longest_size = max(left_result.longest_size, right_result.longest_size, cross_run)

    left_size = left_result.left_size
    if left_result.is_entire_range and mylist[mid] == key:
        left_size = left_result.left_size + right_result.left_size

    right_size = right_result.right_size
    if right_result.is_entire_range and mylist[mid - 1] == key:
        right_size = right_result.right_ize + left_result.right_size

    is_entire_range = left_result.is_entire_range and right_result.is_entire_range and all(x == key for x in mylist)

    return Result(left_size, right_size, longest_size, is_entire_range)

    pass



