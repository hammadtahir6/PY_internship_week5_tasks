counter = 0

def change_counter():
    global counter
    counter += 1

change_counter()
change_counter()
print("Counter:", counter)
