# * gamze
# print("hello")

#! ✨Everything in Pyhton is class✨👇


# def print_types(data):
#     for i in data:
#         print(i, type(i))


# test = [122, "victor", [1, 2, 3], (1, 2, 3), {1, 2, 3}, True, lambda x: x]
# print_types(test)


# data yazan yer test demek oluyor
# 🏄‍♂️👆

#! ✨defining class✨👇
# *Pyhtonda class tanımlarken class keywordunu kullanıyoruz
# class Person:
#     name = "victor"
#     age = 33

# * 👆 Şuan burada ben pyhton da class oluşturmuş oldum.Ben bu kalıptan artık yeni objectler olusutabilirm.

# person1 = Person()
# person2 = Person()

# * 🎉👆Burada iki adet nesne yani object olusturdum.
# * Bu objeclere ✨intance✨ deniyor


# * 🎉Bu olusturmuş oldugum objectlere ✨intance ✨ de deniyor.
# * 🎉Bu nesnlere kalıptan oluşturdugum için kalıbın özelliğini tasır.
# print(person1.name)
# print(person2.age)


# * 🎉 kalıba bir özellik eklemek istersem ekleyebilirim👇
# Person.job = "developer"
# print(person1.job)

# class Meyveler:
#     name = "watermelon"
#     kg = 5


# meyve1 = Meyveler()
# meyve2 = Meyveler()
# * meryve1 ve meyve2 olarak object olusturmuş oluyoruz bu objectlerede intance diyoruz

# print(meyve1.name)
# print(meyve2.kg)

#!   ✨class attributes vs instance attributes:
# class Person:
#     name = "victor"
#     age = 33


# person1 = Person()
# person2 = Person()
# * 👆 iki tane yine intance oluşturdum Person classında

# * Bir instancelarımıza ekleyeceğimiz özellik diğer instancelarımızı etkilemiyor 👇
# person1.location = "turkey"
# print(person1.location)
# print(person2.location)
# * Yani;Burada person1 instance ıma ✨location = turkey'i ✨eklerken person2  intsance ım bundan etkilenmedi.
# * İnstancelarımda class'dan gelen ne varsa hepsi instancelarımda oluyorken, attribute'lerim sadece hangi instanceıma attribute u ekliyorsam sadece o attribute da oluyor.❤

#! ✨SELF keyword and methods
# * SELF hangi instance dan calısıyorsa onu temsil ediyor
# * Hangi instance i cagırırsak methodu o instance ın içindeki belirten methodu bana döndürmüş olur.

# class Person:
#     company = "clarusway"

#     def test(self):
#         print("test")


# person1 = Person()
# person2 = Person()

# person1.test()
# person2.test()

# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
# class Person:
#     company = "clarusway"

#     def test(self):
#         print("test")


#     def get_details(self):
#         print(f"{self.name} - {self.age}")


# person1 = Person()
# person2 = Person()

# person1.name="victor"
# person1.age=33
# person1.get_details()
# 👆 burada person1 instance ını cagırdıgımız için içinde ki methodu gelirdi.


# person2.name="henry"
# person2.age=18
# person2.get_details()
# 👆 Burada da person2 instanceımızıın içindeki metyhod gelirdi

# output:victor - 33
# Ve burada ki methodlar parametre almak zorunda yoksa hata verir dikkat et
# method ların içindeki self yazısını kasdediyorum
# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

# class Person:
#     company = "clarusway"

#     def test(self):
#         print("test")

#     def set_details(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(f"{self.name} - {self.age}")

# person1 = Person()
# person2 = Person()

# person2.set_details("henry", 15)
# 👆 Burada ki parametreler self,name,age  e  gitmiş oldu.
# person2.get_details()

# output:henry - 15
# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
# * eger değişmeyen sabit bir method istersek ✨@staticmethod✨ yazıcaz
# * ve bu @staticmethod u yazdgımızda artık self yazmamıza gerek kalmıyor
# * Yani staticmethodlar self  parametresi almazlar
# class Person:
#     company = "clarusway"

