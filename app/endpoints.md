# Endpoints

This file sets out the various endpoints of the Backend, the required Data and the expected Results. This file should be as detailed as possible to ensure smooth communication between the front and back ends.

## General Note

The backend requires the use of CSRF tokens to ensure security. Requests made to the back end will have to carry the following items:

| Item   | Value                 | Request Type      |
|--------|-----------------------|-------------------|
| Header | "x-csrftoken"         | Any               |
| Cookie | "csrftoken"           | Any               |
| Token  | string                | All Authenticated |
| Input  | "csrfmiddlewaretoken" | POST              |

---

<!-- markdownlint-disable-file MD024 -->

## Auth: _/auth_

### Login: _/login/_ (POST)

This URL is concerned with the logging in of users through email.

#### Request

| Value    | Type   |
|----------|--------|
| email    | string |
| password | string |

#### Response

Success: 200
Value | Type
------|-------
key   | string

Failure: 400
Value            | Type
-----------------|-------------
non_field_errors | list[string]

### Logout: _/logout/_ (POST)

This URL is concerned with the logging out of users.

#### Request

Empty Request Body

#### Response

Success: 200
Value  | Type
-------|-------
detail | string

Failure: 403
Value  | Type
-------|-------
detail | string

### Password Reset: _/password/reset/_ (POST)

This URL is concerned with password resetting when a user has forgotten their password.

#### Request

| Value | Type   |
|-------|--------|
| email | string |

#### Response

Success: 200
Value  | Type
-------|-------
detail | string

### Password Change: _/password/change/_ (POST)

This URL is concerned with updating the user password.

#### Request

_Note_: uid and Token are sent in email

| Value         | Type   |
|---------------|--------|
| new_password1 | string |
| new_password2 | string |
| old_password  | string |

#### Response

Success: 200
Value  | Type
-------|-------
detail | string

### User: _/user/_ (GET/PUT/PATCH)

This URL is concerned with updating the user password.

#### Request

_Note_: User needs to be logged in

| Value      | Type   | Optional |
|------------|--------|----------|
| username   | string | ✅        |
| first_name | string | ✅        |
| last_name  | string | ✅        |

#### Response

_Note_: pk is the primary key, aka the id of the user in the database.

Success: 200
Value      | Type
-----------|-------
pk         | int
email      | string
first_name | string
last_name  | string

### User Registration: _/registration/_ (POST)

This URL is concerned with signing up a user.

#### Request

| Value     | Type   |
|-----------|--------|
| email     | string |
| password1 | string |
| password2 | string |

#### Response

Success: 200
Value  | Type
-------|-------
detail | string

Failure: 400
Value            | Type
-----------------|-------------
email            | list[string]
password1        | list[string]
password2        | list[string]
non_field_errors | list[string]

### User Email Verification: _/registration/verify-email_ (POST)

This URL is concerned with verifying a user.

#### Request

| Value | Type   |
|-------|--------|
| key   | string |

#### Response

Success: 200
Value  | Type
-------|-------
detail | string

Failure: 404
Value  | Type
-------|-------
detail | string

### Resend User Email Verification: _/registration/resend-email_ (POST)

This URL is concerned with resending the verification email to the user.

#### Request

| Value | Type   |
|-------|--------|
| email | string |

#### Response

Success: 200
Value  | Type
-------|-------
detail | string

### Google Authentication: _/google/_ (POST)

This URL is concerned with verifying the user access code with Google.

#### Request

| Value | Type   |
|-------|--------|
| code  | string |

#### Response

Success: 200
Value | Type
------|-------
key   | string

---

## API: _/api_

Enter your custom API here
