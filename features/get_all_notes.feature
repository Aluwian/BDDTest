Feature: Get all notes
  Scenario: Get all creating notes
    Given I have a list of notes
    When I send a request to get all notes
    Then I should receive a list of notes
    And the response status code should be 200 for get all notes

  Scenario: Get all notes with empty list
     Given I have an empty list of notes
     When I send a request to get all notes
     Then I should receive an empty list of notes