class Hashmap:
    def __init__(self):
        self.dictionary = {}
        self.added_value = 0
        self.added_key = 0


    def insert(self, x, y):
        self.dictionary[x - self.added_key] = y - self.added_value


    def get(self, x):
        return self.dictionary[x - self.added_key] + self.added_value


    def add_to_key(self, x):
        self.added_key += x


    def add_to_value(self, y):
        self.added_value += y


def main():
    queryType = ["insert", "insert", "addToValue", "addToKey", "get"]
    query = [[1, 2], [2, 3], 2, 1, 3]
    hashmap = Hashmap()
    result = 0

    for i in range(len(queryType)):
        if queryType[i] == "insert":
            hashmap.insert(query[i][0], query[i][1])
        elif queryType[i] == "get":
            result += hashmap.get(query[i])
        elif queryType[i] == "addToKey":
            hashmap.add_to_key(query[i])
        elif queryType[i] == "addToValue":
            hashmap.add_to_value(query[i])

    print(result)


main()
