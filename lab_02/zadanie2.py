
#a
def print_names(names:list):
    for name in names:
        print(name)
print_names(["Ania","Wiktoria","Robert","Martyna","Wiktor"])
#b
def multiply_numbers_lc(numbers_list:list[int])->list[int]:
    return [x*2 for x in numbers_list]

def multiply_numbers_for(number_list:list[int])->list[int]:
    result = []
    for number in number_list:
        result.append(number*2)
    return result

print(multiply_numbers_lc([2,3,4,5,1]))
print(multiply_numbers_for([2,3,4,5,1]))

#c

def print_only_even(numbers:list[int]):
    for i in range(len(numbers)):
        if(numbers[i]%2==0):
            print(numbers[i])
        

print_only_even([1,2,3,4,5,6,7,8,9,10])

#d
def print_every_other(number_list:list[int]):
    result = [number_list[i] for i in range(len(number_list)) if i%2!=0 ]
    print(result)
print_every_other([1,2,3,4,5,6,7,8,9,10])


