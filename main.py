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
        print ("---")
        print ("Leader", self.leader_title, ",", self.leader)
        print ("Is Bot?", self.bot)
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
        self.allies.remove(other)
    def mod_leader(self,newleader):
        self.leader = newleader
    def mod_titleleader(self, newtitle):
        self.leader_title = newtitle
    def mod_bot(self, res):
        self.bot = res
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
            if self.bot is False:
                print ("You couldn't buy your army units.")
                return False
        if airforce!= 0 and (self.eco - airforce*5000000)> 0:
            self.airforce += airforce
            self.eco -= airforce*5000
        elif airforce == 0:
            a = 0
        else:
            if self.bot is False:
                print ("You couldn't buy your air force units.")
                return False
        if navy != 0 and (self.eco -navy*2500000) >0:
            self.navy += navy
            self.eco -= navy*10000
        elif navy == 0:
            a = 0
        else:
            if self.bot is False:
                print ("You couldn't buy your naval units.")
                return False



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


def peso(CountryK):
    return CountryK.army + CountryK.airforce*10 + CountryK.navy*5

def twobattle(Country1, Country2):
    weighted_1 = peso(Country1)
    weighted_2 = peso(Country2)
    prob1 = random.randrange(1, 50, 1)*weighted_1/weighted_2/100
    prob2 = random.randrange(1, 50, 1) * weighted_2 / weighted_1/100
    if prob1 > prob2:
        return Country1
    else:
        return Country2

def checkloss(Country1, Country2):
    if (Country1.lost == True) or (Country2.lost == True):
        return True
    else:
        return False

