#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")



def square_integers(int_list):
    return [num * num for num in int_list]
        
    

def fizzbuzz():
    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    print("happy_new_year():")
    happy_new_year()

    print("\nsquare_integers([1, 2, 3, 4, 5]):")
    print(square_integers([1, 2, 3, 4, 5]))

    print("\nfizzbuzz():")
    fizzbuzz()
