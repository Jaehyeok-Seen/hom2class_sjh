coin_list = [500,100,50,10]
target = 1730
count = 0

for coin in coin_list:
    possible_count = target // coin

    count += possible_count
    target -=  coin*possible_count
print(count)