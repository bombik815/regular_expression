from dirty_main import *
from  application import salary, people


def main():
    pprint(f"Приветсвую вас! Текущая дата {now.strftime('%d-%m-%Y')}")
    salary.calculate_salary()
    people.get_employees()

if __name__ == '__main__':
    now = datetime.now()
    main()


