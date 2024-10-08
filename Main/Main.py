'''Здесь задание 11.3'''

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


# Создаем объект DisciplineTeacher
teacher = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Учитель старших классов")

# Получение информации о преподавателе
print(teacher.get_teacher_data())

# Добавление
print(teacher.add_mark("Петр Сидоров", 4))

# Удаление
print(teacher.remove_mark("Дмитрий Степанов"))

# Проведение
print(teacher.give_a_consultation("7Б"))

# Изменение
teacher.set_job_title("Завуч")
print(teacher.get_teacher_data())
