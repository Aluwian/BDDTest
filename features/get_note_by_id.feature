Feature: Get note by id
  Scenario: Get note for valid id
    Given I have a valid id
    When I send a request to get a note
    Then I should receive the note
    And status code should be 200

  Scenario: Get note by invalid id
    Given I have an invalid id
    When I send a request to get a note
    Then status code should be 404