import time


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            # check left add left if none if less than self.value
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            # check right go right if none
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# kind of suprised hash is working. I think there are downsides for a real application.
# Creating a bst hashing each name and inserting the hash value into tree
# Hashing names in set 2 and searching with contains for duplicates
# Appending duplicates to duplicates if contains check passes

# runtime: 0.08380603790283203 seconds

duplicates = []

bst = BinarySearchTree(0)
for name_1 in names_1:
    hash_name = hash(name_1)
    # num_name = int(name_1)
    bst.insert(hash_name)

for name_2 in names_2:
    hash_name = hash(name_2)
    if bst.contains(hash_name):
        # num_name = int(name_2)
        duplicates.append(name_2)

# runtime: 5.326942205429077 seconds

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
