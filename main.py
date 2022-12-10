import json

from src import Doctor, Disease


def load_knowledge_base() -> dict:
    with open(r'data\diseases.json') as f:
        return json.load(f)


knowledge_base = load_knowledge_base()


def get_details(disease):
    return knowledge_base[disease]['description']


def get_treatments(disease):
    return knowledge_base[disease]['treatment']


def if_not_matched(disease):
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print(f"\nThe most probable disease that you have is {id_disease}\n")
    print("A short description of the disease is given below :\n")
    print(f"{disease_details}\n")
    print("The common medications and procedures suggested by other real doctors are: \n")
    print(treatments + "\n")


# driver function
if __name__ == "__main__":
    case = Disease(
        'no',
        'no',
        'no',
        'no',
        'no',
        'no',
        'no',
        'high',
        'no',
        'no',
        'no',
        'no',
        'no',
    )
    engine = Doctor(knowledge_base, if_not_matched, get_treatments, get_details, case)
    engine.reset()
    engine.run()
