class Disease:
    headache = 'no'
    back_pain = 'no'
    chest_pain = 'no'
    cough = 'no'
    fainting = 'no'
    sore_throat = 'no'
    fatigue = 'no'
    restlessness = 'no'
    low_body_temp = 'no'
    fever = 'no'
    sunken_eyes = 'no'
    nausea = 'no'
    blurred_vision = 'no'

    def __init__(
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
            blurred_vision
    ):
        self.headache = headache
        self.back_pain = back_pain
        self.chest_pain = chest_pain
        self.cough = cough
        self.fainting = fainting
        self.sore_throat = sore_throat
        self.fatigue = fatigue
        self.restlessness = restlessness
        self.low_body_temp = low_body_temp
        self.fever = fever
        self.sunken_eyes = sunken_eyes
        self.nausea = nausea
        self.blurred_vision = blurred_vision

    def tolist(self):
        return [
            self.headache,
            self.back_pain,
            self.chest_pain,
            self.cough,
            self.fainting,
            self.sore_throat,
            self.fatigue,
            self.restlessness,
            self.low_body_temp,
            self.fever,
            self.sunken_eyes,
            self.nausea,
            self.blurred_vision,
        ]
