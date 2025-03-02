# Interview question at Tableau Software
# Given a list, return a list of elements that have duplicates
# Input: [1,2,3,4,1,2]
# Output: [1,2]

def find_duplicates(iterable):
    counter = {}
    duplicates_list = []
    for item in iterable:
        counter.setdefault(item, 0)
        counter[item] += 1
        if counter[item] == 2:
            duplicates_list.append(item)

    return duplicates_list

li = [1,2,3,4,1,2,1,3,5,4,6,7]
li = [2,1,2,3,1,4]
print find_duplicates(li)