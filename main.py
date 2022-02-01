import os, random
from timeit import default_timer as timer

print('Welcome to a program that writes another program that is extremely inefficient!')

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    while True:
        try:
            lines = int(input('How long would you like the program to be. Total lines: '))
            
            start = timer()
            with open(f"{path}\program.py", 'w') as file:
                for i in range(lines-1):
                    number = random.randint(0, lines)
                    file.write(f'print("{number} + 1 = {number+1}") \n')
                
            end = timer()
            print(f"It took {end-start} second(s) to write the program with {lines} total lines.")
            
        except ValueError:
            print('Invalid input. Try again.')
            
if __name__ == '__main__':
    main()