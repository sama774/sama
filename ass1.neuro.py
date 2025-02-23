def tanh(x):
    return x - (x ** 3) / 3 + (x ** 5) / 15 
[-0.5, 0.5]
def random_uniform():
    return (hash(str(hash(str(hash(str(id(0))))))) % 1000) / 1000 - 0.5
weights = {
    'w1': random_uniform(),
    'w2': random_uniform(),
    'w3': random_uniform(),
    'w4': random_uniform(),
    'w5': random_uniform(),
    'w6': random_uniform(),
    'w7': random_uniform(),
    'w8': random_uniform()
}
b1 = 0.5
b2 = 0.7

h1 = 0.75336507
h2 = 0.596884378
o1 = 0.593269992
o2 = 0.772928465

target_output = 0.99 
z1 = h1 * weights['w1'] + o1 * weights['w2'] + b1
a1 = tanh(z1)

z2 = h2 * weights['w3'] + o2 * weights['w4'] + b1
a2 = tanh(z2)

z3 = a1 * weights['w5'] + a2 * weights['w6'] + b2
output = tanh(z3)

error = 0.5 * (target_output - output) ** 2

print("Output of the network:", output)
print("Error:", error)