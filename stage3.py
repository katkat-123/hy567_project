from owlready2 import *

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
def is_of_types(ontology, individual):
	with ontology: sync_reasoner(infer_property_values = True)
	return individual.is_a



#(3)
def get_all_concept_instances(concept):
	return concept.instances()


#(4)
def get_all_role_instances(role):
	return list(role.get_relations())

#(5)
def is_subclass_of(ontology, C, D):
	subclasses_of_D = ontology.search(subclass_of = D)
	
	#BUG!!!!!!!!!!!!!!!!!!
	# print(subclasses_of_D)
	
	if C in subclasses_of_D:
		return True
	else:
		return False

#(6)
def get_S_module(ontology, S):
	pass



#------------------testing----------------------

onto = get_ontology("./output.owl").load()

# print(is_consistent(onto))
# print(is_of_types(onto, onto.uSt0))
# print(get_all_concept_instances(onto.PostgraduateStudies))
# print(get_all_role_instances(onto.prerequisites))
print(is_subclass_of(onto, onto.PhDStudent, onto.Person))

