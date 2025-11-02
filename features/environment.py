from helpers.note_manager import NoteManager


def after_scenario(context, scenario):
    """
    Выполняется после каждого сценария.
    Удаляет все заметки для очистки базы данных.
    """
    manager = NoteManager()
    manager.delete_all_notes()
    print(f"\n[CLEANUP] Все заметки удалены после сценария: {scenario.name}")
