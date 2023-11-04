import statistics


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    sort_temperature(num_list)
    calc_median_temperature(num_list)


def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5,67,32)")

def get_user_input():
    x = input()
    x = x.split(',')
    list_x = list(map(float, x))
    print(list_x)
    return list_x


def calc_average(num_list):
    value = num_list
    average = sum(value) / len(value)
    print("Average temp is " + str(round(average,2)))
    return average


def find_min_max(num_list):
    val = num_list
    val.sort()
    min = val[0]
    max = val[-1]
    print("Min temp is " + str(min))
    print("\nMax temp is " + str(max))
    return min, max


def sort_temperature(num_list):
    listt = num_list
    listt.sort()
    print("Sorted list is " + str(listt))
    return listt


def calc_median_temperature(num_list):
    templist = num_list
    median = statistics.median(templist)
    print("Median temp is " + str(median))
    return median


if __name__ == "__main__":
    main()
