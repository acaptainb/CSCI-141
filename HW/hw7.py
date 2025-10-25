"""
CS1 Homework 7, 2251
Author: Tony Audi
Author: Abdulaziz Abbasov
"""

def hw7sort(nums, skip=31):  # do not change
    '''
    This is supposed to sort nums in place.
    '''
    if skip >= 1:
        for i in range(skip, len(nums)):
            save = nums[i]
            look = i
            while look >= skip and nums[look - skip] > save:
                nums[look] = nums[look - skip]
                look -= skip
            nums[look] = save
        hw7sort(nums, skip // 2)  # do not change

def test():
    '''
    Test the hw7 sort function.
    For each test case given, see if it is sorted after calling hw7sort on it.
    '''
    t1 = [1,2,3,4,5,6,7]  # [replace with a list of numbers]
    t2 = [1,2,0,9,3,4,8,7,5,6]  # [a different list]
    t3 = [12,34,54,65,234,65,243,-65,3]  # [and so on]
    t4 = [1,1,1,1,1,1,1,1,1]  # [think about what might fail]
    t5 = [7,6,5,4,3,2,1]  # [and succeed]
    # feel free to add more tests!
    for test in (t1, t2, t3, t4, t5):  # ,t6,t7,t8):
        new_test = test
        # you'll want to save the input since it's an in-place sort
        hw7sort(test)
        if test == sorted(new_test):  # how will you decide this?
            print('correct')
        else:
            # add in the list and what you got back to be helpful:
            print('failed')


if __name__ == "__main__":
    test()

