#Unique number
def unique_list(l):
    data_list = []
    for data in l:
        if data not in data_list:
            data_list.append(data)
    return data_list
unique_check = unique_list([1,5,3,3,3,4,5,6,6,7,3,6])
print("unique_check...",unique_check)