from datetime import date

import requests

bdate = 'bdate'
response = "response"
items = "items"
ide = "id"


def calc_age(ident):
    cake = dict()
    bake = dict()
    address = 'https://api.vk.com/method/friends.get?v=5.120&access_token=da9daaccda9daaccda9daacc8bdaee824cdda9dda9daacc8584977ab2b7f9f1e029bf22&fields=bdate&user_id=' + str(
        ident)
    maxi = 1
    feedback = requests.get(address)
    calender = dict(feedback.json())
    for l in calender[response][items]:
        try:
            a = l[bdate]
            a = a.split(".")
            if int(len(a)) <= int(2):
                pass
            else:
                for i in range(3):
                    a[i] = int(today[2 - i]) - int(a[i], 10)
                    if a[i] <= -1 and i != 2:
                        a[i + 1] -= 1
                if a[2] in cake:
                    cake[a[2]] += 1
                    if int(cake[a[2]]) >= maxi:
                        maxi = int(cake[a[2]])
                else:
                    cake[a[2]] = 1
        except:
            pass
    pass
    for j in range(maxi, 0, -1):
        for i in sorted(cake):
            if int(cake[i]) == j:
                bake[i] = j
    return bake


today = (str(date.today()).split('-'))
res = dict()
uid = input()
if uid.isdigit():  # Если на входе не ID, то пытается найти по поиску пользователей
    pass
else:
    get_id = ("https://api.vk.com/method/users.get?user_ids=" +
              str(uid) +
              "&access_token=da9daaccda9daaccda9daacc8bdaee824cdda9dda9daacc8584977ab2b7f9f1e029bf22&v=5.120")
    rep = requests.get(get_id)
    rep = dict(rep.json())
    uid = rep[response][0][ide]
if __name__ == '__main__':
    res = calc_age(uid)
    print(res)
