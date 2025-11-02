Feature: Create a note
    Scenario: Successfully create a note
        Given the note payload with title and content
        When I send a request to create the note
        Then the response status code should be 200 for create
        And the response should contain the correct title

  Scenario: Fail to create a note
        Given the note payload without a title and content
        When I send a request to create the note
        Then the response status code should be 422
