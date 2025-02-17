# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
class Note:

    HIGH= "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str, datetime: str):
        self.code:str = code
        self.title:str = title
        self.text:str = text
        self.importance:str = importance
        self.creation_date:str = datetime.now()
        self.tags = []

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"date: {self.creation_date}\n{self.title}: {self.text}"

class Notebook: h

