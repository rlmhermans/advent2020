# card = 5764801
# door = 17807724

card = 9033205
door = 9281649

def find_loop_size(public_key):
    loop = 0
    value = 1
    while value != public_key:
        value *= 7
        value %= 20201227
        loop += 1
    return loop

def loop(size, nr):
    value = 1
    for _ in range(size):
        value *= nr
        value %= 20201227
    return value

print(loop(find_loop_size(card), door))