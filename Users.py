class User(object):
    all_users = {}

    def __init__(self):
        username = None  # pk
        password = None

    def add_user(self, username, password):
        if username and password:

            self.all_users[username] = {
                    "user_name": username,
                    "password": password
                }
            print(self.all_users)

            return {
                'message': 'user added successfully',
                'status': 'success'
            }
        return {
            'message': 'Invalid username or password',
            'status': 'error'
        }

    def deleteuser(self, username):
        if username in self.all_users.keys():
            del self.all_users[username]

            print(self.all_users)

            return {
                'message': 'Deleted successfully',
                'status': 'success'
            }
        return {
            'message': 'User could not be deleted',
            'status': 'error'
        }

    def get_all_users(self):
        return self.all_users

    def change_password(self, username, current_password, new_password):
        if username in self.all_users.keys():
            if self.all_users[username]['password'] == current_password:
                self.all_users[username]['password'] = new_password
                return {
                    'message': 'Password changed successfully',
                    'status': 'success'
                }
            return {
                'message': 'Password not changed',
                'status': 'error'
            }

    def login(self, username, password):
        if username and password in self.all_users:

            self.all_users = {
                "user_name": username,
                "password": password
            }
            print(username)

            return {
                'message': 'Login successful',
                'status': 'success'
            }
        return {
            'message': 'Incorrect password or username'
        }


new_user = User()
print(new_user.add_user('Joy', 'joyy'))
print(new_user.login('Joy', 'joyy'))
# print(new_user.login('Me', 'hueh'))
