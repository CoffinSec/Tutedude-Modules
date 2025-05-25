dictionary = {
    "Alice": "448",
    "Clara": "332",
    "Bob": "123",
    "John": "456",
    "Mary": "789",
}


def marks(name):
    print("Enter the name of the person you want to search for:")
    if name in dictionary:
        print("The number of the person is:", dictionary[name])
    else:
        print("The person is not in the dictionary.")


name = input("Enter the name of the person you want to search for: ")
marks(name)
