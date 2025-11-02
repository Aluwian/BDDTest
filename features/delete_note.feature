Feature: Delete a note
  Scenario: Successful delete a note by id
    Given I have a note with correct id
    When I send a request to delete the note
    Then the response should be 200

   Scenario: Failed delete a note by id
      Given I have not a note with incorrect id
      When I send a request to delete the note
      Then the response should be 404