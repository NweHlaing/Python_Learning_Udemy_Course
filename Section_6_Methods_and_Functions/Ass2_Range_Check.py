#Range check function
def ran_check(num,low,high):
    return num in range(low,high+1)

check_res = ran_check(5,4,7)
print("check_res",check_res)