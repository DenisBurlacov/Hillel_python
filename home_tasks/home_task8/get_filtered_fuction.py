def get_filtered(a):
    result = []
    for i in a:
        if i < 5:
            result.append(i)
    print(result)


a = [1, 2, 3, 1, 4, 5, 6, 7, 8]
get_filtered(a)
