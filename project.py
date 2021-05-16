from owlready2 import *
 
onto = get_ontology("./new.owl")
onto.load()
 
with onto:
 
    class University(Thing):pass
    class UOC(University):pass
    
    class Department(Thing):pass
    
    
    class Person(Thing):pass


    class Alumni(Person):pass
    class CSDAlumni(Alumni):pass
    
    class UniEmployee(Alumni):pass

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
    
    class Student(Person):pass
    class UndergraduateStudent(Student):pass
    class MScStudent(Student):pass
    class PhDStudent(Student):pass
    
    
    class Area(Thing):pass
    class CourseArea(Area):pass
    
    class enrolledIn(Student >> StudiesProgram):pass
    class graduatedFrom(Alumni >> University):pass
    class courseBelongsTo(Course >> CourseArea):pass
    class studiesBelongsTo(PostGraduateStudies >> CourseArea):pass
    class hasDescription(Course >> Description):pass
    class describes(ObjectProperty):
        inverse_property = hasDescription
    class prerequisites(Course >> Course):pass
    class teaches(FacultyMember >> Course):pass
    class worksAt(UniEmployee >> University):pass
    class attends(Student >> Course):pass
    class advisor(UndergraduateStudent >> FacultyMember):pass
    class mscAdvisor(MScStudent >> FacultyMember):pass
    class phdAdvisor(PhDStudent >> FacultyMember):pass
   
    class consistOf(University >> Department):pass
 
 
    University.equivalent_to.append(consistOf.some(Department))

    UniEmployee.equivalent_to.append(Alumni & worksAt.some(University))
    UniEmployee.equivalent_to.append(FacultyMember | AdministrativePersonnel)
    FacultyMember.equivalent_to.append(UniEmployee & teaches.some(Course))
    AdministrativePersonnel.is_a.append(UniEmployee)
    CSDEmployee.is_a.append(UniEmployee & worksAt.some(UOC))

    Course.equivalent_to.append(GraduateCourse | UndergraduateCourse)
    Course.equivalent_to.append(Course & hasDescription.exactly(1,Description) & prerequisites.min(0,Course))
    Description.equivalent_to.append(Description & describes.exactly(1, Course))
    AllDisjoint([GraduateCourse,UndergraduateCourse])
    GraduateCourse.equivalent_to.append(GraduateCourse & courseBelongsTo.some(CourseArea))

    StudiesProgram.equivalent_to.append(PostGraduateStudies | UndergraduateStudies)
    AllDisjoint([PostGraduateStudies,UndergraduateStudies])
    PostGraduateStudies.equivalent_to.append(PostGraduateStudies & studiesBelongsTo.some(CourseArea))
    PostGraduateStudies.equivalent_to.append(MScProgram | PhDProgram)
   

    Alumni.equivalent_to.append(Person & graduatedFrom.some(University))
    # Alumni.is_a.append(MScStudent | PhDStudent)
    CSDAlumni.is_a.append(Alumni & graduatedFrom.some(UOC))

    Student.equivalent_to.append(UndergraduateStudent | MScStudent | PhDStudent)
    Student.is_a.append(Student & attends.some(Course))
    UndergraduateStudent.equivalent_to.append(Student & enrolledIn.some(UndergraduateStudies) & advisor.exactly(1,FacultyMember))
    MScStudent.equivalent_to.append(Student & enrolledIn.some(MScProgram) & mscAdvisor.exactly(1,FacultyMember))
    MScStudent.is_a.append(Alumni)
    PhDStudent.equivalent_to.append(Student & enrolledIn.some(PhDProgram) & phdAdvisor.exactly(1,FacultyMember))
    PhDStudent.is_a.append(Alumni)
    
    # mscAdvisor.equivalent_to.append( )

    #---------------Abox for concepts---------------

    u = [] 
    for i in range(4):
        u.append(onto.University("u"+ str(i)))

    u.append(onto.UOC("u4"))

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

    #consistOf
    u[0].consistOf = [dep[0],dep[1],dep[2]]
    u[1].consistOf = [dep[0], dep[3]]
    u[2].consistOf = [dep[4]]
    u[3].consistOf = [dep[3],dep[4]]
    u[4].consistOf = [dep[0],dep[1],dep[4]]


    #worksAt
    fac[0].worksAt = [u[4]]
    fac[1].worksAt = [u[1]]
    fac[2].worksAt = [u[2]]
    fac[3].worksAt = [u[3]]
    fac[4].worksAt = [u[0]]
    prof[0].worksAt = [u[4]]
    prof[1].worksAt = [u[1]]
    prof[2].worksAt = [u[2]]
    prof[3].worksAt = [u[3]]
    prof[4].worksAt = [u[0]]
    admin[0].worksAt = [u[4]]
    admin[1].worksAt = [u[4]]
    admin[2].worksAt = [u[4]]
    admin[3].worksAt = [u[3]]
    admin[4].worksAt = [u[0]]


    #teaches
    fac[0].teaches = [gradC[0]]
    fac[1].teaches = [gradC[1]]
    fac[2].teaches = [gradC[2]]
    fac[3].teaches = [underC[0]]
    fac[4].teaches = [underC[1]]
    prof[0].teaches = [underC[2]]
    prof[1].teaches = [underC[3]]
    prof[2].teaches = [underC[4]]
    prof[3].teaches = [gradC[4]]
    prof[4].teaches = [gradC[3]]


    #enrolledIn
    uSt[0].enrolledIn = [uStudies[0]]
    uSt[1].enrolledIn = [uStudies[0]]
    uSt[2].enrolledIn = [uStudies[0]]
    uSt[3].enrolledIn = [uStudies[1]]
    uSt[4].enrolledIn = [uStudies[2]]
    mscSt[0].enrolledIn = [mscPr[0]]
    mscSt[1].enrolledIn = [mscPr[0]]
    mscSt[2].enrolledIn = [mscPr[2]]
    mscSt[3].enrolledIn = [mscPr[3]]
    mscSt[4].enrolledIn = [mscPr[2]]
    phdSt[0].enrolledIn = [phdPr[0]]
    phdSt[1].enrolledIn = [phdPr[0]]
    phdSt[2].enrolledIn = [phdPr[2]]
    phdSt[3].enrolledIn = [phdPr[0]]
    phdSt[4].enrolledIn = [phdPr[4]]


    #attends
    uSt[0].attends = [underC[0], underC[1], underC[2]]
    uSt[1].attends = [underC[3], underC[4]]
    uSt[2].attends = [underC[4]]
    mscSt[0].attends = [gradC[0], gradC[1]]
    mscSt[1].attends = [underC[0]]
    mscSt[3].attends = [gradC[3]]
    mscSt[4].attends = [gradC[4]]
    phdSt[0].attends = [gradC[0]]
    phdSt[1].attends = [gradC[1]]
    phdSt[2].attends = [gradC[2]]
    phdSt[3].attends = [gradC[3]]


    # courseBelongsTo: 
    gradC[0].courseBelongsTo = [carea[0]]
    gradC[1].courseBelongsTo = [carea[1]]
    gradC[2].courseBelongsTo = [carea[0]]
    gradC[3].courseBelongsTo = [carea[2]]
    gradC[4].courseBelongsTo = [carea[3]]
    underC[0].courseBelongsTo = [carea[0]]
    underC[1].courseBelongsTo = [carea[4]]
    underC[2].courseBelongsTo = [carea[1]]
    underC[3].courseBelongsTo = [carea[2]] 
    underC[4].courseBelongsTo = [carea[3]] 
    

    #studiesBelongsTo: 
    mscPr[0].studiesBelongsTo = [carea[0]] 
    mscPr[1].studiesBelongsTo = [carea[1]]
    mscPr[2].studiesBelongsTo = [carea[4]]
    mscPr[3].studiesBelongsTo = [carea[0]]
    mscPr[4].studiesBelongsTo = [carea[2]]
    phdPr[0].studiesBelongsTo = [carea[3]] 
    phdPr[1].studiesBelongsTo = [carea[4]]
    phdPr[2].studiesBelongsTo = [carea[2]]
    phdPr[3].studiesBelongsTo = [carea[0]]
    phdPr[4].studiesBelongsTo = [carea[4]]

    # prerequisites: 
    underC[0].prerequisites = [underC[1], underC[2]]
    underC[1].prerequisites = [underC[3]]
    gradC[0].prerequisites = [gradC[1]]
    gradC[1].prerequisites = [gradC[2]]


    # advisor: 
    uSt[0].advisor = [fac[0]]
    uSt[1].advisor = [fac[0]]
    uSt[2].advisor = [fac[1]]
    uSt[3].advisor = [prof[0]]
    uSt[4].advisor = [prof[1]]

    # mscAdvisor: 
    mscSt[0].mscAdvisor = [fac[0]]
    mscSt[1].mscAdvisor = [prof[1]]
    mscSt[2].mscAdvisor = [prof[3]]
    mscSt[3].mscAdvisor = [fac[4]]
    mscSt[4].mscAdvisor = [prof[3]]

    # phdAdvisor: 
    phdSt[0].phdAdvisor = [prof[0]]
    phdSt[1].phdAdvisor = [prof[2]]
    phdSt[2].phdAdvisor = [prof[3]]
    phdSt[3].phdAdvisor = [fac[4]]
    phdSt[4].phdAdvisor = [fac[4]]

    # graduatedFrom: 
    csdAlumni[0].graduatedFrom = [u[4]]
    csdAlumni[1].graduatedFrom = [u[4]]
    phdSt[0].graduatedFrom = [u[4]]
    phdSt[1].graduatedFrom = [u[4]]
    mscSt[0].graduatedFrom = [u[4]]
    alumni[0].graduatedFrom = [u[1]]
    alumni[1].graduatedFrom = [u[1]]
    alumni[2].graduatedFrom = [u[2]]
    alumni[3].graduatedFrom = [u[3]]
    alumni[4].graduatedFrom = [u[0]]
    mscSt[1].graduatedFrom = [u[1]]
    mscSt[2].graduatedFrom = [u[2]]
    mscSt[3].graduatedFrom = [u[3]]
    mscSt[4].graduatedFrom = [u[0]]
    phdSt[2].graduatedFrom = [u[1]]
    phdSt[3].graduatedFrom = [u[2]]
    phdSt[4].graduatedFrom = [u[3]]
    
    # hasDescription: 
    underC[0].hasDescription = [d[0]]
    underC[1].hasDescription = [d[1]]
    underC[2].hasDescription = [d[2]]
    underC[3].hasDescription = [d[3]]
    underC[4].hasDescription = [d[4]]
    gradC[0].hasDescription = [d[5]]
    gradC[1].hasDescription = [d[6]]
    gradC[2].hasDescription = [d[7]]
    gradC[3].hasDescription = [d[8]]
    gradC[4].hasDescription = [d[9]]

    sync_reasoner()

onto.save('./our_schema.owl')


# sync_reasoner(infer_property_values = True)

for sh in onto.advisor.get_relations():
    print(sh[0], sh[1])
# print(Course.equivalent_to)
# print(worksAt.domain)
# print(Area.instances())
# print(CourseArea.instances())
# print(MScStudent.instances())
# print(PhDStudent.instances())
# print(Person.instances())

# print(admin[0])
 
 
# onto.save('./test.owl')
