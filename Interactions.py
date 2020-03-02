class Interaction:
    def __init__(self, array1, array2):
        self.interactor = array1
        self.interacted = array2
        self.interactions = []
        for i in self.interactor:
            self.interactions.append([False] * len(self.interacted))
    
    def appendInteractor(self, interator):
        self.interactor.append(interactor)
        self.interactions.append([False] * len(self.interacted))
    def appendInteracted(self, interacted):
        self.interacted.append(interacted)
        for i in range(len(self.interactor)):
            self.interactions[i].append(False)
    
    def manageCollisions(self):
        pass
