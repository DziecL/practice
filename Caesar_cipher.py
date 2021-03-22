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

