Feature: Update a note by id
    Scenario: Update a note by valid id
        Given I have valid id
        When I send a request to update a note
        Then the response status code should be 200
        And the response should contain the correct content
    Scenario: Update a note by invalid id
        Given I have incorrect id
        When I send a request to update a note
        Then the response status code should be 422