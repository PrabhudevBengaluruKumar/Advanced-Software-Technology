class Person:
    def __init__(self, f_name, l_name, username, password,dob,post,friends):
        self.f_name = f_name
        self.l_name= l_name
        self.username = username
        self.password = password
        self.dob=dob
        self.post=[]
        self.friends=[]
    def get_firstname(self):
        return(self.f_name)
    def get_lastname(self):
        return(self.l_name)
    def get_username(self):
        return(self.username)
    def get_password(self):
        return(self.password)
    def get_dob(self):
        return(self.dob)
    def get_details(self):
        return(self.name,self.u_name,self.dob)
    def add_post(self,post):
        self.post.append(post)
    def get_post(self):
        return(self.post)
    def add_friends(self,friendName):
        self.friends.append(friendName)
    def get_friends(self):
        return(self.friends)


# p1=person("a","aa","020502","a","aaa")
# b=p1.showdetails()
# print(b)
