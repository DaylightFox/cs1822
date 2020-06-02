from Attacks import *

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
    
    def manageInteractions(self, sticky=True):
        """
        intDetector is the function that detects the interaction
        intResolver is the function that resolves the interaction
        sticky is True if the interations occour every game cycle(frame)
        """
        for i in range(len(self.interactor)):
            inter = self.interactor[i]
            for j in range(len(self.interacted)):
                inted = self.interacted[j]
                if sticky or not self.interactions[i,j]:
                    if self.intDetector(inter, inted):
                        #self.interactions[i][j] = True
                        self.intResolver(inter, inted)

class AttackCreatureInteraction(Interaction):
    def __init__(self, attacks, creatures):
        super().__init__(attacks, creatures)

    def intDetector(self, attack, attacked):
        return attack.hit_creature(attacked)
        
    def intResolver(self, attack, attacked):
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
    
    def intDetector(self, attack, room):
        if isinstance(attack, ProjectileAttack):
            return attack.hit_room(room)
        
    def intResolver(self, attack, room):
        if isinstance(attack, ProjectileAttack):
            attack.done = True
    
    #def manageInteractions(self):
        #super().manageInteractions(hit_detector, hit_resolver)

class CreatureCreatureInteraction(Interaction):
    def __init__(self, creatures):
        super().__init__(creatures, creatures)
    
    def intDetector(self, creature1, creature2):
        return (creature1.pos - creature2.pos).length() <= (creature1.radius + creature2.radius)
    
    def intResolver(self, creature1, creature2):
        difference = creature2.pos - creature1.pos
        newPos = creature2.pos + difference.normalize().multiply(creature1.radius + creature2.radius)
        creature2.pos = newPos
