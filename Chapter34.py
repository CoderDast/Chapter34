def small_int(list_):
    for i in range(1, len(list_)+2):
        if i not in list_:
            res = i
            break
    return res







def main():
    my_list = input('Input number with useing space : ').split()
    try:
        my_list = list(map(int, my_list))
        res = small_int(my_list)
        print(res)
    except:
        print("Your inputing is not correct, try again, please! : ")
        main()

main()