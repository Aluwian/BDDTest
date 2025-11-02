from behave import given, when, then
from helpers.note_manager import NoteManager
from helpers.send_request import SendRequest


@given("I have a list of notes")
def step_have_list_of_notes(context):
    manager = NoteManager()
    context.created_notes = manager.create_and_send_notes(5)


@given('I have an empty list of notes')
def step_have_empty_list_of_notes(context):
    manager = NoteManager()
    manager.delete_all_notes()


@when('I send a request to get all notes')
def step_send_get_request(context):
    client = SendRequest()
    created_notes, status_code = client.get_all_notes()
    context.created_notes = created_notes
    context.status_code = status_code


@then('I should receive a list of notes')
def step_check_response_list_of_notes(context):
    assert context.created_notes is not None
    assert isinstance(context.created_notes, list)
    assert isinstance(context.created_notes[0], dict)
    assert len(context.created_notes) > 0


@then("the response status code should be 200 for get all notes")
def step_check_response_status_code_200(context):
    assert context.status_code == 200


@then('I should receive an empty list of notes')
def step_check_response_empty_list(context):
    assert context.created_notes == []
