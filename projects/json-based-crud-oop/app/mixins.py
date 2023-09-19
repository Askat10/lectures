import uuid

class ReadMixin:
    def read(self):
        print(self.read_db())

class CreateMixin:
    def create(self):
        data = self.read_db()
        username = input('enter username please: ')
        age = int(input('enter age pls: '))
        email = input('enter your email: ')
        uid = str(uuid.uuid4())[:8]
        model = self.model(uid, username, age, email)
        data.append(model.dict())
        self.write_to_db(data)
        return model

class UpdateMixin:
    def update(self):
        data = self.read_db()
        uid = input('input uid: ')
        user = self.get_object(uid)
        if user:
            data.remove(user)
            new_username = input('input name: ') or user['username']
            new_age = input('input age') or user['age']
            new_email = input('input new mail') or user['email']
            uid = user['uuid']

            model = self.model(uid, new_username, new_age, new_email)
            data.append(model.dict())
            self.write_to_db(data)       
        else:
            print('нет такого челика')    

class DeleteMixin:
    def delete(self):
        data = self.read_db()
        uid = input('enter your id: ')
        for i in data:
            if uid == i['uid']:
                data.pop(data.index(i))
                self.write_to_db(data)
                break  
        else:
            print('нет такого челика')
class DetailMixin:
    def retrieve(self):
        uid = input('enter the id: ')
        user = self.get_object(uid)
        if user:
            print(user)
        else:
            print('Нет такого челика')

