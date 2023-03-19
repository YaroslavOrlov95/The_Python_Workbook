
def encode_rle(lst):
    encoded_lst = []
    count = 1
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            encoded_lst.append(lst[i - 1])
            encoded_lst.append(count)
            count = 1
        else:
            count += 1
    encoded_lst.append(lst[-1])
    encoded_lst.append(count)
    return encoded_lst

def decode_rle(encoded_lst):
    decoded_lst = []
    for i in range(0, len(encoded_lst), 2):
        decoded_lst += [encoded_lst[i]] * encoded_lst[i+1]
        print(encoded_lst[i], encoded_lst[i+1], decoded_lst, i)
    return decoded_lst

lst = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
encoded_lst = encode_rle(lst)
print(encoded_lst)  # ['A', 12, 'B', 4, 'A', 6, 'B', 1]

decoded_lst = decode_rle(encoded_lst)
print(decoded_lst)  # ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B']
