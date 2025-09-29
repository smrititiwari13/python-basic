my_list = [10, 20, 30, 40, 50]
print("Initial List:", my_list)

my_list.insert(2, 25)
print("List after inserting 25 at index 2:", my_list)

my_list.remove(40)
print("List after deleting 40:", my_list)

my_list[1] = 15
print("List after updating the element at index 1:", my_list)

my_list.append(60)
print("List after appending 60:", my_list)

another_list = [70, 80, 90]
my_list.extend(another_list)
print("List after extending with another list:", my_list)
