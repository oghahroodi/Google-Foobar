def solution(s):
    d = []

    for i in range(1, len(s)//2+1):
        if len(s)%i == 0:
            d.append(i)

    for i in d:
        flag = True
        for j in range(i):
            for k in range(len(s)//i):
                # print('i:', i, 'j:', j, 'k:', k)
                if s[j] != s[j+k*i]:
                    flag = False
                    break
        if flag:
            return len(s)//i
    return 1