data="Hellow world"
print(data[1:]) #last value will not print
print(data[-1:])
print(data[6:])
print(data[6])
print(data.index("world"))
#data.replace
mail_id="bala.88@gmail.com"
print(mail_id[mail_id.index('@') + 1 : ])
print(mail_id.split("@")[0])
print(mail_id[0:mail_id.index("@")])
res=mail_id.split("@")
print(res)