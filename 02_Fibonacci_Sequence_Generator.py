"""

s.no: 2
Name: Fibonacci Sequence Generator
category: Python Programming
project_discretion: Create a function that generates the Fibonacci sequence up to a user-specified number of terms. The Fibonacci sequence is a series where each number is the sum of the two preceding ones (e.g., 0, 1, 1, 2, 3, 5, 8...). This introduces loops (for/while), functions, and recursion. You'll compare iterative and recursive approaches, learning about time complexity (e.g., recursive Fibonacci is O(2^n), iterative is O(n)).
Project requirements: {'language': 'Python', 'libraries': [], 'concepts': ['Functions', 'Loops', 'Recursion', 'Time complexity basics'], 'learn topics from': ['https://www.programiz.com/python-programming/function', 'https://realpython.com/python-recursion/']}
Time: 45
Difficulty: 25
"""

# Start your implementation here...
def main():


    print("Welcome to Fibonacci sequence generator.")
    num :str = input("Entre a number of term you want to generate:")

    try:
        num :int =int(num)
    except:
        print('Not a valid input')

    control_list=[0,1]
    print(control_list[0],control_list[1] , end=',')
    for i in range(num):
        control_list.append(control_list[len(control_list)-1]+control_list[len(control_list)-2])
        print(control_list[len(control_list)-1], end=',')

if __name__=="__main__":
    main()