#     def test(self):
#         print("test")

#     def set_details(self, name, age):
#          self.name = name
#          self.age = age

#     def get_details(self):
#         print(f"{self.name} - {self.age}")

#     @staticmethod
#     def salute():
#         print("Hi Gamze!")


# person1 = Person()
# person2 = Person()


# person1.salute()

# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

#! Special methods(Dunder methods)
#! __init__ methodu
# * daha önceden tanımlanmış methodlardır.
# class Person:
#     company = "clarusway"

#     def set_details(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(f"{self.name} - {self.age}")


# person1 = Person()
# person1.set_details("victor", 33)
# person1.get_details()

# output:victor - 33

# * init methodu:instancelarımızı olusturuyorken otomatik olarak çalışır.
# *  Bu yukarıdaki methodu artık kısaca init methoduyla yapabiliriz.


# class Person:
#     company = "clarusway"

#     def __init__(self, name, age):
#             self.name = name
#             self.age = age

#     def get_details(self):
#             print(f"{self.name} - {self.age}")


# person1 = Person("victor", 33)
# person1.get_details()

# output:victor - 33

# * 👆burada yukarıda ki yaptıgımızı ✨__init__✨ methoduyla kısaca yapmış olduk.

# class Person:
#       company = "clarusway"

#       def __init__(self, name, age,gender="male"):
#               self.name = name
#               self.age = age
#               self.gender=gender

#       def get_details(self):
#               print(f"{self.name} - {self.age}")

# person1 = Person("victor", 33)
# person1.get_details()

# output:victor - 33 - male

# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

#! __str__ methodu
# *  str methodlarla ben instance larımın çıktısını görüntüsünü ayarlayabiliyorum
# * Yani ben instance larımın içine ne yazdıysam onu __str__ methoduyla görebiliyorum
# class Person:
#            company = "clarusway"

#            def __init__(self, name, age,gender="male"):
#                    self.name = name
#                    self.age = age
#                   self.gender=gender
# def __str__(self):
#     return f"{self.name} - {self.age}"
#            def get_details(self):
#                    print(f"{self.name} - {self.age}")

# person1 = Person("victor", 33)
# person2=Person("henry",33)

# print(person1)
# print(person2)
# output: victor - 33
#         henry - 33

#! OOP Principles (4 pillars)
# ✨#?Encapsulation
# ✨#?Abstraction
# ✨#?Inheritance
# ✨#?Polymorphism


# ✨# ?Encapsulation
# * kullanıcı tarafından classların,verilerin ve methodların ne kadarının görüntülenebileceğini, ne kadarınn değiştirebileceğini belirlediğimiz yapı.

# *public - private - protected
# *Bu getter settre methodlarını bu methotlara göre ayarlayıp kullanabiliyoruz.Mesela;
# * person1.name ="victor" u yukarıda gayet atadık ama name'i biz protected olarak ayarlasaydık direk değeri elimizi kolumuzu sallayarak busekilde atayamazdık.

# class Person:
#             company = "clarusway"

#             def __init__(self, name, age"):
#                     self.name = name
#                     self.age = age
#                     self._id = 5000
#                     # 👆Burada ✨_id✨ yapmamızın sebebi idnin basına altçizgi koymamızın sebebi idmizin private olması için
#                     # tek alt cizgi demek sadece bir uyarı değiştirirsem sıkınıt cıkarabilir uyarsı


#             def __str__(self):
#                 return f"{self.name} - {self.age}"


#             def get_details(self):
#                 print(f"{self.name} - {self.age}")

# person1 = Person("victor",33)
# print(person1._id)
# output: 5000

# person1._id = 4000
# print(person1._id)
# 👆Burada _id yi değiştirdik değiştirebiliriz ama sıkıntı cıkarabilir
