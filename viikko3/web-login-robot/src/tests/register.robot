*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register with Valid Username And Password
    Set Username  thuckey
    Set Password  salainen1234
    Set Password Confirmation  salainen1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  th
    Set Password  salainen1234
    Set Password Confirmation  salainen1234
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  thuckeyyy
    Set Password  salain
    Set Password Confirmation  salain
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long.

Register With Nonmatching Password And Password Confirmation
    Set Username  thuckeyy
    Set Password  salainen123
    Set Password Confirmation  salainen1234
    Submit Credentials 
    Register Should Fail With Message  Password and password confirmation do not match

*** Keywords ***
Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}