k = 1.0595 #??
v = 246.94*4*0.65 #m/s
freq_A = 440 #Hz

print('boob',1 - 1/k)

def length(n):
    return v/(4*freq_A)*k**(10-n)

for n in range(1,9):
    print(f'bånd {n} befinner seg ved L = {length(n):2f} ')