# Login and Register API with django-rest framework using JWT

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Usage](#usage)


## General info
REST API - provide login, register, reset-password functionalities.

## Technologies
* Django version: 4.1.2
* django-restframework: 3.14.0
* djangorestframework-simplejwt==5.2.1
* django-cors-headers==3.13.0
You can see all technologies in the **requirements.txt**

## Usage

### register
`POST ` ```/api/register```
Request body
The request body should be a ```"application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```email ``` |
| ```user_name ``` |
| ```password ``` |

### send-otp
`POST` ```/api/send-otp```
Request body
The request body should be a ```"application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```email ``` |

### verify-email
`POST` ```/api/verify-otp```
Request Body
The request body should be a ```"application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```email ``` |
| ```otp ``` |

### login
`POST` ```/api/login```
Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.
Request body
The request body should be a ```"application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```email ``` |
| ```password``` |

### logout
`POST` ```/api/logout/```
Takes a token and blacklists it. Must be used with the `rest_framework_simplejwt.token_blacklist` app installed.
Request body
The request body should be a ```"application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```refresh  ``` |

### refresh > token
`POST` ```/api/token/refresh/```
Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.
Request Body
The request body should be a ```"application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```refresh ``` |

### reset-password
`POST` ```/api/reset-password/```
Request Body
The request body should be a ```"application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```email  ``` |
| ```otp ``` |
| ```password ``` |
| ```password_confirm ``` |

## Setup
To run this project in your local you need to execute below commands
First download project to your computer.
```
$ git clone
```
Then create virtual environment and activate it
```
$ py venv env
$ env\Scripts\activate
```
Using requirements.txt file download dependencies
```
$ pip install -r requirements.txt
```
Using below command run the application
```
$ py manage.py runserver
```
