def find_exp(num):
    exp = 0
    while num != 1:
        num /= 3
        exp += 1
    return exp

def level_up(arr):
    old_size = len(arr[0])
    new_size = len(arr[0])*3
    new_arr = [[False] * new_size for _ in range(new_size)]
    
    for nx in range(3):
        for ny in range(3):
            for ox in range(old_size):
                for oy in range(old_size):
                    if nx == 1 and ny == 1: continue
                    new_arr[(old_size*nx)+ox][(old_size*ny)+oy] = arr[ox][oy]
    
    return new_arr

def print_arr(arr):
    for i in arr:
        for l in i:
            print("*" if l == True else " ", end="")
        print()
    return

num = int(input())
exp = find_exp(num)

base_arr = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
for i in range(exp-1):
    base_arr = level_up(base_arr)

print_arr(base_arr)