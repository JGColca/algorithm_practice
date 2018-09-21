array = ["wes", "score","night", "flight", "two", "to"]
word = max(array)


def largest_element(word):
    for index in range(len(array)):
        if len(array[index]) < len(word):
            word = array[index]
    return word

print(largest_element(word))

array = [-5,1,2,3,4,5,-100]
number = max(array)

def largest_element(number):
    for index in range(len(array)):
        if array[index] < number:
            number = array[index]
    return number

print(largest_element(number))