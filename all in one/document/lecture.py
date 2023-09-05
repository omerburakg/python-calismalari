# file = open("C:/Users/omerb/Desktop/well well well/projeler/kodlama_egzersizleri/document/bilgiler.txt","w",encoding="UTF-8") --- dosya adi (dizinli ya da dizinsiz) ve işlem ve utf
# KODUN SONUNDA DOSYAYI KAPATMAYI UNUTMA! DOSYA BAZEN KAPANMAYABİLİR VE SİSTEM KAYNAKLARINI GEREKSİZ YERE HARCAR.
# Dosyaya alt alta yazmak için yazdıktan sonra \n koymayı unutma.
# "w" >>> writing , yeni dosya açar ve aynı isimde dosya varsa yeni dosya açıp üstüne yazar. Eski dosya silinir.
# "a" >>> append , mevcut olan dosyaya gidip üzerinde değişiklik yapmaya yarar. Kip en sona gider.
# "r" >>> reading, mevcut dosyayi okumayi sağlar.
# "r+">>> Hem okumayi, hem de değişiklik yapmayı sağlar.
try:
    file = open("bilgiler2", "r")
except FileNotFoundError:
    print("Dosya Bulunamadi..")

# dosyanın ortasında bir yere satır eklemek için readlines() fonksiyonunu ve writelines() fonksiyonunu kullanabiliriz.
