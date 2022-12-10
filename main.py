import json

from src import Greetings, Disease

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}


# loads the knowledge from .txt files into variables to allow the code to use it
def load_disease_symptoms() -> dict:
    with open(r'data\symptoms\symptoms.json') as f:
        return json.load(f)


def preprocess():
    global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    diseases = open("diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
    symptom_map = load_disease_symptoms()
    for disease in diseases_list:
        disease_s_file = open("data/descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()

        disease_s_file = open("data/treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()


def get_details(disease):
    return d_desc_map[disease]


def get_treatments(disease):
    return d_treatment_map[disease]


def if_not_matched(disease):
    print("")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print("")
    print("The most probable disease that you have is %s\n" % (id_disease))
    print("A short description of the disease is given below :\n")
    print(disease_details + "\n")
    print(
        "The common medications and procedures suggested by other real doctors are: \n"
    )
    print(treatments + "\n")


# driver function
if __name__ == "__main__":
    preprocess()
    case = Disease(
        'no',
        'no',
        'no',
        'low',
        'no',
        'no',
        'no',
        'no',
        'no',
        'no',
        'no',
        'no',
        'no',
    )
    # creating class object
    engine = Greetings(symptom_map, if_not_matched, get_treatments, get_details, case)
    # loop to keep running the code until user says no when asked for another diagnosis
    engine.reset()
    engine.run()

