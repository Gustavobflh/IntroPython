def breakfor(s):

    for i in s:
        if i % 2 == 1 :  # If the number is odd
        break        #  ... immediately exit the loop
    return i
print(breakfor(s))
