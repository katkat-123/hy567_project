from owlready2 import *
from py4j.java_gateway import launch_gateway, JavaGateway

#(1) if an ontology is incosistent, running the reasoner
#will raise the OwlReadyInconsistentOntologyError exception
def is_consistent (ontology):
	try:
		with ontology: sync_reasoner(infer_property_values = True)
	except OwlReadyInconsistentOntologyError:
		return 'no'
	else: 
		return 'yes'



#(2) 
def is_of_types(individual):

	concepts = []
	for c in individual.is_a:
		ancestors = c.ancestors()
		for a in ancestors:
			if a not in concepts:
				concepts.append(a)
	return concepts



#(3)
def get_all_concept_instances(concept):
	return concept.instances()


#(4)
def get_all_role_instances(role):
	return list(role.get_relations())


#(5)
def is_subclass_of(ontology, C, D):

	subclasses_of_D = ontology.search(subclass_of = D)
	return (subclasses_of_D.count(C)>0)


#(6)
def get_S_module(onto_path, signature_path):
	
	launch_gateway(jarpath='./robot.jar',
               classpath='org.obolibrary.robot.PythonOperation',
               port=25333,
               die_on_exit=True)

	gateway = JavaGateway()

	io_helper = gateway.jvm.org.obolibrary.robot.IOHelper()
	extractor = gateway.jvm.org.obolibrary.robot.ExtractOperation()


	ModuleType = gateway.jvm.uk.ac.manchester.cs.owlapi.modularity.ModuleType
	starModuleType = ModuleType.STAR


	io_helper.saveOntology(
		extractor.extract(
			io_helper.loadOntology(onto_path),
			io_helper.parseTerms(signature_path),
			io_helper.createIRI("http://example.com"),
			starModuleType
		),
		'result.owl'
		)



#------------------testing----------------------

onto = get_ontology("./ontology.owl").load()

#1
print(is_consistent(onto))

#2
print(is_of_types(onto.gradC0))
print(is_of_types(onto.uSt0))

#3
print(get_all_concept_instances(onto.CSDEmployee))

#4
print(get_all_role_instances(onto.advisor))

#5
print(is_subclass_of(onto, onto.PhDStudent, onto.Person))
print(is_subclass_of(onto, onto.PhDStudent, onto.Course))

#6
get_S_module("./ontology.owl", "./signature.txt")