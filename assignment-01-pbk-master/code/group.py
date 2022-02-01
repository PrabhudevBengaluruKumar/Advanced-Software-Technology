class group:
    def __init__(self,groupname,posts,groupmembers):
        self.groupname=groupname
        self.posts={}
        self.groupmembers=[]
    
    def add_groupmembers(self,memberName):
        self.groupmembers.append(memberName)
    def get_groupmembers(self):
        return(self.groupmembers)
    def add_post(self,membername,postmessage):
        post=[]
        if membername in self.posts.keys():
            post=self.posts[membername]
        post.append(postmessage)
        self.posts.update({membername:post})
    def showpost(self):
        return(self.posts)
    def get_groupName(self):
        return(self.groupname)