import person
import account

def main():
    print('Welcome !')
    entry=None
    while entry!='5':
        entry = input('\n1. Login...\n2. Register/Sign Up..\n3. Exit. \nPlease, Choose the options 1, 2 or 3: ')
        if entry=='1':
            user_dao = account.account()
            username = input('\nEnter Your username: ')
            pw = input('\nEnter Your password: ')
            if user_dao.validate_user(username, pw):
                user = user_dao.get_user_by_username(username)
                print("hello ",username,"!")
                print('\nWhat Would You Like To Do?')
                rentry='99'
                while rentry!='2':
                    rentry = input('\n 1. Post\n 2. Show Users\n 3. Show posts\n 4. Search users by first name \n 5. Groups\n 6.Logout\n Please, enter 1, 2, 3, 4, 5 or 6 : ')
                    if rentry=='1':
                        post=input("\nEnter the post : ")
                        user_dao.newPost(username,post)
                        
                    elif rentry =='2':
                        # fname = input("\nEnter the name of the user to be searched: ")
                        user_dao.showUsers(username)
                        rentry='1'
                    elif rentry=='3':
                        user_dao.displaypost(username)
                        rentry='1'
                        # break;
                    elif rentry=='4':
                        first_name=input("\nEnter first name to search the users : ")
                        user_dao.searchUsers(first_name)
                    elif rentry=='5':
                        user_dao.showGroups(username)
                    elif rentry=='6':
                        break
                    else:
                        print('\nInvalid Option...')
            else:
                print('\nWrong Credentials!')
        elif entry=='2':
            print("\nEnter the details to register.")
            user_dao = account.account()
            username = input('\nPlease provide your username : ')
            if not user_dao.get_user_by_username(username):
                f_name = input("\nPlease enter your first name : ")
                l_name = input("\nEnter your last name : ")
                password = input("\nPlease enter your password : ")
                dob = input("\nPlease enter your date of birth : ")
                user_dao.add_new_user(f_name, l_name, username, password,dob)
                entry = '-1'
                continue
            else:
                print("\nThat username is already taken, please choose some other username.\n")
        elif entry=='3':
            print("\nLogged Out of the account...,\n ")
            break
        else:
            print('\nInvalid Option...\n')
    print('\nClosing the Program. Goodbye.')
if __name__=='__main__':
    main()