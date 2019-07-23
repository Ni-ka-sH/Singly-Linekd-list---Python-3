class box:
    def __init__(self,names):
        self.names = names
        self.next = None
class squad:
    def __init__(self):
        self.first = None
        self.second = None
    def addin(self,names):
        if self.first is None:
            self.first = box(names)
            self.second = None
        else:
            self.second.next = box(names)
            self.second = self.second.next
    def show(self):
        print(("Team "+ team_name).center(70,':'))
        now = self.first
        while now:
            print(now.names,end=' ')
            if now.next is not None:
                print(',',end='')
            now = now.next
    def num(self,num):
        if players<num:
            print('There are only',players,'players in the team')
            for j in range(num-players):
                print((num-players)-j,'players remaining from entry, if u wanna add types S :',end='')
                choice = str(input())
                if choice == 'S' or choice=='s':
                    self.addin(str(input('Enter newbie name :')))
                    print('\nNew team list :',end='\n')
                    self.show()
                else:
                    print('Enter a valid number.')

        else:
            now = self.first
            count = 1
            while now:
                if count==num:
                    print("The player at position ",num,"is",now.names)
                    break
                count+=1
                now = now.next
    def who(self,noobie):
        pos = 1
        now = self.first
        check = 0
        while now:
            if now.names.lower() == noobie.lower():
                print(noobie," is at position ",pos)
                check = 1
                break
            else:
                now = now.next
                pos+=1
        if check==0:
            print('There is no player named',noobie," in the team")
            see = str(input('if u wanna add '+noobie+" to team type s"))
            if see == 's'.lower():
                self.addin(noobie)
                print('Team',team_name,'has added a new player ',noobie)
                self.show()


team = str(input('Enter team name :'))
team_name = team
team = squad()
print("\n",('Welcome team '+team_name).center(50,':'))
players = int(input('Enter the number of players in '+team_name+' :'))
for i in range(1,1+players):
    team.addin(str(input('Enter player name : ')))
team.show()
team.num(int(input('\nEnter a number : ')))
team.who(str(input('\nEnter player name : ')))
