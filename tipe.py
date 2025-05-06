import random
class School:
    fatalty = 1
    def __init__(self, fatality, mark, predmet):
        self.fatalty=fatality
        self.mark = mark
        self.predmet = predmet

    def bell(self):
        print(f"Началась/лся {self.predmet}. Уровень усталости и чувства депресии: {self.fatalty}, а оценка, поставленная учителем: {self.mark}")

    
fizra = School(random.randint(0, 50), random.randint(0, 5), random.choice(["Физра", "Математика", "Русский язык"]))
fizra.bell()
        
