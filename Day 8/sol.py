# Enter your code here. Read input from STDIN. Print output to STDOUT0p
number_of_inputs = int(input())
name_number = [input().split() for num in range(number_of_inputs)]
phone_book = {key:value for key,value in name_number}
while True:
    try:
        name = input()
        if name in phone_book:
            print(f'{name}={phone_book[name]}')
        else:
            print('Not found')
    except:
        break 