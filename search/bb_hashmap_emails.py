class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()  # create many lists in each bucket

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        # look for existence. If found, replace it with new value
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break

        # update or append the tuple of (key, value)
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            return record_value
        else:
            return "Not found"

    def delete(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket.pop(index)
            return record_value
        else:
            return "Not found"

    def __str__(self):
        return ''.join(str(item) for item in self.hash_table)


hash_table = HashTable(256)
with open("data.txt") as f:
    for line in f:
        key, value = line.split(':')
        hash_table.set_val(key, value)

print(hash_table.get_val("mashrur@example.com"))
print(hash_table.get_val("evgeny@example.com"))