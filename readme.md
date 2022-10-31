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
`POST ` ```diff - /api/register```
Request body
The request body should be a ```diff - "application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```diff - email ``` |
| ```diff - user_name ``` |
| ```diff - password ``` |

### send-otp
`POST` ```diff - /api/send-otp```
Request body
The request body should be a ```diff - "application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```diff - email ``` |

### verify-email
`POST` ```diff - /api/verify-otp```
Request Body
The request body should be a ```diff - "application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```diff - email ``` |
| ```diff - otp ``` |

### login
`POST` ```diff - /api/login```
Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.
Request body
The request body should be a ```diff - "application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```diff - email ``` |
| ```diff - password``` |

### logout
`POST` ```diff - /api/logout/```
Takes a token and blacklists it. Must be used with the `rest_framework_simplejwt.token_blacklist` app installed.
Request body
The request body should be a ```diff - "application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```diff - refresh  ``` |

### refresh > token
`POST` ```diff - /api/token/refresh/```
Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.
Request Body
The request body should be a ```diff - "application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```diff - refresh ``` |

### reset-password
`POST` ```diff - /api/reset-password/```
Request Body
The request body should be a ```diff - "application/json" ``` encoded object, containing the following items.
| Parameter |
| --------- |
| ```diff - email  ``` |
| ```diff - otp ``` |
| ```diff - password ``` |
| ```diff - password_confirm ``` |

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

