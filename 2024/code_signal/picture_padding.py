# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# Example

# For

# picture = ["abc",
#            "ded"]
# the output should be

# solution(picture) = ["*****",
#                      "*abc*",
#                      "*ded*",
#                      "*****"]

def solution(picture):
    a = "*"
    for i in range(len(picture)):
        picture[i] = a + picture[i] + a
    a_row = a*len(picture[0])
    picture.insert(0, a_row)
    picture.append(a_row)
    return picture