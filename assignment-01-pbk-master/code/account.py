import person
import group
userClassTable = []
groupTable=[]
class account:
    def __init__(self):
        self.userList = userClassTable
        self.groupList=groupTable

    def get_users(self):
        result = [] 
        for k in self.userList:
            result.append(k.get_name())
        return(result)
    def validate_user(self, username, pw):
        for k in self.userList:
            if k.get_username() == username: 
                if k.get_password() == pw:
                    return True
                else:
                    return False
    def get_user_by_username(self, username):
        for tick, k in enumerate(self.userList):
            if k.get_username() == username:
                return self.userList[tick]
        print("\nThere is no user with this username , you can proceed.\n")
        return False
    def add_new_user(self, f_name, l_name, username, password, dob):
        newDude = person.person(f_name, l_name, username, password, dob,"","")
        self.userList.append(newDude)
        # self.save_user()
        print("\nYou've been successfully signed up!\n")

    def newPost(self,username,post):
        for k in self.userList:
            if k.get_username() == username:
                # fname=k.get_firstname()
                # lname=k.get_lastname()
                # userName=k.get_username()
                # pass=k.get_password()
                # dOb=k.get_dob()
                k.addpost(post)

    def displaypost(self,username):
        for k in self.userList:
            if k.get_username() == username:
                if len(k.getpost())>0:
                    for i in k.getpost():
                        print(i)
                else:
                    print("\nNo posts to display.\n")

    def showUsers(self,user_Name):
        for k in self.userList:
            print(k.get_firstname(),"",k.get_lastname())
        rentry='99'
        while rentry!='2':
            rentry = input('\n 1. Add friends to yours friend\'s list\n 2. See your friend\'s posts\n 3. Show friends list\n 4. Go back to home page\n Please, enter 1, 2, 3 or 4 : ')
            if rentry=='1':
                last_Name=input("\nEnter the last name of the friend to add it to your friend\'s list : ")
                for k in self.userList:
                    if k.get_username() == user_Name:
                        for l in self.userList:
                            if l.get_lastname() == last_Name:
                                k.addfriends(l.get_username())
                                print(l.get_firstname()," ",l.get_lastname()," is added to your friend\'s list\n")
 
            elif rentry=='2':
                list_of_friends=[]
                posts_by_friends={}
                for k in self.userList:
                    if k.get_username() == user_Name:
                        list_of_friends=k.get_friends()
                for i in list_of_friends:
                    for k in self.userList:
                        if i == k.get_username():

                            posts_by_friends.update({k.get_username():k.getpost()})
                if(len(posts_by_friends))>0:
                    print(posts_by_friends)
                else:
                    print("\nNo post from friend\'s\n")
                # break
                rentry='1'
            elif rentry=='3':
                for k in self.userList:
                    if k.get_username()==user_Name:
                        if len(k.get_friends())>0:
                            print(k.get_friends())
                        else:
                            print("\nNo friends to display.\n")
            elif rentry=='4':
                break


    def get_group_by_groupName(self,group_name):
        for tick, k in enumerate(self.groupList):
                if k.get_groupName() == group_name:
                    return self.groupList[tick]
        print("\nThere is no group with this name\n")
        return False

    def searchUsers(self,f_name):
        for k in self.userList:
            if k.get_firstname() == f_name:
                print(f_name+" "+k.get_lastname())

    def showGroups(self,memberName):
        if len(self.groupList)>0:
            for k in self.groupList:
                print(k.get_groupName())
        else:
            print("No groups present.\n")
        
        reentry=0
        while reentry!='1':
            # print("1. Create group\n 2. Join group\n 3.Leave group\n Enter your choice 1, 2,or 3 : ")
            reentry=input(" \n1. Create group\n 2. Join group\n 3.Leave group\n 4. Show joined groups\n 5. Go back to home page\n Enter your choice 1, 2, 3, 4 or 5 : ")
            if reentry=='1':
                groupName=input("\nEnter the name of the group to create : ")
                a=len(self.groupList)
                b=0
                for k in self.groupList:
                    b=b+1
                    if k.get_groupName()==groupName:
                        print("\nGroup already exist with that name\n")
                        break
                if a==b:
                    newGroup = group.group(groupName,"","")
                    self.groupList.append(newGroup)
                    for k in self.groupList:
                        if k.get_groupName()==groupName:
                            k.add_groupmembers(memberName)
                            print("\nYou've been successfully created the group!")

                reentry='1' 
            elif reentry=='2':
                grpName=input("\nEnter the name of the group you want to join : ")
                for k in self.groupList:
                    if grpName==k.get_groupName():
                        k.add_groupmembers(memberName)
                        print("\nYou are successfully added to ",k.get_groupName()," group.")
                # reentry='1'
            elif reentry=='3':
                leaveGroup=input("\nEnter the name of the group you want to leave : ")
                
                for k in self.groupList:
                    if leaveGroup==k.get_groupName():
                        for i in k.get_groupmembers():
                            if memberName==i:
                                grppost={}
                                k.get_groupmembers().remove(memberName)
                                print("\nYou have left the group.\n")
                                grppost=k.showpost()
                                if memberName in grppost:
                                    del k.showpost()[memberName]
            elif reentry=='4':
                entry='2'
                while(entry!='1'):
                    for k in self.groupList:
                        list=[]
                        list=k.get_groupmembers()
                        for i in list:
                            if i == memberName:
                                print(k.get_groupName())
                    print("\n 1. Add post to group\n 2. See posts of group\n 3. Go back\n Enter your choice 1, 2 or 3 : ")
                    choice=input()
                    if choice=='1':
                        g_name=input("\nTo post the you have to be the member of the group. Enter the group name in which you want to post. : ")
                        post_msg=input("\nEnter the post message : ")
                        for k in self.groupList:
                            if k.get_groupName()==g_name:
                                list=[]
                                list=k.get_groupmembers()
                                for i in list:
                                    if i == memberName:
                                        k.add_post(memberName,post_msg)
    
                    elif choice=='2':
                        grp_Name=input("\nTo view the post you have to be member of that group. Enter the group name to view the posts : ")
                        for k in self.groupList:
                            if k.get_groupName()==grp_Name:
                                list=[]
                                list=k.get_groupmembers()
                                for i in list:
                                    if i == memberName:
                                        if len(k.showpost())>0:
                                            print(k.showpost())
                                        else:
                                            print("\nNo posts in the group to print\n")
                    elif choice=='3':
                        entry='1'
            else:
                break