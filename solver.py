import hashlib


def md5_hex(word):
    h = hashlib.md5()
    h.update(word)
    return h.hexdigest()

res_hash = '76fb930fd0dbc6cba6cf5bd85005a92a'
res_hash_bin = bin(int(res_hash, 16))[2:]
words = open('words').read().split()
word_hashes = {md5_hex(word): word for word in words}


def main():
    secrets = []
    for word in words:
        word_bin = bin(int(md5_hex(word), 16))[2:]
        if hex(int(word_bin, 2) ^ int(res_hash_bin, 2))[2:-1] in word_hashes:
            secrets.append(word)
    print(secrets)


if __name__ == '__main__':
    main()
