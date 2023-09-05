# PYTHON NOTLARI

## Operators
- \   : Kaçış İşareti
- **  : Üs alma
- //  : Tam bölen
- %   : Mod Alma
- \n  : Bir Satır Aşağı İnme
- \t  : Bir tab boşluk
- +, -, *, /: Metamatik işlemleri

```python
print("""this
is a
multiline
text""")
#Bu da bir \n alternatifidir. Üç tırnak (""") konulduğu zaman python cümle biçimine dikkat eder.
```
- Inputla aldığımız değerler sayı olsa bile str olarak çıkar.

- print(num:=int(input()))       Kolay yoldan var atama 

- Python'un işlem sırası normal matematiğinkiyle aynıdır; önce parantezler, sonra üs alma, sonra çarpma/bölme ve ardından toplama/çıkarma.
---
## List [ ]
- The first list item's index is 0, rather than 1, as might be expected.
- To check if an item is in a list, the in operator can be used. It returns True if the item occurs one or more times in the list, and False if it doesn't.

```python
liste = ["spam", "egg", "spam", "sausage"]
print("egg" in liste)       #True
print("tomato" in liste)    #False
print("spam" in liste)      #True
```


## List Functions
- .sort : The sort() method sorts the list ascending by default.
- .sort(reverse = True) : To get reverse of the list. It's depended.
- .append : The append method adds an item to the end of an existing list.
- For example: var.append("word")
- len     : To get the number of items in a list, you can use the len function.
- For example:  var(len)
- .insert : The insert method is similar to append, except that it allows you to insert a new item at any position in the list, as opposed to just at the end.
- For example:

```python
words = ["Python", "fun"]
index = 1 
words.insert(index, "is")
print(words)     #Output: ['Python', 'is', 'fun'] because of index variable.
```
---
## Tuple ( )
- A tuple is a collection which is ordered and unchangeable.
- Tuples are used to store multiple items in a single variable.
- Tuples are used to store items because tuples can not be changed at all.

## Tuple Functions
* .count : The count() method returns the number of elements with the specified value.
- For Example:
```python
demet = (1,1,1,1,1,2,2,4,5)
demet.count(1)   #5
demet.count(5)   #1
demet.count(10)  #0   - If the variable doesn't exist in tuple, you getting 0 on console.
```
- .index : The index() method shows variables index number.
- For Example:

```python
demet2 = ("Python", "Php", "C", "Java")
demet2.index("Java")     #3
demet2.index("AngularJS")    #ValueError: tuple.index(x) not in tuple
```

## Dictionary { }
* Dictionaries are used to store data values in key:value pairs.
- The values in dictionary items can be of any data type:

```python
new_dict = {"sayi":{"bir":1, "iki":2, "uc":3,}, "meyveler":{"kiraz":"yaz", "portakal":"kıs", "erik":"yaz"}}
print(new_dict["sayi"["iki"]])           # That line returns '2' value.
```
## Dictionary Functions
- .keys() : Returns a list containing the dictionary's keys.
- For Example:
```python
print(new_dict.keys())           # Output: dict_keys(['sayi', 'meyveler'])
print(new_dict["sayi"].keys())   # Output: dict_keys(['bir', 'iki', 'uc'])
```
- .values() : Returns a list of all the values in the dictionary.
- For Example:
```python
print(new_dict.values())             
# Output : dict_values([{'bir': 1, 'iki': 2, 'uc': 3}, {'kiraz': 'yaz', 'portakal': 'kıs', 'erik': 'yaz'}]) 
print(new_dict["meyveler"].values())
# Output : dict_values(['yaz', 'kıs', 'yaz'])
```
- .items() : Returns a list containing a tuple for each key value pair.
- For Example:
```python
print(new_dict.items())
# Output: dict_items([('sayi', {'bir': 1, 'iki': 2, 'uc': 3}), ('meyveler', {'kiraz': 'yaz', 'portakal': 'kıs', 'erik': 'yaz'})])
print(new_dict["sayi"].items())
# Output: dict_items([('bir', 1), ('iki', 2), ('uc', 3)])
```
---

