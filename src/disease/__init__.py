class Disease:
    headache = None
    back_pain = None
    chest_pain = None
    cough = None
    fainting = None
    sore_throat = None
    fatigue = None
    restlessness = None
    low_body_temp = None
    fever = None
    sunken_eyes = None
    nausea = None
    blurred_vision = None

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
