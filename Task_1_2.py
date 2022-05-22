def odd_cube():
    new_list = []
    second_list = []
    third_list = []
    fourth_list = []

    for i in range(1, 1000):
        if i % 2 != 0:
            new_list.append(i ** 3)
    print(new_list)
    for j in new_list:
        if j % 7 == 0:
            second_list.append(j)
    print(second_list)
    sum_list = sum(second_list, 0)
    print(sum_list)
    for i in new_list:
        third_list.append(i + 17)
    print(third_list)
    for n in third_list:
        if n % 7 == 0:
            fourth_list.append(n)
    print(fourth_list)
    sum_list1 = sum(fourth_list, 0)
    print(sum_list1)

odd_cube()
