names = ["Alex","John","Mary","Steve","John", "Steve"]

names_copy = []

def remove_duplicates():
    for index in names:
         if index not in names_copy:
            names_copy.append(index)
    print (f'Duplicates :        {names}')
    print (f'Duplicates Removed: {names_copy}')
    return

remove_duplicates()