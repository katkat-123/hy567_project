from owlready2 import *
 
onto = get_ontology("./new.owl")
onto.load()
 
with onto:
 
   class University(Thing):pass
   class UOC(University):pass
 
   class Department(Thing):pass
 
  
   class Person(Thing):pass
   class AdministrativePersonnel(Person):pass
  
   class FacultyMember(Person):pass
   class Professor(FacultyMember):pass
 
   class UniEmployee(Person):pass
   class CSDEmployee(UniEmployee):pass
 
   class Course(Thing):pass
   class GraduateCourse(Course):pass
   class UndergraduateCourse(Course):pass
   class Description(Thing):pass
 
   class StudiesProgram(Thing):pass
   class UndergraduateStudies(StudiesProgram):pass
   class PostGraduateStudies(StudiesProgram):pass
   class MScProgram(PostGraduateStudies):pass
   class PhDProgram(PostGraduateStudies):pass
 
   class Alumni(Person):pass
   class CSDAlumni(Alumni):pass
 
   class Student(Person):pass
   class UndergraduateStudent(Student):pass
   class MScStudent(Student):pass
   class PhDStudent(Student):pass
 
  
   class Area(Thing):pass
   class CourseArea(Area):pass
 
   class enrolledIn(Student >> StudiesProgram):pass
   class graduatedFrom(Alumni >> University):pass
   class belongsTo(ObjectProperty):
       domain = [Course, PostGraduateStudies]
       range = [CourseArea]
   class hasDescription(Course >> Description):pass
   class prerequisites(Course >> Course):pass
   class teaches(FacultyMember >> Course):pass
   class worksAt(Person >> University):pass
   class attends(Student >> Course):pass
   class advisor(Student >> FacultyMember):pass
   class advises(ObjectProperty):
       inverse_property = advisor
   class mscAdvisor(advisor):
       domain=[MScStudent]
   class phdAdvisor(advisor):
       domain=[PhDProgram]
 
   class consistOf(University >> Department):pass
 
 
University.equivalent_to.append(consistOf.some(Department))
FacultyMember.equivalent_to.append(Person & teaches.some(Course) & worksAt.some(University))
AdministrativePersonnel.is_a.append(Person & worksAt.some(University))
UniEmployee.equivalent_to.append(FacultyMember | AdministrativePersonnel)
CSDEmployee.is_a.append(UniEmployee & worksAt.some(UOC))
Course.equivalent_to.append(GraduateCourse | UndergraduateCourse)
Course.equivalent_to.append(Course & hasDescription.some(Description) & prerequisites.min(0,Course))
AllDisjoint([GraduateCourse,UndergraduateCourse])
GraduateCourse.is_a.append(GraduateCourse & belongsTo.some(CourseArea))
PostGraduateStudies.is_a.append(PostGraduateStudies & belongsTo.some(CourseArea))
PostGraduateStudies.equivalent_to.append(MScProgram | PhDProgram)
StudiesProgram.equivalent_to.append(PostGraduateStudies | UndergraduateCourse)
AllDisjoint([PostGraduateStudies,UndergraduateStudies])
Alumni.equivalent_to.append(Person & graduatedFrom.some(University))
CSDAlumni.is_a.append(Alumni & graduatedFrom.some(UOC))
Student.equivalent_to.append(Person & advisor.exactly(1,FacultyMember))
Student.equivalent_to.append(UndergraduateStudent | MScStudent | PhDStudent)
Student.is_a.append(Student & attends.some(Course))
UndergraduateStudent.equivalent_to.append(Student & enrolledIn.some(UndergraduateStudies))
MScStudent.equivalent_to.append(Student & enrolledIn.some(MScProgram))
PhDStudent.equivalent_to.append(Student & enrolledIn.some(PhDProgram))
 
 
 
onto.CSDAlumni("Alex")
onto.GraduateCourse("HY567")
 
 
onto.save('./test.owl')
