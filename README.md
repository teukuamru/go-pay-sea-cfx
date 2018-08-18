## Account API List

* [Create Account](#create-account)
* [Get Account Details](#get-account-details)

## Balance API List

* [Create Balance](#create-balance)
* [Get Balance Details](#get-balance-details)

## Transaction API List

## Create Account
URL: POST - `https://go-pay-sea-cfx.herokuapp.com/api/rest-auth/registration/`

Example Request Body:

```json
{
    "username": "compfestx",
    "password1": "admin12345",
    "password2": "admin12345"
}
```

Response Body:

```json
{
    "key": "e4a218f4ea58b269762981694844521889d545c7"
}
```

## Get Account Details
URL: GET - `https://go-pay-sea-cfx.herokuapp.com/api/accounts/<username>`

Example: https://go-pay-sea-cfx.herokuapp.com/api/accounts/compfest

Response Body:

```json
{
    "id": 2,
    "username": "compfest"
}
```
