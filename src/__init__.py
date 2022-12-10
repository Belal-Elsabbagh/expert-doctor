from experta import *

from src.disease import Disease


class Greetings(KnowledgeEngine):

    def __init__(self, symptom_map, if_not_matched, get_treatments, get_details, case):
        self.symptom_map = symptom_map
        self.if_not_matched = if_not_matched
        self.get_details = get_details
        self.get_treatments = get_treatments
        self.case: Disease = case
        KnowledgeEngine.__init__(self)

    # code giving instructions on how to use the Expert System
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="find_disease")

    @Rule(Fact(action="find_disease"), NOT(Fact(headache=W())), salience=4)
    def headache(self):
        self.declare(Fact(headache=self.case.headache))

    @Rule(Fact(action="find_disease"), NOT(Fact(back_pain=W())), salience=1)
    def back_pain(self):
        self.declare(Fact(back_pain=self.case.back_pain))

    @Rule(Fact(action="find_disease"), NOT(Fact(chest_pain=W())), salience=1)
    def chest_pain(self):
        self.declare(Fact(chest_pain=self.case.chest_pain))

    @Rule(Fact(action="find_disease"), NOT(Fact(cough=W())), salience=3)
    def cough(self):
        self.declare(Fact(cough=self.case.cough))

    @Rule(Fact(action="find_disease"), NOT(Fact(fainting=W())), salience=1)
    def fainting(self):
        self.declare(Fact(fainting=self.case.fainting))

    @Rule(Fact(action="find_disease"), NOT(Fact(fatigue=W())), salience=1)
    def fatigue(self):
        self.declare(Fact(fatigue=self.case.fatigue))

    @Rule(Fact(action="find_disease"), NOT(Fact(sunken_eyes=W())), salience=1)
    def sunken_eyes(self):
        self.declare(Fact(sunken_eyes=self.case.sunken_eyes))

    @Rule(Fact(action="find_disease"), NOT(Fact(low_body_temp=W())), salience=1)
    def low_body_temp(self):
        self.declare(Fact(low_body_temp=self.case.low_body_temp))

    @Rule(Fact(action="find_disease"), NOT(Fact(restlessness=W())), salience=1)
    def restlessness(self):
        self.declare(Fact(restlessness=self.case.restlessness))

    @Rule(Fact(action="find_disease"), NOT(Fact(sore_throat=W())), salience=1)
    def sore_throat(self):
        self.declare(Fact(sore_throat=self.case.sore_throat))

    @Rule(Fact(action="find_disease"), NOT(Fact(fever=W())), salience=1)
    def fever(self):
        self.declare(Fact(fever=self.case.fever))

    @Rule(Fact(action="find_disease"), NOT(Fact(nausea=W())), salience=1)
    def nausea(self):
        self.declare(Fact(nausea=self.case.nausea))

    @Rule(Fact(action="find_disease"), NOT(Fact(blurred_vision=W())), salience=1)
    def blurred_vision(self):
        self.declare(Fact(blurred_vision=self.case.blurred_vision))

    # different rules checking for each disease match
    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="high"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="low"),
        Fact(sunken_eyes="no"),
        Fact(nausea="high"),
        Fact(blurred_vision="no"),
    )
    def disease_0(self):
        self.declare(Fact(disease="Jaundice"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="high"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def alzheimers(self):
        self.declare(Fact(disease="Alzheimers"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="high"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="low"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def arthritis(self):
        self.declare(Fact(disease="Arthritis"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="high"),
        Fact(cough="low"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="high"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def tuberculosis(self):
        self.declare(Fact(disease="Tuberculosis"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="low"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def asthma(self):
        self.declare(Fact(disease="Asthma"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="low"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(sore_throat="high"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="low"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def sinusitis(self):
        self.declare(Fact(disease="Sinusitis"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="low"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def epilepsy(self):
        self.declare(Fact(disease="Epilepsy"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="high"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="high"),
        Fact(blurred_vision="no"),
    )
    def heart_disease(self):
        self.declare(Fact(disease="Heart Disease"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="high"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="low"),
        Fact(blurred_vision="low"),
    )
    def diabetes(self):
        self.declare(Fact(disease="Diabetes"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="low"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="high"),
        Fact(blurred_vision="low"),
    )
    def glaucoma(self):
        self.declare(Fact(disease="Glaucoma"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="high"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="low"),
        Fact(blurred_vision="no"),
    )
    def hyperthyroidism(self):
        self.declare(Fact(disease="Hyperthyroidism"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="high"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="high"),
        Fact(sunken_eyes="no"),
        Fact(nausea="high"),
        Fact(blurred_vision="no"),
    )
    def heat_stroke(self):
        self.declare(Fact(disease="Heat Stroke"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="yes"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="high"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def hypothermia(self):
        self.declare(Fact(disease="Hypothermia"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="high"),
        Fact(back_pain="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(sore_throat="high"),
        Fact(fatigue="high"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="high"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def coronavirus(self):
        self.declare(Fact(disease="Coronavirus"))

    # when the user's input doesn't match any disease in the knowledge base
    @Rule(Fact(action="find_disease"), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease):
        print("")
        id_disease = disease
        disease_details = self.get_details(id_disease)
        treatments = self.get_treatments(id_disease)
        print("")
        print("Your symptoms match %s\n" % id_disease)
        print("A short description of the disease is given below :\n")
        print(disease_details + "\n")
        print(
            "The common medications and procedures suggested by other real doctors are: \n"
        )
        print(treatments + "\n")

    @Rule(
        Fact(action="find_disease"),
        Fact(headache=MATCH.headache),
        Fact(back_pain=MATCH.back_pain),
        Fact(chest_pain=MATCH.chest_pain),
        Fact(cough=MATCH.cough),
        Fact(fainting=MATCH.fainting),
        Fact(sore_throat=MATCH.sore_throat),
        Fact(fatigue=MATCH.fatigue),
        Fact(low_body_temp=MATCH.low_body_temp),
        Fact(restlessness=MATCH.restlessness),
        Fact(fever=MATCH.fever),
        Fact(sunken_eyes=MATCH.sunken_eyes),
        Fact(nausea=MATCH.nausea),
        Fact(blurred_vision=MATCH.blurred_vision),
        NOT(Fact(disease=MATCH.disease)),
        salience=-999
    )
    def not_matched(
            self,
            headache,
            back_pain,
            chest_pain,
            cough,
            fainting,
            sore_throat,
            fatigue,
            restlessness,
            low_body_temp,
            fever,
            sunken_eyes,
            nausea,
            blurred_vision,
    ):
        print("\nThe bot did not find any diseases that match your exact symptoms.")
        symptoms = Disease(
            headache,
            back_pain,
            chest_pain,
            cough,
            fainting,
            sore_throat,
            fatigue,
            restlessness,
            low_body_temp,
            fever,
            sunken_eyes,
            nausea,
            blurred_vision
        )
        symptoms_list = symptoms.tolist()
        max_count = 0
        max_disease = ""
        for disease_name, disease_symptoms in self.symptom_map.items():
            count = 0
            for ref_symptom, in_symptom in zip(disease_symptoms.values(), symptoms_list):
                if ref_symptom == in_symptom and self.symptom_exists(in_symptom):
                    count += 1
            if count > max_count:
                max_count, max_disease = count, disease_name
        if max_disease != "":
            self.if_not_matched(max_disease)

    @staticmethod
    def symptom_exists(in_symptom):
        return in_symptom in ['high', 'low', 'yes']
