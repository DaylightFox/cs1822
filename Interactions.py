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
    
    def manageInteractions(self, intDetector, intResolver, sticky=True):
        """
        intDetector is the function that detects the interaction
        intResolver is the function that resolves the interaction
        sticky is True if the interations occour every game cycle(frame)
        """
        for inter in self.interactor:
            inter = self.interactor[i]
            for inted in self.interacted:
                inted = self.interacted[j]
                if sticky or not self.interactions[i,j]:
                    if intDetector(inter, inted):
                        intResolver(inter, inted)