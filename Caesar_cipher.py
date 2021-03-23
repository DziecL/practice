import random

def encode(text, seed):
    random.seed(seed)
    e = [chr(ord(i) + round(random.random() * 10)) for i in text]
    return "".join(e)


def decode(text, seed):
    random.seed(seed)
    d = [chr(ord(i) - round(random.random() * 10)) for i in text]
    return "".join(d)
  
  def brute_force(text):
    i = 0
    seed = 0
    while i == 0:
        random.seed(seed)
        d = [chr(ord(j) - round(random.random() * 10)) for j in text]
        print("".join(d))
        i = int(input('Does it make sense? t=1 , f=0\n'))
        if i == 1:
            return f'Decoded text: \'{"".join(d)}\', seed: {seed}'
        else:
            seed += 1
            
# makes brute_force obsolete
def encode2(text, seed, seed2):
    random.seed(seed)
    e = [chr(ord(i) + random.randint(1, seed2)) for i in text]
    return "".join(e)


def decode2(text, seed, seed2):
    random.seed(seed)
    d = [chr(ord(i) - random.randint(1, seed2)) for i in text]
    return "".join(d)

# additional layer of protection could be added, another seed for the range of unicode characters ('33' and '1100' in the loop, both or any of them), 
# it should loop on itself so that you can input a large number and you won't get an error and you won't get all the weird characters
# probably overly complicated but with up to 4 variables seems decent enough

uni = []
for i in range(33, 1100):
    uni.append(chr(i)) if (i <= 126 or i >= 151) else print(chr(i))
print(uni)

a = 10001
while a > len(uni):
    a -= len(uni)
print(f'{uni[a]} {str(a)}')
