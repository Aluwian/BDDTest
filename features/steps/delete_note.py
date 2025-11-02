from behave import given, when, then
from helpers.fake_note_factory import NoteFactory
from helpers.send_request import SendRequest
from helpers.note_manager import NoteManager


@given('I have a note with correct id')
def step_get_correct_id_for_delete(context):
    manager = NoteManager()
    manager.create_and_send_notes()
    context.id = manager.get_note_id()

@given('I have not a note with incorrect id')
def step_get_incorrect_id_for_delete(context):
    context.id = 1000000

@when('I send a request to delete the note')
def step_send_post_request(context):
    client = SendRequest()
    context.response_data, context.response_status_code = client.delete_note(context.id)

@then('the response should be 200')
def step_check_response_200_for_delete(context):
    assert context.response_status_code == 200

@then('the response should be 404')
def step_check_response_404_for_delete(context):
    assert context.response_status_code == 404