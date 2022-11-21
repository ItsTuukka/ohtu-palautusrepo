*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testimies  testaajansalis123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  thuckey  testaajansalis123
    Output Should Contain  User already exists.

Register With Too Short Username And Valid Password
    Input Credentials  th  testaajansalis123
    Output Should Contain  Username must be at least 3 characters long.

Register With Valid Username And Too Short Password
    Input Credentials  testimies  tes
    Output Should Contain  Password must be at least 8 characters long.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  testimies  testaajansalis
    Output Should Contain  Password must not consist only of symbols from [a-z].

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  thuckey  isojakomee123