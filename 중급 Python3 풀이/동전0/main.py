input_num =  [int(x) for x in input().split(" ")]
coin_count = input_num[0]
price = input_num[1]

coins = []
for _ in range(coin_count):
    coins.append(int(input()))

coins.reverse()

ans = 0

for coin in coins:
    if price >= coin:
        ans += int(price/coin)
        price = price%coin

    if price == 0:
        break

print(ans)