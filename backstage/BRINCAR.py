import random, math, time

class Country:
    def __init__(self, namek, popk):
        self.name = namek
        self.population = popk
        self.eco = popk*22000*0.04
        rand = random.randrange(3, 8, 1)/10
        self.army = math.floor(rand*self.population*0.65/90000) + 2
        self.airforce = math.floor(rand*self.population*0.15/5000) + 1
        self.navy = math.floor(rand*self.population*0.20/90000) +1
        self.allies = []
        self.lost = False
        self.leader = namek
        self.leader_title = "Something"
        self.bot = True

    def story(self):
        print ("")
        print (self.name,"Data:")
        print ("Population:", self.population )
        print ("Economy:", self.eco)
        print ("Army Forces:", self.army)
        print ("Air Forces:", self.airforce)
        print ("Naval Forces:", self.navy)
        print ("")
    def battle(self, result, gamer):
        if result == 1:
            k = random.randrange(1, 10, 1)
        else:
            k = random.randrange(4, 55, 1)
        popl = -math.floor(self.population*k/1000)
        armyl = -math.floor(self.army * k / 100) - random.randint(0, 2)
        airforcel = -math.floor(self.airforce * k / 100) - random.randint(0, 2)
        navyl = -math.floor(self.airforce * k / 100) - random.randint(0, 2)
        if popl >= self.population or self.population <= 0 or armyl >= self.army or self.army <= 0 :
            self.lost = True
        else:
            self.population += popl
            self.army += armyl
            self.airforce += airforcel
            self.navy +=navyl
            if self.army < 0: self.army = 0
            if self.airforce < 0: self.airforce= 0
            if self.navy < 0: self.navy= 0
            print("Population:", popl," Now with:", self.population)
            print("Army:",armyl, "Now with:", self.army)
            print("Air Force:", airforcel, "Now with:", self.army)
            print("Navy:", navyl, "Now with:", self.airforce)
    def add_allie(self, other):
        self.allies.append(other)
        print (other)
    def del_allie(self,other):
        self.allies.pop(other)
    def turn(self):
        self.population += math.floor(self.population*0.05)
        self.army += math.floor(self.army*0.05)
        self.airforce += math.floor(self.airforce*0.03)
        self.navy += math.floor(self.navy*0.02)
        self.eco -= self.army*100000 + self.airforce*500000 + self.navy*100000
        contrib_alies = 0
        for alie in self.allies:
            contrib_alies += alie.eco*0.000001
        self.eco += contrib_alies
    def buy_units(self, army = 0, airforce = 0, navy = 0):
        army = int(army)
        airforce = int(airforce)
        navy = int(navy)
        if army != 0 and (self.eco - army*100000)> 0:
            self.army += army
            self.eco -= army*10000
        elif army == 0:
            a = 0
        else:
            print ("You couldn't buy your army units.")
        if airforce!= 0 and (self.eco - airforce*5000000)> 0:
            self.airforce += airforce
            self.eco -= airforce*5000
        elif airforce == 0:
            a = 0
        else:
            print ("You couldn't buy your air force units.")
        if navy != 0 and (self.eco -navy*2500000) >0:
            self.navy += navy
            self.eco -= navy*10000
        elif navy == 0:
            a = 0
        else:
            print ("You couldn't buy your naval units.")



listk = ['Russia', 'Germany', 'France', 'United Kingdom', 'Italy', 'Spain', 'Ukraine', 'Poland', 'Romania',
             'Netherlands', 'Belgium', 'Greece', 'Portugal', 'Czech Republic', 'Hungary', 'Sweden', 'Belarus',
             'Austria', 'Switzerland', 'Bulgaria', 'Serbia', 'Denmark', 'Finland', 'Slovakia', 'Norway', 'Ireland',
             'Croatia', 'Bosnia and Herzegovina', 'Moldova', 'Lithuania', 'Albania', 'Macedonia', 'Slovenia',
             'Latvia', 'Kosovo', 'Estonia', 'Montenegro', 'Luxembourg', 'Malta', 'Iceland']
pop = [143455000, 80640000, 66616416, 64231000, 59789000, 46958000, 45461000, 38548000, 19858000, 16795000,
               11162000, 10758000, 10609000, 10519000, 9894000, 9595000, 9460000, 8477000, 8075000, 7261000, 7203000,
               5612000, 5436000, 5413000, 5077000, 4662000, 4258000, 3847000, 3486000, 2956000, 2783000, 2066000,
               2062000, 2011000, 1826000, 1283000, 620000, 542000, 419000, 324000]
clk = []
def generator():
    for k in range(0,len(listk)):
        name = listk[k]
        popest = pop[k]
        clk.append(Country(name, popest))
    print ("Done")
generator()


def find_country(namel): #returns country pointer!!!!!!!!
    for i in range(0, len(clk)):
        if clk[i].name == namel:
            return clk[i]
        else:
            continue
print(find_country("Portugal"))