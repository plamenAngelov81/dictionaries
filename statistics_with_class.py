class Store:

    def __init__(self, all_keys, total_values):
        self.all_keys = all_keys
        self.total_values = total_values
        self.store = {}

    def add_items(self, command):

        while True:

            if command == "statistics":
                break

            current_tack = command.split(": ")
            food = current_tack[0]
            quantity = int(current_tack[1])
            if food in self.store.keys():
                self.store[food] += quantity
            else:
                self.store[food] = quantity

            command = input()

    def stats(self):
        print(f"Products in stock:")
        for (key, value) in self.store.items():
            print(f"- {key}: {value}")

    def sum_len(self):
        self.all_keys = len(self.store.keys())
        self.total_values = sum(self.store.values())
        print(f"Total Products: {self.all_keys}")
        print(f"Total Quantity: {self.total_values}")


store = Store(all_keys=0, total_values=0)
store.add_items(command=input())
store.stats()
store.sum_len()
