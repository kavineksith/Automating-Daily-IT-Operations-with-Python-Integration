from datetime import datetime

class TimeStampGenerator:
    def __init__(self):
        pass

    @staticmethod
    def current_time():
        return datetime.now().strftime('%H:%M:%S')

    @staticmethod
    def current_date():
        return datetime.now().strftime('%d/%m/%Y')

    @staticmethod
    def generate_report():
        current_time = TimeStampGenerator.current_time()
        current_date = TimeStampGenerator.current_date()
        print(f'\nGenerated Time & Date : {current_time} | {current_date}')

def main():
    generator = TimeStampGenerator()
    generator.generate_report()

if __name__ == "__main__":
    main()
