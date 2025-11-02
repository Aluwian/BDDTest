from behave import given, when, then
from helpers.send_request import SendRequest
from helpers.note_manager import NoteManager


@given('I have valid id')
def step_get_valid_id(context):
    manager = NoteManager()
    manager.create_and_send_notes()
    context.note_id = manager.get_note_id()
    context.updates = {"title": "New_Title",
                       "content": "New_Content"}


@given('I have a note with empty content and valid id')
def step_get_correct_id_empty_content(context):
    manager = NoteManager()
    manager.create_and_send_notes()
    context.note_id = manager.get_note_id()
    context.updates = {"content": ""}


@given('I have incorrect id')
def step_get_incorrect_id(context):
    context.note_id = 1000000000000
    context.updates = {"content": "New content"}


@when('I send a request to update a note')
def step_send_request(context):
    client = SendRequest()
    response_data, status_code = client.update_note(context.note_id, context.updates)
    context.response_data = response_data
    context.status_code = status_code


@then('the response status code should be 200')
def step_check_status_code_200_for_update(context):
    assert context.status_code == 200


@then('the response should contain the correct content')
def step_check_content(context):
    expected_content = context.updates["content"]
    actual_content = context.response_data.get('content')
    assert actual_content == expected_content


@then('the response status code should be 422 for update')
def step_check_status_code_422(context):
    assert context.status_code == 422
