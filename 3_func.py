# def foo() -> None: #annotation return type None але може повернути будь-який тип. Це просто комент
#     pass #do nothing return None


# def multipl(x:int, y:int) -> int:
#     return x*y


# a = multipl(25, 235)
# print(a)
# # help('def')

# def mult_list(list:list) -> int:
#     result = 1
#     for el in list:
#         result *= el
#     return result



# numbers = [1, 12, 44, 4, 57, 8]
# print(mult_list(numbers))

def foo(a:int, b = 0, c = 0) -> int:
    return 100*a + 10*b + 1*c


def bar(args):
    '''Print all incoming arguments'''
    for arg in args:
        print(f'bar arg is: {arg}')
        
        
bar([2, 4, 6])  

def bar2(*args, named_parametr = 'done!'):# за замовчанням done
    for arg in args:
        print(f'bar arg is: {arg}, {named_parametr}')
        
        
bar2(1, 2, 5, 8, 'anything') #named_parametr за замовчанням
bar2(2, 16, 10, 20, 'cool', named_parametr='last one')#named_parametr вказали
# print(foo(1, 2, 3))
# print(foo(c = 1, b = 2, a = 3)) #named parametrs
# print(foo(1, 2)) # c declared in function
# print(foo(1))

help(bar)

