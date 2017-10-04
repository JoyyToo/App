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
                'description': description
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

    def update_list(self, description, key_to_find):
        if description:
            for name in self.sl.keys():
                if name == key_to_find:
                    self.sl[name] = {
                        'name': name,
                        'description': description
                    }
                    print(self.sl)

            return {
                'message': 'List successfully updated',
                'status': 'success'
            }
        return {
            'message': 'List Unavailable',
            'status': 'error'
        }

            #     if name in self.sl.keys():
        #         self.sl[name] = {
        #             'name': name,
        #             'description': description
        #         }
        #         print(self.sl)
        #              return {
        #         'message': 'List successfully updated',
        #         'status': 'success'
        #     }
        # return {
        #     'message': 'List Unavailable',
        #     'status': 'error'
        # }

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
# print(new_list.create_list('List two', 'visitors in town'))
print(new_list.update_list('Dinner for xmas', 'List one'))

