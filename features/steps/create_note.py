from behave import given, when, then
from helpers.fake_note_factory import NoteFactory
from helpers.send_request import SendRequest


@given('the note payload with title and content')
def step_get_note(context):
    note = NoteFactory()
    context.note = {"title": note.title, "content": note.content}

@given("the note payload without a title and content")
def step_get_empty_note(context):
    context.note = {}

@when("I send a request to create the note")
def step_send_post_request(context):
    client = SendRequest()
    response_data, status_code = client.create_note(context.note)
    context.response_data = response_data
    context.status_code = status_code

@then("the response status code should be 200 for create")
def step_check_response_status_code_200(context):
    assert context.status_code == 200

@then("the response status code should be 422")
def step_check_response_status_code_422(context):
    assert context.status_code == 422

@then("the response should contain the correct title")
def step_check_response_title(context):
    assert context.response_data["title"] == context.note["title"]
