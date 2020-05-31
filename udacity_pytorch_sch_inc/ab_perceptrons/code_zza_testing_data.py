# A popo(plain old py object) class containing data, its correct output and its prediction output
class testing_data:
    inp1 = 0
    inp2 = 0
    predictive_result = False
    correct_result = False

    def __init__(self, inp1, inp2, correct_result=False):
        self.inp1 = inp1
        self.inp2 = inp2
        self.correct_result = correct_result
    def set_prediction(self, prediction:bool):
        self.predictive_result = prediction

    def __str__(self):
        i1 = "inp1=" + str(self.inp1 != 0)      +"(%i)"%self.inp1
        i2 = "inp2=" + str(self.inp2 != 0)      +"(%i)"%self.inp2
        correct_result = "correct results=" + str(self.correct_result)
        predictive = "predictive results=" + str(self.predictive_result)

        s = i1 + '  ;  ' + i2 + '  ;  ' + correct_result + '  ;  ' + predictive
        return s

    def __repr__(self):
        return str(self)
