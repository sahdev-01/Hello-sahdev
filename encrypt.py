encrypt = input("Enter coded message : ")
location = encrypt[0:len(encrypt):2]
city = encrypt[1:len(encrypt):2]
decrypt = location + "," + city
print(decrypt)