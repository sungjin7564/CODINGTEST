h, b, c, s = map(int,input().split()) 

totalbit = h*b*c*s

totalbyte = totalbit/8
totalkb = totalbyte/1024
totalmb = totalkb/1024

print("%0.1f MB" %totalmb)