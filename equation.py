import math

# List of nums that have integer roots
valid_nums = []

# key = valid num, value = valid num exponential form (x^y)
nums_dict = {}

# Find nums that have integer roots up to one hundred million100000000
for num in range(1, 100000000):
    has_root = False
    temp = []
    for root in range(3,31):
        val = num ** (1 / root)
        if(math.isclose(val % 1, round(val % 1))):
            print(root, 'th root', sep = '')
            has_root = True
            temp.append(str(round(val)) + '^' + str(root))
    if(has_root):
        valid_nums.append(num)
        nums_dict[num] = temp
        print(num)
        print()

print(valid_nums)

# Create text file to hold output
with open("output.txt", "w") as output:
    output.write('List of equations where each number has integer roots\n\n')
output = open('output.txt', 'a')



# Check if two valid nums add up to another in the list
for i in range(len(valid_nums)):
    for q in range(len(valid_nums)):
        if(i > q):
            start = i
        else:
            start = q
        for test in range(start, len(valid_nums)):
            if(valid_nums[i] + valid_nums[q] == valid_nums[test]):
                print('found')
                print(valid_nums[i], valid_nums[q], valid_nums[test])
                print(nums_dict[valid_nums[i]][-1], '+', nums_dict[valid_nums[q]][-1], '=', nums_dict[valid_nums[test]][-1])
                print()

                output.write(f'found\n{valid_nums[i]} {valid_nums[q]} {valid_nums[test]}\n')
                output.write(f'{nums_dict[valid_nums[i]][-1]} + {nums_dict[valid_nums[q]][-1]} = {nums_dict[valid_nums[test]][-1]}\n\n')

output.close()
