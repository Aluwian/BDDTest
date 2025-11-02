import requests


class SendRequest:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"

    def get_response(self, method, endpoint, json_data=None, params=None):
        url = f'{self.base_url}/{endpoint}'
        data = []
        response = requests.request(method, url, json=json_data, params=params)
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            data = None
        return data, response.status_code

    def create_note(self, note_data):
        """Создание одной заметки"""
        return self.get_response("post", "notes", json_data=note_data)

    def get_note_by_id(self, note_id):
        """Получение заметки по id"""
        return self.get_response("get", f"notes/{note_id}")

    def get_all_notes(self):
        """Получение всех заметок"""
        return self.get_response("get", "notes")

    def update_note(self, note_id, updates):
        """Обновление заметки"""
        return self.get_response("put", f"notes/{note_id}", json_data=updates)

    def delete_note(self, note_id):
        """Удаление заметки"""
        return self.get_response("delete", f"notes/{note_id}")
