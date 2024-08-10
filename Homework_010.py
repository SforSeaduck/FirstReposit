"""
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку
здійснюється за механізмом

student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення,
    бал від 0 до 100 (інт чи флоат)
2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to you
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""

students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
# ваш код нижче !!!!!!!! вище нічого не змінюємо

from pywebio.output import put_table, put_html, put_text
from pywebio.input import input as input_pw, slider

put_html('Заповнiть форму:')
student_name = input_pw("Введiть, ваше iм'я та прiзвище: ", type='text')

student_email = input_pw('Введiть, вашу електронну пошту: ')
student_age = slider('Введiть, ваш вiк: ', min_value=18, max_value=40, step=1)
student_phone_num = input_pw('Введiть, ваш номер телефону: ', type='text')
average_mark = input_pw('Введiть, ваш середнiй бал: ', type='float')
student = {}
student.update({
    'Пошта': student_email,
    'Вiк': student_name,
    'Номер телефону': student_phone_num,
    'Середній бал': average_mark,
})
# print("student: ", student)
students.update({student_name: student})

# print("students['Іван Петров']['Пошта']", students['Іван Петров']['Пошта'])

list_of_well_students = []
counter = 0
sum_of_marks = 0
for k, v in students.items():
    sum_of_marks = sum_of_marks + float(students[k]['Середній бал'])
    counter = counter + 1
    number_of_phone = students[k].get('Номер телефону')

    if number_of_phone is None or student_phone_num == str(None) or student_phone_num is None:
        students[k].update({'Номер телефону': '+38098322322'})

    if students[k]['Середній бал'] > 90:
        print('well student', k, students[k]['Середній бал'])
        list_of_well_students.append([k, students[k]['Середній бал']])
    pass
pass

# print(list_of_well_students)
# print(students)
average_mark_of_group = sum_of_marks / counter

put_table([list_of_well_students[0], list_of_well_students[1]],
          header=["Прiзвище та iм'я", "Середнiй бал"])

put_text(f'Середнiй бал по групi = {average_mark_of_group}')

