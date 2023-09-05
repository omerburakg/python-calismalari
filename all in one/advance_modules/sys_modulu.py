import sys

# sys.exit() #program bu metni yorumladığı an sonlandırılır.

"""
stder ve stdout

Bilgisayarlar uygulamalarımız ve işlemlerimiz çalıştığı zaman çıktı vermek ve girdi almak için şu dosyaları kullanır:

stdin  : Bu standart dosya, işlemimizin (process) kullanıcıdan alınmasını sağlar.
stdout : Bu standart dosya, işlemimizin (process) çıktı vermesini sağlar.
stderr : Bu standart dosya, işlemimizin hata mesajını çıktı olarak vermek için kullanılır.

Biz print() fonksiyonunu kullandığımızda aslında standart olarak stdout kullanılmaktadır. Ancak biz istersek *stderr'e de bir şey yazabiliriz.
"""

# sys.stderr.write("Bu bir hata mesajıdır.\n")       #hata mesajı olarak yazdırdık.
# sys.stderr.flush()                               # stderr den sonra yapılmalı.

# sys.stdout.write("Bu normal bir yazıdır.\n")       #normal çıktı olarak yazdırdık.

# for i in sys.argv:                  # terminal'de istenilen sys klasörü açılır.python sys_project_name 1 2 3 4 5
    # print(i)

# print(sys.argv)                #


# stderr sadece hatalarda kullanılır. try except ise programın sona ermemesi için kullanılır.