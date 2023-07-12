"""
without list comprehension we need for loop 
with list comprehension we can do all in only line of code
"""
# without list comprehension 
country = ['India','usa','japan']
country1 = []
for i in country:
    if 'I' in i:
        country1.append(i)
print(country1)

#with list comprehension
country2 = ['india','uk','usa','china']
country3 = [i for i in country2 if 'u' in i]
print(country3)
rollno = [i for i in range(20)]
print(rollno)
rollno1 = [i for i in range(20) if i<7]
print(rollno1)

#with list comprehension
currency = ['usd','inr','yen']
currency1 = [i.upper() for i in currency]
print(currency1)

currency2 = ['USD','INR','YEN']
currency3 = [i.lower() for i in currency2]
print(currency3)

currency4 = ['usd','inr','yen']
currency5 = ['INDIAN RUPEES' for i in currency4]
print(currency5)