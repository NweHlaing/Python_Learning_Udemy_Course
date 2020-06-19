#Upper case and lower case string
def up_low(s):
    check={"upper":0, "lower":0}
    for data in s:
        if data.isupper():
            check["upper"]+=1
        elif data.islower():
            check["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", check["upper"])
    print("No. of Lower case Characters : ", check["lower"])

up_low_check = up_low("Hello Elsa. Nice to MeeT yoU")
# print("up_low_check....",up_low_check)