import spacy 
from spacy import displacy 

nlp = spacy.blank("en")
ruler = nlp.add_pipe("entity_ruler")

pattern = {"pattern": [{"LOWER": {"FUZZY", "voldemort"}}], "label": "person"}

ruler.add_patterns([pattern])

doc = nlp("Harry fought voldemort.")
displacy.render(doc, style="ent", jupyter=True)