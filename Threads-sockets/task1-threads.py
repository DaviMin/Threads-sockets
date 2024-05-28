# User types in values in  a list. After that, two threads start.
# The first thread finds the largest value in the list.
# The second thread finds the smallest value in the list.
# The results are displayed on the screen.

import time
import threading

def find_largest(numbers):
    largest = max(numbers)
    print("Largest value:", largest)

def find_smallest(numbers):
    smallest = min(numbers)
    print("Smallest value:", smallest)

# Main function
def main():
    # User input for list of values
    values = input("Enter values separated by space: ").split()
    numbers = [int(num) for num in values]

   #  se používá k rozdělení textového řetězce na podřetězce (slova) podle oddělovače.
    #  Pokud není specifikován žádný oddělovač, použije se implicitně mezera. V tomto případě

    # Creating and starting threads
    thread1 = threading.Thread(target=find_largest, args=(numbers,)) # args = argument ypredane funkci
    thread2 = threading.Thread(target=find_smallest, args=(numbers,))
    thread1.start()
    thread2.start()

    # Waiting for threads to finish
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
