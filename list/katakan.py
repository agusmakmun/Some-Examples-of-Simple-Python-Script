"""
4
2 belas
seratus 4 puluh 0
9 ribu seratus 2 puluh 1
2 puluh 1 ribu 3 puluh 0
9 ratus 5 ribu 0
8 puluh 2 juta 8 ratus 8 belas ribu seratus 8 puluh 8
3 ratus 1 juta 4 puluh 8 ribu 5 ratus 8 puluh 8
"""

def kata(n):
    angka = range(11)
    temp = ""

    if n < 12: 
        temp += str(angka[n])
    elif n < 20: 
        temp += str(n-10)+" belas"
    elif n < 100: 
        temp += str(kata(n/10)) + " puluh "+ str(kata(n%10))
    elif n < 200:
        temp += "seratus "+ str(kata(n-100))
    elif n < 1000:
        temp += str(kata(n/100))+ " ratus " + str(kata(n%100))
    elif n < 2000:
        temp +=  "seribu "+str(kata(n-1000))
    elif n < 1000000:
        temp += str(kata(n/1000))+ " ribu "+ str(kata(n%1000))
    elif n < 1000000000:
        temp += str(kata(n/1000000)) +" juta " + str(kata(n%1000000))

    return temp

print kata(4)
print kata(12)
print kata(140)
print kata(9121)
print kata(21030)
print kata(905000)
print kata(82818188)
print kata(301048588)
