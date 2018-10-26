def counter(n):
    count = 0
    count_5 = 0
    while n!=0:
        count = count + 1
        n = n // 10     
        p = n / 5

        if p % 5 == 0:
            count_5 = count_5 + 1  
  
    return count_5

print(counter(300548126462015451654))
