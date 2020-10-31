import random

if __name__ == "__main__":
    chars = ['r']*5 + ['b']*5 + ['g']*5 + [' ']
    random.shuffle(chars)
    state = "".join(chars[0:4]) + '|' + "".join(chars[4:8])+ '|' + "".join(chars[8:12])+ '|' + "".join(chars[12:16])
    print("\"" + state + "\"")