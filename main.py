def main():
    list_jump = list(map(int, input().split()))

    print(list_jump)
    i = 0
    list_road = []
    while i <= len(list_jump):
        max = [0, []]
        for k in range(1,list_jump[i]+1):
            c = i + list_jump[i+k]
            if c > max[0]:
                max[0] = c
                max[1] = [str(i) + "----->" + str(i+k)]

        i = max[0]
        list_road.append(max[1])

    for i in list_road:
        print(i[0])


if __name__ == '__main__':
    main()
