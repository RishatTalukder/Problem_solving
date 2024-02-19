list_of_nums = [1,2,3,4,5,6,7,8,9,10]
counter = 0

for i in list_of_nums:
        counter += 1
        if counter%2 == 0:
            list_of_nums.remove(i)

        print(list_of_nums)

