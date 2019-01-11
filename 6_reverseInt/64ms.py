neg = True if x < 0 else False
        s = str(x)[1:] if neg else str(x)
        x_ = int('-'+ s[::-1]) if neg else int(s[::-1])
        if x_ < 2**31 and x_ >= -(2**31):
            return x_
        else: 
            return 0