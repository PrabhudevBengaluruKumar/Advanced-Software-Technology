import Facebook
import Person
import Group

def create_test_data():

    facebook1 = Facebook.Facebook()
    #create users
    user1 = Person.Person("Patil","Gowda","patil gowda","patil","01/02/1997","","")
    user2 = Person.Person("Rahul","Mogur","rahul mogur","rahul","03/04/1997","","")
    user3 = Person.Person("Prashanth","Sharma","prashanth sharma","prashanth","05/06/1997","","")

    #create groups
    group1 = Group.Group("Friends","","")
    group2 = Group.Group("sports group","","")

    #add user and group objects to facebook class
    facebook1.userList.append(user1)
    facebook1.userList.append(user2)
    facebook1.userList.append(user3)
    facebook1.groupList.append(group1)
    facebook1.groupList.append(group2)

    #add friends
    user1.add_friends(user2.get_username())
    user2.add_friends(user3.get_username())
    user3.add_friends(user1.get_username())

    #join groups
    group1.add_group_members(user3.get_username())
    group1.add_group_members(user1.get_username())
    group1.add_group_members(user2.get_username())
    group1.add_group_members(user2.get_username())
    group2.add_group_members(user1.get_username())

    #add user posts
    user1.add_post("hello friends")
    user2.add_post("hello guys")
    user3.add_post("Good day")

    #add group posts
    group1.add_post(user2.get_username,"Good night guys..")
    group1.add_post(user3.get_username,"Bye...")
    group2.add_post(user1.get_username,"this is sports group")

