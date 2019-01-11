i, j, k = 0,0,0
        n = len(s)
        op = [[] * i for i in range(numRows)]
        while k < n:
            while i < numRows and k < n:
                op[i].append(s[k])
                i += 1
                k += 1
            j = i - 2
            # print(op)
            while j >= 0 and k < n:
                op[j].append(s[k])
                j -= 1
                k += 1
            i = j + 2
            # print(op)
        res = ''
        for row in op:
            for c in row:
                res += c
        return res