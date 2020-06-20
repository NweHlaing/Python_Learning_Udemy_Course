def user_input():

    #Variable Declaration
    input_data = 'Check'
    check_range = range(0,10)
    within_range = False

    #Type and range check
    while input_data.isdigit() == False or within_range == False:
        input_data = input("Please Enter data bet(0-10): ")
        #Type Check
        if input_data.isdigit() == False:
            print("Sorry! your input is not a digit!!!!")
        #Range Check
        if input_data.isdigit() == True:
            if int(input_data) in check_range:
                within_range = True
            else:
                print("Sorry! your input is out of range!!!")
                withn_range = False
    return int(input_data)

user_input()