class Interaction:
    def __init__(self, array1, array2):
        self.interactor = array1
        self.interacted = array2
        self.interactions = []
        for i in self.interactor:
            self.interactions.append([False] * len(self.interacted))
    
    def appendInteractor(self, interactor):
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
                        interactions[i][j] = True
                        intResolver(inter, inted)

class AttackCreatureInteraction(Interaction):
    def __init__(self, attacks, creatures):
        super().__init__(attacks, creatures)

    def hit_detector(attack, attacked):
        attack.hit_creature(attacked)
        
    def hit_resolver(attack, attacked):
        attack.deal_damage(attacked)
        if isinstance(attack, ProjectileAttack):
                attack.done = True

    def manageInterations(self, sticky=True):
        super().manageInterations(hit_detector, hit_resolver)
        removeList = []
        for creature in interacted:
            if creature.killed:
                creature.die()
                removeList.append(creature)

class AttackRoomInteraction(Interaction):
    def __init__(self, attacks, rooms):
        super().__init__(attacks, rooms)
    
    def hit_detector(attack, room):
        attack.hit_room(room)
        
    def hit_resolver(attack, room):
        if isinstance(attack, ProjectileAttack):
            attack.done = True
    
    def manageInteractions(self):
        super().manageInteractions(hit_detector, hit_resolver)
