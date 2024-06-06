import sys

class DiskStorageCalculator:
    def __init__(self, input_labels):
        self.input_labels = input_labels
        self.input_values = []

    def input_validator(self, value):
        if not isinstance(value, int):
            print('Please insert numeric data only.')
            return False
        return True

    def calculate_storage(self):
        for label in self.input_labels:
            while True:
                value = input(f'No. of {label}: ')
                try:
                    value = int(value)
                    if self.input_validator(value):
                        self.input_values.append(value)
                        break
                except ValueError:
                    print('Please insert a numeric value.')

        total = 1
        for value in self.input_values:
            total *= value
        return total

    def preview_storage(self):
        total_bytes = self.calculate_storage()
        total_gb = total_bytes / (1024 ** 3)  # convert byte value into gigabyte value
        print(f'Total Size of the Disk: {total_gb:.2f} GigaBytes')

def main():
    input_labels = ['Cylinders', 'Heads', 'Sectors per Track', 'Bytes per Sector']
    calculator = DiskStorageCalculator(input_labels)
    calculator.preview_storage()

if __name__ == "__main__":
    main()
    sys.exit(0)
