import requests
from datetime import date
def calc_age(uid):
    cake=dict()
    stri='https://api.vk.com/method/friends.get?v=5.120&access_token=da9daaccda9daaccda9daacc8bdaee824cdda9dda9daacc8584977ab2b7f9f1e029bf22&fields=bdate&user_id='+str(uid)
    feedback = requests.get(stri)
    for ant in feedback:
        for pride in ant:
            print ()
    for bdate in feedback["response"]["items"]:
                a=list(int(cdate[bdate].split('.')))
                if (a.len())<=int(2):
                    pass
                else:
                    for i in range (3):
                        a[i]=a[i]-today[i]
                        if a[i]<=-1:
                            a[2]-=1
                    if a[2] in cake:
                        cake[a[2]]+=1
                    else:
                        cake[a[2]]=1
    return sorted(cake)


today = (str(date.today()).split('-'))
res=dict()
uid=input()
#if uid.issnumeric():
    #pass
#else:
    #uid = requests.get('https://api.vk.com/method/users.get',screen_name=uid)[id]
    #print ('unsupported')
    #pass
if __name__ == '__main__':
    res = calc_age(uid)
    print(sorted(res))
