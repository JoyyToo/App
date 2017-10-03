class ShoppingList(object):
    sl = {}

    def __init__(self):
        name = None  # pk
        description = None
        username = None  # fk

    def create_list(self, name, description):
        if name and description:
            self.sl[name] = {
                'name': name,
                'desc': description
            }
            print(self.sl)

            return {
                'message': "List successfully created",
                'status': "success"
            }
        return {
            'message': "Provide all details ",
            'status': "error"
        }

    def view_list(self):
            return self.sl

    def update_list(self, name, curr_desc, new_desc):
        if name in self.sl.keys():
            if self.sl[name]['desc'] == curr_desc:
                self.sl[name]['desc'] = new_desc

            print(self.sl)

            return {
                'message': 'List successfully updated',
                'status': 'success'
            }
        return {
            'message': 'List Unavailable',
            'status': 'error'
        }

    def delete_list(self, name):
        if name in self.sl.keys():
            del self.sl[name]

            print(self.sl)

            return {
                'message': 'List successfully deleted',
                'status': 'success'
            }
        return {
            'message': 'List unavailable',
            'status': 'error'
        }


new_list = ShoppingList()
print(new_list.create_list('List one', 'Dinner for xmas'))
print(new_list.create_list('List two', 'visitors in town'))
print(new_list.view_list())
# print(new_list.update_list('List one', 'Dinner for xmas', 'Xmass dinner'))
# print(new_list.delete_list('List one'))
