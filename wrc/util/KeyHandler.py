def save_key(filename, key):
    key_file = open(filename + '.wrc', 'wb')
    key_file.write(key.encode())
    key_file.flush()
    key_file.close()


def read_key(filename):
    f = open(filename + '.wrc', 'rb')
    return f.read().decode()
