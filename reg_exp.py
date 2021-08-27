import re
from pprint import pprint
import csv


result_list = []
result_phone = []

''' Функция для проверки дублирующие Фамилии '''
def check_last_name(lastname, list_line, stat = False):
    for line in result_list:
        if lastname in line[0]:
            if (line[0] != '') or (line[0] != '' and list_line[0] != '') \
                    or (line[0] == '' and list_line[0] == ''):
                pass
            else: line.insert(0, list_line[0])

            if (line[1] != '') or (line[1] != '' and list_line[1] != '') \
                    or (line[1] == '' and list_line[1] == ''): pass
            else: line.insert(1, list_line[1])

            if (line[2] != '') or (line[2] != '' and list_line[2] != '') \
                    or (line[2] == '' and list_line[2] == ''): pass
            else:  line.insert(2, list_line[2])

            if (line[3] != '') or (line[3] != '' and list_line[3] != '') \
                    or (line[3] == '' and list_line[3] == ''): pass
            else: line.insert(3, list_line[3])

            if (line[4] != '') or (line[4] != '' and list_line[4] != '') \
                    or (line[4] == '' and list_line[4] == ''): pass
            else: line.insert(4, list_line[4])

            if (line[5] != '') or (line[5] != '' and list_line[5] != '') \
                    or (line[5] == '' and list_line[5] == ''): pass
            else: line.insert(5, list_line[5])

            if (line[6] != '') or (line[6] != '' and list_line[6] != '') \
                    or (line[6] == '' and list_line[6] == ''): pass
            else: line.insert(6, list_line[6])

            stat = True
    return stat

''' Главная функция - входящая'''
def main():
    # читаем адресную книгу в формате CSV в список contacts_list
    with open("phonebook_raw.csv", "r", encoding="utf8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)


    # TODO 1: выполните пункты 1-3 ДЗ

    look_for_phone = r"(\+7|8)\s?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(\s*\(?(доб.)?\)?\s?(\d{4})\)?)?"

    temp = []
    lastname=''
    result_check = False
    for line in range(0, len(contacts_list)):
        if line == 0:
            result_list.append(contacts_list[line])
            pass

        for items in range(len(contacts_list[line])):

            if items == 0:
                lastname = contacts_list[line][items].split()[0]
                result_check = check_last_name(lastname, contacts_list[line])

            if result_check == True:
                break
            else:
                ''' Проверяем если в списке пустой элемент '', то записываем его по конкретным идексом '''
                if len(contacts_list[line][items].split()) == 0:
                    if items == 3 and (contacts_list[line][items] == ''):
                        temp.insert(3, contacts_list[line][items])
                    elif items == 4 and (contacts_list[line][items] == ''):
                        temp.insert(4, contacts_list[line][items])
                    elif items == 5 and (contacts_list[line][items] == ''):
                        temp.insert(5, contacts_list[line][items])
                    elif items == 6 and (contacts_list[line][items] == ''):
                        temp.insert(6, contacts_list[line][items])

                ''' Проверяем если ФИО в списке в правильной форме или нет и меняем на правильную '''
                if len(contacts_list[line][items].split()) == 1:
                    temp.append(contacts_list[line][items].split()[0])
                elif len(contacts_list[line][items].split()) == 2:
                    if items == 5:
                        temp.append(contacts_list[line][items])
                    else:
                        temp.append(contacts_list[line][items].split()[0])
                        temp.append(contacts_list[line][items].split()[1])
                elif len(contacts_list[line][items].split()) == 3:
                    if items == 5:
                        temp.append(contacts_list[line][items])
                    else:
                        temp.append(contacts_list[line][items].split()[0])
                        temp.append(contacts_list[line][items].split()[1])
                        temp.append(contacts_list[line][items].split()[2])
                elif len(contacts_list[line][items].split()) > 4:
                    temp.append(contacts_list[line][items])
        if len(temp) == 0:  pass
        else:
            myString = ', '.join(temp)
            result_phone = re.sub(look_for_phone, r"+7(\2)\3-\4-\5 \7\8", myString)
            result_list.append(result_phone.split(","))
            temp = []



    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding="utf8") as f:
     datawriter = csv.writer(f, delimiter=',')
     datawriter.writerows(result_list)



if __name__ == '__main__':
  main()
  pprint(result_list)

