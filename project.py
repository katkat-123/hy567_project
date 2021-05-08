from owlready2 import *
 
onto = get_ontology("malakia")
# onto.load()
 
with onto:
 
   class University(Thing):pass
   class UOC(University):pass
 
   class Department(Thing):pass
 
  
   class Person(Thing):pass
   
   class UniEmployee(Person):pass

   class AdministrativePersonnel(UniEmployee):pass
   class FacultyMember(UniEmployee):pass
   class Professor(FacultyMember):pass
 
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
   class describes(ObjectProperty):
       inverse_property = hasDescription
   class prerequisites(Course >> Course):pass
   class teaches(FacultyMember >> Course):pass
   class worksAt(UniEmployee >> University):pass
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

UniEmployee.equivalent_to.append(Person & worksAt.some(University))
UniEmployee.equivalent_to.append(FacultyMember | AdministrativePersonnel)
FacultyMember.equivalent_to.append(UniEmployee & teaches.some(Course))
AdministrativePersonnel.is_a.append(UniEmployee)
CSDEmployee.is_a.append(UniEmployee & worksAt.some(UOC))

Course.equivalent_to.append(GraduateCourse | UndergraduateCourse)
Course.equivalent_to.append(Course & hasDescription.exactly(1,Description) & prerequisites.min(0,Course))
Description.equivalent_to.append(Description & describes.exactly(1, Course))
AllDisjoint([GraduateCourse,UndergraduateCourse])
GraduateCourse.is_a.append(GraduateCourse & belongsTo.some(CourseArea))
PostGraduateStudies.is_a.append(PostGraduateStudies & belongsTo.some(CourseArea))
PostGraduateStudies.equivalent_to.append(MScProgram | PhDProgram)
StudiesProgram.equivalent_to.append(PostGraduateStudies | UndergraduateCourse)
AllDisjoint([PostGraduateStudies,UndergraduateStudies])

Alumni.equivalent_to.append(Person & graduatedFrom.some(University))
Alumni.is_a.append(MScStudent | PhDStudent)
CSDAlumni.is_a.append(Alumni & graduatedFrom.some(UOC))

Student.equivalent_to.append(Person & advisor.exactly(1,FacultyMember))
Student.equivalent_to.append(UndergraduateStudent | MScStudent | PhDStudent)
Student.is_a.append(Student & attends.some(Course))
UndergraduateStudent.equivalent_to.append(Student & enrolledIn.some(UndergraduateStudies))
MScStudent.equivalent_to.append(Student & enrolledIn.some(MScProgram))
PhDStudent.equivalent_to.append(Student & enrolledIn.some(PhDProgram))
 

#---------------Abox for concepts---------------

u = [] 
for i in range(4):
    u.append(onto.University("u"+ str(i)))

u4 = onto.UOC("u4")

dep = [] 
for i in range(5):
    dep.append(onto.Department("dep"+ str(i)))

p = [] 
for i in range(5):
    p.append(onto.Person("p"+ str(i)))

admin = [] 
for i in range(5):
    admin.append(onto.AdministrativePersonnel("admin"+ str(i)))

fac = []
for i in range(5):
    fac.append(onto.FacultyMember("fac"+ str(i)))

prof = []
for i in range(5):
    prof.append(onto.Professor("prof"+ str(i)))

admin[0].is_a.append(CSDEmployee) #gia na kanw ton admin0 na anhkei se 2 klaseis/concepts
admin[1].is_a.append(CSDEmployee)
admin[2].is_a.append(CSDEmployee)
fac[0].is_a.append(CSDEmployee)
prof[0].is_a.append(CSDEmployee)


gradC = []
for i in range(5):
    gradC.append(onto.GraduateCourse("gradC"+ str(i)))

underC = []
for i in range(5):
    underC.append(onto.UndergraduateCourse("underC"+ str(i)))

d = []
for i in range(10):
    d.append(onto.Description("d"+ str(i)))

uStudies = []
for i in range(5):
    uStudies.append(onto.UndergraduateStudies("uStudies"+ str(i)))

mscPr = []
for i in range(5):
    mscPr.append(onto.MScProgram("mscPr"+ str(i)))

phdPr = []
for i in range(5):
    phdPr.append(onto.PhDProgram("phdPr"+ str(i)))


uSt = []
for i in range(5):
    uSt.append(onto.UndergraduateStudent("uSt"+ str(i)))

mscSt = []
for i in range(5):
    mscSt.append(onto.MScStudent("mscSt"+ str(i)))

phdSt = []
for i in range(5):
    phdSt.append(onto.PhDStudent("phdSt"+ str(i)))


alumni = []
for i in range(5):
    alumni.append(onto.Alumni("alumni"+ str(i)))

csdAlumni = []
for i in range(2):
    csdAlumni.append(onto.CSDAlumni("csdAlumni"+ str(i)))
phdSt[0].is_a.append(CSDAlumni)
phdSt[1].is_a.append(CSDAlumni)
mscSt[0].is_a.append(CSDAlumni)

area = []
for i in range(5):
    area.append(onto.Area("area"+ str(i)))

carea = []
for i in range(5):
    carea.append(onto.CourseArea("carea"+ str(i)))


#---------------Abox for roles---------------

# for i in range(5):
#     u[i].consistOf = [dep[0]]
    

# for sh in onto.consistOf.get_relations():
#     print(sh.x1, sh)

print(Area.instances())
print(CourseArea.instances())
# print(MScStudent.instances())
# print(PhDStudent.instances())
# print(Person.instances())

# print(admin[0])
 
 
# onto.save('./test.owl')
