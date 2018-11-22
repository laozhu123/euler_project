def is_concealed(helo):
    for i in range(9):
        if int(helo[2*i]) != i+1:
            return False
    return True


def compute():
    for i in range(100000003,150000000,10):
        helo = pow(i,2)
        if is_concealed(str(helo)):
            print(i*10)
            return
        helo = pow(i+4,2)
        if is_concealed(str(helo)):
            print((i+4)*10)
            return

compute()