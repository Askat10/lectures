from app.models import User
from app.email_sender import EmailSender
from app.mixins import (CreateMixin, ReadMixin, 
                        UpdateMixin, DeleteMixin, 
                        DetailMixin)
from app.crud import CRUD



class Interface(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin, DetailMixin, CRUD):
    model = User

interface = Interface()
email_sender = EmailSender()
user = interface.create()

email_sender.send_mail(user.email)

# interface.read()
# interface.delete()
# interface.read()
# interface.create()
# interface.create()
# interface.update()
# interface.retrieve()