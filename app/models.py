class Player:
    def __init__(self, data):
        self.playerID = data.get('playerID')
        self.birthYear = data.get('birthYear')
        self.birthMonth = data.get('birthMonth')
        self.birthDay = data.get('birthDay')
        self.birthCountry = data.get('birthCountry')
        self.birthState = data.get('birthState')
        self.birthCity = data.get('birthCity')
        self.deathYear = data.get('deathYear')
        self.deathMonth = data.get('deathMonth')
        self.deathDay = data.get('deathDay')
        self.deathCountry = data.get('deathCountry')
        self.deathState = data.get('deathState')
        self.deathCity = data.get('deathCity')
        self.nameFirst = data.get('nameFirst')
        self.nameLast = data.get('nameLast')
        self.nameGiven = data.get('nameGiven')
        self.weight = data.get('weight')
        self.height = data.get('height')
        self.bats = data.get('bats')
        self.throws = data.get('throws')
        self.debut = data.get('debut')
        self.finalGame = data.get('finalGame')
        self.retroID = data.get('retroID')
        self.bbrefID = data.get('bbrefID')

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}