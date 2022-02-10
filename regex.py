split_name_pattern = r'([А-Я]{1}[а-яё]+)[ |,]*([А-Я]{1}[а-яё]+)' \
                     r'[ |,]*([А-Я]{1}[а-яё]+)?'
pattern_phone = r'(\+7|8)?\s?\(?(\d+)\)?[ |-]?(\d{3})[ |-]?(\d{2})' \
                r'[ |-]?(\d{2})\s?\(?([а-я]*\.?)\s*(\d*)\)?'
pattern_mail = r'\w*@\w*\.\w*'
position_check = r'(\w+\D[ –]+)+(\w*\s*)*'
comma_pattern = r',+'
comma_sub = r','
name_sub = r'\1,\2,\3'
phone_sub = r"+7(\2)\3-\4-\5 \6\7"
