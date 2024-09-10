import math  

def oklid_mesafesi(x1, y1, x2, y2):
    mesafe = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 
    return mesafe


x1 = float(input("Birinci noktanin x koordinatini girin: "))  
y1 = float(input("Birinci noktanin y koordinatini girin: ")) 
x2 = float(input("İkinci noktanin x koordinatini girin: "))  
y2 = float(input("İkinci noktanin y koordinatini girin: "))   


mesafe = oklid_mesafesi(x1, y1, x2, y2)


print(f"İki nokta arasındaki mesafe: {mesafe:.2f}")  
