from helpers.fake_note_factory import *
from helpers.send_request import SendRequest


class NoteManager:
    def __init__(self):
        self.client = SendRequest()

    def create_and_send_notes(self, count=10):
        """Создает заметки и отправляет их на сервер"""
        created_notes = []
        notes = NoteFactory.build_batch(count)

        for note in notes:
            note_data = {"title": note.title, "content": note.content}
            response_data, status_code = self.client.create_note(note_data)
            if status_code in [200, 201]:
                created_notes.append(response_data)
        return created_notes

    def delete_all_notes(self):
        notes, status_code = self.client.get_all_notes()
        if notes is not None:
            for note in notes:
                note_id = note.get("id")
                self.client.delete_note(note_id)
            return True
        return False

    def get_note_id(self):
        ids = []
        notes, status_code = self.client.get_all_notes()
        if notes is not None:
            for note in notes:
                ids.append(note.get("id"))
            return ids[0]
        return None