def cstr(text): #80
    if len(text) >80:
        for k in range(len(text)//80 +2):
            print(text[80*(k-1): 80*k])
    else:
        print (text)


def allies_ask(Playr, allying):
    p = abs(7*2.27**(-Playr.losses))
    rint = random.randint(0,100)
    if rint <= p:
        Playr.add_allie(allying.name)
        allying.add_allie(Playr.name)
        return True
    else:
        return False

def allies_begin(Playr,Enmy):
    pool = listk
    pool.pop(pool.index(Playr.name))
    pool.pop(pool.index(Enmy.name))
    added = []
    for k in pool:
        p_land = random.randint(0,100)
        if p_land <= 12:
            Playr.add_allie(k)
            added.append(k)
        else:
            continue
    print("-" * 80)
    print("-" * 80)
    print("ALLIES REPORT\n")
    if len(added) >0:
        text = "Congratulations! Other countries have revised your proposal for war against "+ Enmy.leader +" and the result is now clear. Next follows a list of nations which have allied you. If you wish to remove them, you may do so later."
        cstr(text)
        for each in added:
            print (each)
    else:
        text = Playr.leader + " your advisers are not eager to share this with you but someone must. We humbly ask your apology but our diplomatic efforts weren't strong enough to provoke any reaction from them."
        cstr(text)

def endgame(lost):
    print ("-"*80)
    time.sleep(0.5)
    print("-"*10, end ="")
    time.sleep(0.2)
    print ("-"*60, end="")
    time.sleep(0.3)
    print ("-"*10)
    print ("")
    print ("This Game is Over")
    if lost.bot is True:
        print ("Congratulations, you have won.")
    else:
        print ("You have lost.")
        print ("If you may choose so, you may play again!")
def enemy_buy(EnCount, PlaCount):
    rank = random.randrange(45,90)/100
    army_b = PlaCount.army*rank
    airforce_b = PlaCount.airforce*rank
    navy_b = PlaCount.navy*rank
    n=2
    while EnCount.buy_units(army_b,airforce_b,navy_b) is False:
        army_b = PlaCount.army * rank/n
        airforce_b = PlaCount.airforce * rank/n
        navy_b = PlaCount.navy * rank/n
        n += 1

def choice(CountryK):
    print ("-"*80)
    print ("List of Available Commands:")
    print ("B - Buy Units")
    print ("C - Check my Nation data")
    print ("A - Allies Operations")
    print ("P - Pass Turn or Proceed Without Action")
    case = input(">")
    while case != "P":
        if case == "C":
            print("-" * 80)
            print ("Population:", CountryK.population)
            print ("Money Available:", CountryK.eco )
            print ("Army Size:", CountryK.army )
            print ("Air Force Size:", CountryK.airforce)
            print ("Navy Size:", CountryK.navy)
            case = input(">")
            print("-" * 80)
        elif case == "A":
            print("-" * 80)
            print ("Welcome to your Diplomatic Screen, what do you want to do?")
            print ("R - Diplomatic Report")
            print ("B - Break Diplomatic Relation")
            print ("P - Proceed")
            diplo = input(">")
            while diplo != "P":
                if diplo == "R":
                    print ("Following, a list of you allies:")
                    for each in CountryK.allies:
                        print(each)
                    diplo= input(">")
                elif diplo == "B":
                    print("Following, a list of you allies:")
                    for each in CountryK.allies:
                        print(each)
                    print ("Which do you want to remove? Press C to Continue")
                    remov = input(">")
                    if remov == "C" or remov == "c":
                        continue
                    else:
                        if remov in CountryK.allies:
                            CountryK.del_allie(remov)
                            print ("Removed", remov,"successfuly.")
                        else:
                            print ("Input Not Valid.")
                        print ("B to remove more, P to Proceed:")
                        diplo = input(">")
                else:
                    print ("This is not a valid command, please re-enter.")
                    diplo = input(">")
            case = input(">")
            print("-" * 80)
        elif case == "B":
            print("-" * 80)
            print("You currently have:", CountryK.eco, "to spend on your Military.")
            print("1 Combat Brigade (Army) Costs 100,000")
            print("1 Air Force Combat Fighter Costs 5,000,000")
            print("1 Naval Asset Costs 2,500,000")
            print("")
            cstr("For each kind, input how many units you want to buy, if you wish to not buy simply enter 0")
            army = input("Army Combat Brigades >")
            airforce = input("Air Force Combat Fighter >")
            naval = input("Naval Unit >")
            CountryK.buy_units(army, airforce, naval)
            print("What to do next?")
            case = input(">")
            print("-" * 80)
        else:
            print("-" * 80)
            print ("Please enter a real command: B,C, or P")
            case = input(">")
            print("-" * 80)

def turn2 (Country1, Country2):
    print("-" * 80)
    battle = False
    randomc = random.randrange(0,100,1)
    if randomc <80:
        battle = True
    enemy_buy(Country2, Country1)
    choice(Country1)
    if battle is True:
        winner = twobattle(Country1, Country2)
        if winner == Country1:
            loser = Country2
        else:
            loser = Country1
        cstr("And the winner of the battle is "+ winner.leader+ ", led by the"+ winner.leader_title+ " "+ winner.leader + " .")
        winner.battle(1, winner)
        print("And the loser is", loser.leader)
        loser.battle(0, loser)
    if checkloss(Country1, Country2) is False:
        turn3(Country1, Country2)
    elif checkloss(Country1, Country2) is True:
        if Country2.lost is True:
            endgame(Country2)
        else:
            endgame(Country1)
    else:
        print ("Unexpected ERROR")

def turn3(Country1, Country2):
    print("-" * 80)
    battle = False
    choice(Country1)
    #Enemy buys random units
    print ("It's your turn,", Country1.leader_title,".")
    print ("Are you willing to go to war? Y/N")
    call = input(">")
    while call not in ["Y","N"]:
        print("Please choose a valid option: Y for Yes or N for No")
        call = input(">")
    if call == "Y":
        battle = True
    else: battle = False
    if battle is True:
        winner = twobattle(Country1, Country2)
        if winner == Country1:
            loser = Country2
        else:
            loser = Country1
        cstr("And the winner of the battle is"+  winner.leader+ ", lead by the "+ winner.leader_title+ winner.leader+ " .")
        winner.battle(1, winner)
        print("And the loser is", loser.leader)
        loser.battle(0, loser)
        print("-" * 80)
    if checkloss(Country1, Country2) is False:
        turn2(Country1, Country2)
    elif checkloss(Country1, Country2) is True:
        if Country2.pais.lost is True:
            endgame(Country2)
        else:
            endgame(Country1)
    else:
        print ("Unexpected ERROR")

def printnations():
    max = 0
    for k in listk:
        if len(k) > max: max = len(k)
    for l in listk:
        if (listk.index(l) + 1) % 3 == 0:
            print(" ", l)
        else:
            print(" ", l, " " * (max - len(l)), "|", end="")
def main():
    max = 0
    for k in listk:
        if len(k) > max: max = len(k)
    print ("-"*80)
    print ("Welcome to Titanium Warz(z)!")
    print ("\n")
    print ("Mark 2 by Chekhov.")
    print ("-"*80)
    print ("First things first! What is your user name?")
    name = input(">")
    print ("And what title would you like to use?")
    title = input(">")
    print ("Very nice choice!, to start you need to choose a country amongst the following:")
    print ("-"*80)
    for l in listk:
        if (listk.index(l) +1)%3 == 0 :
            print (" ", l)
        else:
            print (" ", l," "*(max-len(l)),"|", end="")
    print ("")
    count = input(">")
    while count not in listk:
        print("Please Retry, Your chosen nation should be listed")
        count = input(">")
    Player = find_country(count)
    Player.mod_leader(name)
    Player.mod_titleleader(title)
    Player.mod_bot(False)
    print ("Data from your Country:")
    Player.story()
    print ("-"*80)
    cstr("Now, time to choose your first opponent. Take a new look at the first list and choose your opponent!")
    opus = input(">")
    while opus == count or opus not in listk:
        print("Please Retry, Your enemy should be listed and not be yourself")
        opus = input(">")
    Enemy = find_country(opus)
    print("Data from your enemy's country:")
    Enemy.story()
    print("-" * 80)
    print("\n" * 2)
    print("-" * 80)
    print("Turn 1! Your enemy is getting eager to fight you! Are you up for the challenge? ")
    cstr("".join("This is your first battle" + Player.leader_title + Player.leader +", your citizens are weary of your war and hope it goes soon or that their daughters and their sons return safe and sound. It's in your hands."))
    print("")
    winner = twobattle(Player,Enemy)
    if winner == Player:
        loser = Enemy
    else:
        loser = Player
    cstr ("And the winner of the first battle is "+ winner.leader+ ", lead by the "+ winner.leader_title +" "+ winner.leader +" .")
    winner.battle(1, winner)
    print ("And the loser is", loser.leader)
    loser.battle(0, loser)
    allies_begin(Player, Enemy)
    turn2(Player, Enemy)

main()