'''Здесь задание 11.4'''

class Teacher:
	def __init__(self, name, education, experience):
		self._name = name
		self._education = education
		self._experience = experience
		self._marks = {}

	# Геттеры для полей
	def get_name(self):
		return self._name

	def get_education(self):
		return self._education

	def get_experience(self):
		return self._experience

	# Сеттер для опыта работы
	def set_experience(self, experience):
		self._experience = experience

	def get_teacher_data(self):
		return f"{self._name}, образование {self._education}, опыт работы {self._experience} года."

	def add_mark(self, student_name, mark):
		self._marks[student_name] = mark
		return f"{self._name} поставил оценку {mark} студенту {student_name}."

	def remove_mark(self, student_name):
		if student_name in self._marks:
			del self._marks[student_name]
			return f"{self._name} удалил оценку у студента {student_name}."
		else:
			return f"У студента {student_name} нет оценки."

	def give_a_consultation(self, student_class):
		return f"{self._name} провел консультацию для класса {student_class}."

class DisciplineTeacher(Teacher):
	def __init__(self, name, education, experience, discipline, job_title):
		super().__init__(name, education, experience)
		self._discipline = discipline
		self._job_title = job_title

	def get_discipline(self):
		return self._discipline

	def get_job_title(self):
		return self._job_title

	def set_job_title(self, job_title):
		self._job_title = job_title

	def get_teacher_data(self):
		return f"{self._name}, образование {self._education}, опыт работы {self._experience} года, предмет {self._discipline}, должность {self._job_title}."

	def add_mark(self, student_name, mark):
		self._marks[student_name] = mark
		return f"{self._name} ({self._job_title}) поставил оценку {mark} студенту {student_name}, по предмету {self._discipline}."

	def remove_mark(self, student_name):
		if student_name in self._marks:
			del self._marks[student_name]
			return f"{self._name} ({self._job_title}) удалил оценку у студента {student_name}, по предмету {self._discipline}."
		else:
			return f"У студента {student_name} нет оценки."

	def give_a_consultation(self, student_class):
		return f"{self._name} ({self._job_title}) провел консультацию для класса {student_class}, по предмету {self._discipline}."


class Lawyer:
    def __init__(self, last_name, first_name):
        self._last_name = last_name
        self._first_name = first_name
        self._cases = {}  # Для хранения отметок по делам

    def get_last_name(self):
        return self._last_name

    def get_first_name(self):
        return self._first_name
    def add_mark(self, case_name, mark):
        self._cases[case_name] = mark
        return f"Адвокат {self._first_name} {self._last_name} поставил отметку {mark} по делу {case_name}."
    def remove_mark(self, case_name):
        if case_name in self._cases:
            del self._cases[case_name]
            return f"Адвокат {self._first_name} {self._last_name} удалил отметку по делу {case_name}."
        else:
            return f"По делу {case_name} отметка не найдена."
    def give_a_consultation(self, case_name):
        return f"Адвокат {self._first_name} {self._last_name} провел консультацию по делу {case_name}."


lawyer = Lawyer("Иванов", "Сергей")

# Получение информации
print(lawyer.get_first_name(), lawyer.get_last_name())

# Добавление отметки
print(lawyer.add_mark("Дело №123", "Победа"))

# Удаление отметки
print(lawyer.remove_mark("Дело №123"))

# Консультация
print(lawyer.give_a_consultation("Дело №456"))

