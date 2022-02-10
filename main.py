import re
import csv
from regex import split_name_pattern, pattern_phone,\
    pattern_mail, position_check, comma_pattern, comma_sub, name_sub, phone_sub

with open("phonebook.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


contact_list = []
for data in contacts_list:
    split_names = re.sub(split_name_pattern, name_sub, ','.join(data))
    comma_fixed = re.sub(comma_pattern, comma_sub, split_names)
    phones_transformation = re.sub(pattern_phone, phone_sub, comma_fixed)
    contact_list.append(phones_transformation.split(','))


unique_record_book = dict()
for data in contact_list[1:]:
    if (data[0], data[1]) not in unique_record_book:
        unique_record_book[(data[0], data[1])] = data[2:]
    else:
        unique_record_book[(data[0], data[1])] += data[2:]


def search_data(search_pattern, data_list):
    data_search = re.search(search_pattern, ','.join(data_list))
    if data_search:
        return data_search.group()
    else:
        return ''


final_phonebook = [contact_list[0]]
for fullname, data in unique_record_book.items():
    position = search_data(position_check, data)
    phone = search_data(pattern_phone, data)
    mail = search_data(pattern_mail, data)
    final_phonebook.append(
        [fullname[0], fullname[1], data[0],
         data[1], position, phone, mail]
                          )


with open("new_phonebook.csv", "w", encoding='utf-8', newline='') as f:
    data_writer = csv.writer(f, delimiter=',')
    data_writer.writerows(final_phonebook)

