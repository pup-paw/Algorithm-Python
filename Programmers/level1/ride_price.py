def solution(price, money, count):
    price *= (count + 1) * count / 2
    # return price - money if price > money else 0
    return max(0, price-money)


print(solution(3, 20, 4))
