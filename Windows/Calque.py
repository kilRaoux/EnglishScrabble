class Calque:
    """
    Classe stoquant des GameObjects.
    Permet dans une scene de gérer l'ordre d'affichage des composants graphiques.
    number correspond au numero global du calque
    """
    number = 0
    def __init__(self,scene):
        """
        Constructeur.
        :param scene: Scene du calque.
        """
        self.master = scene
        self.items = [] #Liste des items
        self.number = self.__class__.number
        self.__class__.number += 1
    def add(self,obj):
        """
        Ajoute un composant au calque (a self.items)
        :param obj: composant a ajouter
        :return: None
        """
        self.items.append(obj)
    def delete(self,obj):
        """
        Enleve l'obj au calque (a self.items)
        :param obj: l'obj a enlever
        :return: 0 si l'obj appartient a self.items sinon 1
        """
        try:
            self.items.remove(obj)
            return 0
        except: return 1
    def update(self):
        """
        Met a jour tout les composants
        :return: None
        """
        for i in self.items:
            i.update()
    def __getitem__(self, item):
        """
        Methode special.
        Calque[i] renvoi self.items[i]
        :param item: index de l'item
        :return: l'item si item < len(self.items) sinon 0
        """
        if item < len(self.items):
            return self.items[item]
        else:
            return 0
    def __str__(self):
        res = "Calque n° {}".format(self.number)
        res += "\n -- nombre d'item:{}".format(len(self.items))
        for i in self.items:
            res += "\n ---- {},{},{}".format(i.__class__,i.x,i.y)
        return res