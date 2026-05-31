'''
Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel etc.).  
'''

# --- Base Class (Parent) ---
class Entity:
    def __init__(self, name):
        self.name = name

# 1. Single Inheritance (Student inherits from Entity)
class Student(Entity):
    def study(self):
        print(f"{self.name} study is going.")

# 2. Multilevel Inheritance (SportsStudent inherits from Student)
class SportsStudent(Student):
    def play(self):
        print(f"{self.name} sports is running.")

# 3. Multiple Inheritance (ScholarSportsStudent inherits from Student & Athlete)
class Chess:
    def training(self):
        print("Training is going.")

class ScholarSportsStudent(Student, Chess):
    def details(self):
        print(f"{self.name} study and sports are managed.")

# 4. Hierarchical Inheritance (Teacher also inherits from Entity)
class Teacher(Entity):
    def teach(self):
        print(f"{self.name} taken class.")

print("--- 1. Single ---")
s = Student("Jainam Sheth")
s.study()

print("\n--- 2. Multilevel ---")
ss = SportsStudent("Het Patel")
ss.study()
ss.play()

print("\n--- 3. Multiple ---")
sss = ScholarSportsStudent("Fenil Patel")
sss.study()
sss.training()
sss.details()

print("\n--- 4. Hierarchical ---")
t = Teacher("Ankit Sir")
t.teach()
