import random

list_ = []
t = 0
while t != 1:
    OP_list = ["O", "P"]
    x = random.choice(OP_list)

    list_.append(x)
    OP_ = len(list_) - 1
    OP_m = OP_ - 1
    OP_m_m = OP_m - 1

    if len(list_) >= 3:
        if list_[OP_] == list_[OP_m] == list_[OP_m_m]:
            t = 1
            print(*list_,f' (попыток: {len(list_)})')
    else:
        pass