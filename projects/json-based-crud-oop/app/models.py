from dataclasses import dataclass, asdict
from uuid import UUID

class Model:
    def dict(self):
        return asdict(self)
    

@dataclass
class User(Model):
    uid: UUID # уникальный идентификатор
    username: str
    age: int
    email: str


