class Group:
    def __init__(self,groupname,posts,groupmembers):
        self.groupname=groupname
        self.posts={}
        self.groupmembers=[]
    
    def add_group_members(self,memberName):
        self.groupmembers.append(memberName)
    def get_group_members(self):
        return(self.groupmembers)
    def add_post(self,membername,postmessage):
        post=[]
        if membername in self.posts.keys():
            post=self.posts[membername]
        post.append(postmessage)
        self.posts.update({membername:post})
    def show_post(self):
        return(self.posts)
    def get_group_name(self):
        return(self.groupname)
