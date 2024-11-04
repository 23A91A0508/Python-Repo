from math import sqrt
def check_pronic(no):
    sr=int(sqrt(no))
    return sr*(sr+1)==no
given_num=int(input())
if check_pronic(given_num):
    print("YES")
else:
    print("NO")