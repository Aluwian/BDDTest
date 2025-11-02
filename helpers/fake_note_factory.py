import factory


class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def to_dict(self):
        data = {}
        if self.title is not None and self.content is not None:
            data = {"title": self.title, "content": self.content}
            return data
        return None


class NoteFactory(factory.Factory):
    class Meta:
        model = Note

    title = factory.Faker('sentence', nb_words=4)
    content = factory.Faker('sentence', nb_words=30)
