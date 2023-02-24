from utils import load_students, load_professions, get_student_by_pk, get_profession_by_title, check_fitness, show_result

if __name__ == '__main__':
    file_students = 'students.json'
    file_professions = 'professions.json'

    data_students = load_students(file_students)
    data_professions = load_professions(file_professions)

    pk = int(input('Введите номер студента: '))
    student = get_student_by_pk(pk, data_students)

    if student:
        print(f'Студент {student["full_name"]}')
        str_skills = ', '.join(student["skills"])
        print(f'Знает {student["skills"]}')
    else:
        quit()
    
    title = input('Выберите специальность для оценки студента: ')
    profession = get_profession_by_title(title, data_professions)

    if not profession:
        quit()
    
    data = check_fitness(student, profession)

    print(show_result(data, student['full_name']))