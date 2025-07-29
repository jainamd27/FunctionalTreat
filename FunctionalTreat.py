inp = []
data = []


def inp_data():
    global data  # Add this line to modify the global data list
    print("Enter data for a 1D array (Should be separated by spaces):")
    inp = input()
    print("Data has been stored successfully!")
    inp = inp.split(sep=" ")
    data = list(map(int, inp))


def data_summary():
    print("Data Summary:")
    print(f"- Total Elements: {len(data)}")
    print(f"- Minimum value: {min(data)}")
    print(f"- Maximum value: {max(data)}")
    print(f"- Sum of all value: {sum(data)}")
    print(f"- Average value: {(sum(data))/len(data)}")


def factorial():
    n = int(input("Please enter a number to find its factorial value"))
    if n < 0:
        print("Factorial not defined..")

    elif n == 0:
        print("Factorial of 0 is 1")

    else:
        res = 1
        for i in range(1, n+1):
            res *= i
        print(f"Factorial of {n} is: {res}")


def filter_data():
    global data
    th = int(input("Enter a threshold value to filter out data below this value: "))
    data_up = data
    data_up = [el for el in data_up if el > th]
    print(f"Filtered Data: {data_up}")


def data_sorter():
    print("Choose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        sort_dat = sorted(data)
        print(f"Sorted Data in Ascending Order: {sort_dat}")
    elif choice == 2:
        sort_dat = reversed(sorted(data))
        print(f"Sorted Data in Descending Order: {sort_dat}")
    else:
        print("Invalid input!!")


def stats():
    print("Dataset Statistics:")
    print(f"- Minimum value: {min(data)}")
    print(f"- Maximum value: {max(data)}")
    print(f"- Sum of all value: {sum(data)}")
    print(f"- Average value: {(sum(data))/len(data)}")


while True:
    print("Welcome to the Data Analyzer and Transformer Program")

    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        inp_data()
    elif choice == 2:
        data_summary()
    elif choice == 3:
        factorial()
    elif choice == 4:
        filter_data()
    elif choice == 5:
        data_sorter()
    elif choice == 6:
        stats()
    elif choice == 7: 
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break
    else:
        print("Invalid Input!!")
        break
