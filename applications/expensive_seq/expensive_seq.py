ans_dict = dict()

def expensive_seq(x, y, z):
    if ans_dict.get(f'{x},{y},{z}'):
        return ans_dict[f'{x},{y},{z}']

    if x <= 0:
        return y + z
    else:
        # calculate and store each recursive call
        first = expensive_seq(x-1,y+1,z)
        second = expensive_seq(x-2,y+2,z*2)
        third = expensive_seq(x-3,y+3,z*3)
        ans_dict[f'{x-1},{y+1},{z}'] = first
        ans_dict[f'{x-2},{y+2},{z*2}'] = second
        ans_dict[f'{x-3},{y+3},{z*3}'] = third
        ans_dict[f'{x},{y},{z}'] = first + second + third
    return ans_dict[f'{x},{y},{z}']

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
