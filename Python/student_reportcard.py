import numpy as np

class Student:
  def __init__(self, name, Class,PRN):
    self.name = name
    self.Class = Class
    self.PRN = PRN
    self.marks = []

  def __display(self):
    print(f"\nStudent Info:\nName: {self.name}\nClass: {self.Class}\nPRN number: {self.PRN}")

  def calculate(self,currSem):
    m = []
    print("\nEnter semester wise matks of student(marks greater than 40 only)")
    for i in range(1,currSem+1):
      semMarks = [int(x) for x in input(f"Enter 5 subjects marks for Sem-{i}: ").split()]
      m.append(semMarks)
    self.marks = np.array(m)

    self.__display()
    print("\nScore Card:-\n")
    print("Semester wise Percentage:-")
    Sum = self.marks.sum(axis = 1)
    for i in range(currSem):
      print(f"Sem {i+1} Total marks: {Sum[i]} out of 500 Percentage: {Sum[i]/5}%")
    print(f"\nOverall Aggregate Total marks:{Sum.sum()} out of {500*currSem}\nPercentage: {Sum.sum()/(5*currSem)}%")

    print("\nSemester wise Min/Max Marks:-")
    Min = self.marks.min(axis = 1)
    Max = self.marks.max(axis = 1)
    for i in range(currSem):
      print(f"Sem {i+1} Max: {Max[i]} Min: {Min[i]}")
    print(f"\nOverall Max Marks: {Max.max()}\nOverall Min Marks:{Min.min()}")

if __name__=="__main__":
  currSem = int(input("Enter Current Semester: "))
  ch = 0
  studentList = []
  while True:
    print("\n1.Add Student")
    print("2.Display Student Card")
    print("3.Exit")
    ch = int(input("Enter Your Choice: "))
    if ch==1:
      name = input("Enter Name of Student: ")
      Class = input("Entet Class: ")
      PRN = input("Enter PRN number: ")
      studentList.append(Student(name,Class,PRN))
    elif ch==2:
      searchPRN = input("Enter PRN of student: ")
      flag = 0
      for s in studentList:
        if s.PRN==searchPRN:
          flag = 1
          try:
            s.calculate(currSem)
          except:
            print("\nException Occured...\nTry Again...\n")
      if not flag:
        print("\nPRN number not found...")
    elif ch==3:
      break
    else:
      print("Enter Valid Choice...")
