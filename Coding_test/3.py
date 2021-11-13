def solution(ings, menu, sell):
    answer = 0
    ings_dict = {}
    menu_dict = {}
    for i in ings:
        ing_name, ing_price = i.split()
        ings_dict[ing_name] = int(ing_price)
    for m in menu:
        menu_name, ing_list, menu_price = m.split()
        cost = 0
        for i in ings_dict.keys():
            cost += ing_list.count(i)*ings_dict[i]
        menu_dict[menu_name] = int(menu_price) - cost
    for s in sell:
        menu_name, sell_count = s.split()
        answer += menu_dict[menu_name] * int(sell_count)

    return answer


print(solution(["r 10", "a 23", "t 124", "k 9"], ["PIZZA arraak 145", "HAMBURGER tkar 180",
               "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"], ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))
