def solve(equation):
    num = equation.split('+')
    nums = num[1].split('=')
    x = int(nums[1].strip()) - int(nums[0].strip())
    print('The value of X is', str(x))


equation = input("Enter the equation : ")
solve(equation)
