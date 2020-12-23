# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    my_list = [[1, 8, 10], [20, 30], [40, 50]]
    my_list.append([1, 2, 3, 5])
    print(my_list)
    print(my_list[1][0])
    print(sum(sum(my_list[i]) for i in range(0, len(my_list))))  # to find sum of multi dimension list
    print(list(range(4)))
    print(list(range(2, 6)))
    print(list(range(2, 8, 2)))

    my_dict = {"Name": "Rizwan", "Roll Number": 31, 1: 18}
    print(my_dict['Name'])
    print(my_dict.keys())
    print(my_dict.values())
    print(len(my_dict))
    for key, value in my_dict.items():
        print(key, value)


if __name__ == '__main__':
    main()
