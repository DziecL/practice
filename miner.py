from hashlib import sha256
import time
import string
import random


def encode_sha256(text):
    return sha256(text.encode('ascii')).hexdigest()


def miner(block_number, transactions, previous_hash, prefix_zeros):
    nonce = range(1, 100000000)
    for i in nonce:
        try_hash = str(block_number) + transactions + str(previous_hash) + str(i)
        new_hash = encode_sha256(try_hash)
        if new_hash.startswith('0'*prefix_zeros):
            print(f'Block mined, nonce: {i}')
            return new_hash
    return 'Mining failed'


def random_letter():
    list_lower = list(string.ascii_lowercase)
    return list_lower[random.randint(0, 25)]


def random_number_big():
    return random.randint(1, 1000)


def random_number_small():
    return random.randint(1, 11)


def generate_transactions():
    lines = range(0, random_number_small())
    transactions = ""
    for i in lines:
        f = random_letter()
        t = random_letter()
        a = random_number_big()
        transactions += f'from: {f}, to: {t}, amount: {str(a)};'
        transactions += '\n' if i != lines[-1] else ''
    return transactions


def print_to_file(content):
    with open('blockchain.txt', 'w') as file:
        file.write(content)
        file.close()


def main():
    start = time.time()
    block_number = 1
    diff = 4
    prev_hash = '0'*64
    i = 1
    content = ""
    while i < 10 or prev_hash == 'Mining failed':
        transactions = generate_transactions()
        mined_hash = miner(block_number, transactions, prev_hash, diff)
        prev_hash = mined_hash
        print(mined_hash)
        i += 1
        block_number += 1
        content += f'Block hash: {mined_hash}, block number: {block_number} \nList of transactions: \n{transactions} \n \n'

    print_to_file(content)
    print(f'Mining took {time.time() - start} seconds.')


if __name__ == '__main__':
    main()
