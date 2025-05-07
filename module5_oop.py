class DataProcessor:
    def __init__(self):
        self.nums = []

    def read_n(self):
        self.n = int(input("Enter N"))
        if self.n <= 0:
            raise ValueError("N must be a positive integer")

    def read_input_numbers(self):
        print(f"Enter {self.n} numbers (one by one):")
        for i in range(1, self.n + 1):
            num = int(input(f"Number #{i}: "))
            self.nums.append(num)

    def search(self, x):
        try:
            return self.nums.index(x) + 1
        except ValueError:
            return -1

    def run(self):
        self.read_n()
        self.read_input_numbers()
        x = int(input("Enter X (integer to search): "))
        print(self.search(x))


if __name__ == "__main__":
    DataProcessor().run()