int_input = int(input())
for index in range(int_input):
    string_input = input()
    print("".join(string_input[::2]), "".join(string_input[1::2]))