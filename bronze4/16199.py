b_year, b_month, b_day = map(int, input().split())
t_year, t_month, t_day = map(int, input().split())

if b_month < t_month:
    age1 = t_year - b_year
elif b_month == t_month and b_day <= t_day:
    age1 = t_year - b_year
else:
    age1 = t_year - b_year - 1

age2 = t_year - b_year + 1
age3 = t_year - b_year

print(age1)
print(age2)
print(age3)
