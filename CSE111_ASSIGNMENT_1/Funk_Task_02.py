# Solution to Task 2 (Function):

def special_adder(start, stop, step):
    result_sum = 0
    for i in range(start, stop, step):
        result_sum += i
    print(result_sum)

if __name__ == "__main__":
    start, stop, step = [int(i) for i in input().strip("() ").split(",")]
    special_adder(start, stop, step)