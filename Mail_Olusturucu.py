import random

def mailcreate(nickname, mailtype="gmail.com", add_random=False):
    if add_random:
        # Rastgele 3 basamaklı bir sayı oluştur
        random_suffix = ''.join(random.choices('0123456789', k=3))
        mailadresi = f"{nickname}{random_suffix}@{mailtype}"
    else:
        mailadresi = f"{nickname}@{mailtype}"
    return mailadresi

nickname = input("Lütfen kullanıcı adını giriniz: ")
mail = input("Lütfen mail tipini giriniz (örn. gmail.com): ")
add_random = input("Mail adresine rastgele sayılar eklemek ister misiniz? (e/h): ").lower() == 'e'

if mail:
    print("Mail adresi:", mailcreate(nickname, mail, add_random))
else:
    print("Mail adresi:", mailcreate(nickname, add_random=add_random))