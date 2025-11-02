from behave import given, when, then
from helpers.note_manager import NoteManager
from helpers.send_request import SendRequest


@given('I have a valid id')
def step_get_correct_id(context):
    manager = NoteManager()
    manager.create_and_send_notes()
    context.note_id = manager.get_note_id()


@given('I have an invalid id')
def step_get_invalid_id(context):
    context.note_id = 1000000


@when("I send a request to get a note")
def step_send_request_by_id(context):
    client = SendRequest()
    context.data, context.status_code = client.get_note_by_id(context.note_id)


@then("I should receive the note")
def step_should_receive_note(context):
    assert context.data is not None


@then("status code should be 200")
def step_should_be_200_by_get_note(context):
    assert context.status_code == 200


@then("status code should be 404")
def step_should_be_404_by_get_note(context):
    assert context.status_code == 404
