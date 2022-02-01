from neo4j import GraphDatabase
class Database:

    def create_session(self):
        graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        session=graphdb.session()
        return session

    def create_person_node(self,first_name,last_name,user_name,password,dob):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        session.run("Create (a:Person {firstName:$fname, lastName:$lname,userName:$uname,password:$passWord,dateofbirth:$dob})",fname=first_name,lname=last_name,uname=user_name,passWord=password,dob=dob)

    def get_person_node_details(self,user_name):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        result=session.run("MATCH (a:Person {userName:$uname}) return a.firstName,a.lastName,a.dateofbirth,a.posts",uname=user_name)
        print(result.single())

    def add_post_to_person_node(self,user_name,message):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        msg=[]
        msg.append(user_name)
        # msg.append(':')
        msg.append(message)
        session.run("MATCH (a:Person {userName:$uname}) SET a.posts=$msg",uname=user_name,msg=msg)

    def add_friends_to_person_node(self,user_name,friend_name):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        session.run("MERGE (a:Person {userName:$uname})  SET a.friendsList=$friendname",uname=user_name,friendname=friend_name)
        # session.run("create (a:Person {userName:$uname}) -[KNOWS]-->(b:Person {userName:$friendname}) ",uname=user_name,friendname=friend_name)
        session.run("MATCH (a:Person),(b:Person) WHERE a.userName = $uname AND b.userName = $friendname CREATE (a)-[r:knows]->(b)",uname=user_name,friendname=friend_name)

        

    def get_post_from_person_node_details(self,user_name):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        result=session.run("MATCH (a:Person {userName:$uname}) return a.posts",uname=user_name)
        # print(result.single())

        list=[]
        for posts in result:
            list.append(posts)
            print(posts)
        # print(list)

        

    def get_friends_list_from_person_node_details(self,user_name):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        result=session.run("MATCH (a:Person {userName:$uname}) return a.friendsList",uname=user_name)
        print(result.single())

    def get_friends_post(self,user_name):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        result=session.run("MATCH (a:Person {userName:$uname})-[KNOWS]->(b:Person) return b.posts",uname=user_name)
        print(result.single())


    def create_group_node(self,group_name,posts,members_name):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        session.run("Create (a:Group {groupName:$gname, post:$post,membersName:$msname})",gname=group_name,post=posts,msname=members_name)
        session.run("MERGE (a:Person {userName:$uname})  SET a.groupsList=$groupname",uname=members_name,groupname=group_name)
        session.run("MATCH (a:Person),(b:Group) WHERE a.userName = $uname AND b.groupName = $groupname CREATE (a)-[r:member_of]->(b)",uname=members_name,groupname=group_name)
    
    def get_groups(self):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        result=session.run("MATCH (n:Group) RETURN n")
        # print(result.single())
        list=[]
        for groups in result:
            list.append(groups)
            print(groups)
        # print(list)


    def get_person(self):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        result=session.run("MATCH (n:Person) RETURN n.userName")
        # print(result.single())
        list=[]
        for persons in result:
            list.append(persons)
            print(persons)
        # print(list)


    def add_post_to_group(self,group_name,posts,members_name):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        result=session.run("MATCH (a:Group {groupName:$gname}) return a.posts",gname=group_name)
        # msgg=[]
        # for i in result:
        #     msgg.append(i)
        mssg=members_name+' '+posts
        # msg.append(members_name)
        # msg.append(':')
        msg=[]
        # msg.append(msgg)
        msg.append(mssg)
        # msg.append(posts)
        session.run("MATCH (a:Group {groupName:$gname}) SET a.posts=$msg",gname=group_name,msg=msg)

    def get_post_from_group(self,group_name):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        result=session.run("MATCH (a:Group {groupName:$gname}) return a.posts",gname=group_name)
        print(result.single())

    def leave_group(self,group_name,members_name):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        # msgs=session.run("MATCH (a:Group {groupName:$gname}) return a.posts",gname=group_name)
        session.run("MATCH (a:GROUP {groupName:$gname}) MATCH a.membersName:$msname DETACH DELETE a.members",gname=group_name,msname=members_name)
        
    def search_person_by_first_name(self,first_name):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        result=session.run("Match (a:Person{firstName:$fname}) return a.firstName,a.lastName",fname=first_name)
        print(result.single())

    def join_group(self,group_name,member_name):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        session.run("MATCH (a:Group {groupName:$gname}) SET a.membersName=$mname",gname=group_name,mname=member_name)
        session.run("MERGE (a:Person {userName:$uname})  SET a.groupsList=$groupname",uname=member_name,groupname=group_name)
        session.run("MATCH (a:Person),(b:Group) WHERE a.userName = $uname AND b.groupName = $groupname CREATE (a)-[r:member_of]->(b)",uname=member_name,groupname=group_name)

    def show_joined_group(self,member_name):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        result=session.run("MATCH (a:Person {userName:$mname}) return a.groupsList",mname=member_name)
        print(result.single())

    def create_chat_message(self,chatmessage,grpname):
        session=Database.create_session('')
        session.run("Create (c:Chat {chatGroupName:$cgname,message:$msg})",msg=chatmessage,cgname=grpname)

    def post_chat_msg(self,msg,chatgrp):
        session=Database.create_session('')
        session.run("MATCH (a:Chat {chatGroupName:$cgname}) SET a.message:$msg", cgname=chatgrp,msg=msg)
        # session.rum()


    def show_chat_messages(self,grpname):
        # graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        # g = graph.begin()
        session=Database.create_session('')
        result=session.run("MATCH (a:Chat {chatGroupName:$grp}) return a.message",grp=grpname)
        print(result.single())
        # return result

    def show_chat_group(self):
        # graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"))
        # session=graphdb.session()
        session=Database.create_session('')
        result=session.run("MATCH (a:Chat) return a")
        print(result.single())
    



# a=Database()
# a.create_person_node('b','b','b','b','b')
# a.create_person_node('c','c','c','c','c')
# a.create_person_node('a','a','a','a','a')
# a.get_person_node_details('p')
# a.add_post_to_person_node('p','hihihi')
# a.get_person_node_details('p')
# a.get_post_from_person_node_details('p')
# a.add_friends_to_person_node('b','c')
# a.add_friends_to_person_node('c','a')
# a.add_friends_to_person_node('a','b')
# a.get_person_node_details('a')
# a.get_person_node_details('b')
# a.get_person_node_details('c')

# a.get_friends_list_from_person_node_details('a')
# a.get_friends_list_from_person_node_details('b')
# a.get_friends_list_from_person_node_details('c')

# a.add_post_to_person_node('b','Hello this is b')
# a.add_post_to_person_node('a','hello this is a')
# a.add_post_to_person_node('a','this is my 2nd post')

# a.get_friends_post('a')

# a.get_post_from_person_node_details('a')

# a.create_group_node('group1','','a')
# a.create_group_node('group2','','a')

# a.get_groups()

# a.get_person()

# a.add_post_to_group('group1','hello','a')
# a.add_post_to_group('group1','hi','a')
# a.add_post_to_group('group1','3rd post','a')

# a.get_post_from_group('group1')

# a.leave_group('group1','a')

# a.search_person_by_first_name('a')

# a.join_group('group2','b')

# a.show_joined_group('b')