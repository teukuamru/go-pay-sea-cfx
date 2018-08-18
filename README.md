## Account API List

* [Create Account](#create-account)
* [Get Account Details](#get-account-details)
* [Login](#login)

## Balance API List

* [Create Balance](#create-balance)
* [Get Balance Details](#get-balance-details)

## Transaction API List

* [Create Transaction](#create-transaction)
* [Get Transaction Details](#get-transaction-details)
* [Finish Transaction](#finish-transaction)
* [Cancel Transaction](#cancel-transaction)
* [List Transactions By Username](#list-transactions-by-username)
* [Top Up Balance](#top-up-balance)


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

Example Response Body:

```json
{
    "key": "e4a218f4ea58b269762981694844521889d545c7"
}
```

## Get Account Details
URL: GET - `https://go-pay-sea-cfx.herokuapp.com/api/accounts/<username>/`

Example: https://go-pay-sea-cfx.herokuapp.com/api/accounts/compfest/

Example Response Body:

```json
{
    "id": 2,
    "username": "compfest"
}
```


## Login
URL: POST - `https://go-pay-sea-cfx.herokuapp.com/api/rest-auth/login/`

Example Request Body:

```json
{
    "username": "compfest",
    "password": "admin12345"
}
```

Example Response Body:

```json
{
    "key": "e4a218f4ea58b269762981694844521889d545c7"
}
```

## Create Balance
URL: POST - `https://go-pay-sea-cfx.herokuapp.com/api/accounts/<username>/balance/create/`

Example: https://go-pay-sea-cfx.herokuapp.com/api/accounts/compfest/balance/create/

__NO REQUEST BODY__

Example Response Body:

```json
{
    "id": 1,
    "go_pay_balance": 0,
    "user": "compfest"
}
```

## Get Balance Details
URL: GET - `https://go-pay-sea-cfx.herokuapp.com/api/accounts/<username>/balance/`

Example: https://go-pay-sea-cfx.herokuapp.com/api/accounts/compfest/balance/

Example Response Body:

```json
{
    "id": 1,
    "go_pay_balance": 0,
    "user": "compfest"
}
```

## Create Transaction
URL: POST - `https://go-pay-sea-cfx.herokuapp.com/api/transactions/`

Example Request Body:

```json
{
    "user": "compfest",
    "changed_balance": -10000,
    "description": "jalan jalan"
}
```

Example Response Body:

```json
{
    "id": 1,
    "changed_balance": -10000,
    "description": "jalan jalan",
    "finished": false,
    "user": "compfest"
}
```


## Get Transaction Details
URL: GET - `https://go-pay-sea-cfx.herokuapp.com/api/transactions/<transaction_id>/`

Example: https://go-pay-sea-cfx.herokuapp.com/api/transactions/1/

Example Response Body:

```json
{
    "id": 1,
    "changed_balance": 100000,
    "description": "top up",
    "finished": false,
    "user": "compfest"
}
```


## Finish Transaction
URL: PUT - `https://go-pay-sea-cfx.herokuapp.com/api/transactions/<transaction_id>/`

Example: https://go-pay-sea-cfx.herokuapp.com/api/transactions/1/

Example Request Body:

```json
{
    "finished": true
}
```

Example Response Body:

```json
{
    "id": 1,
    "changed_balance": -10000,
    "description": "jalan jalan",
    "finished": true,
    "user": "compfest"
}
```


## Cancel Transaction
URL: DELETE - `https://go-pay-sea-cfx.herokuapp.com/api/transactions/<transaction_id>/`

Example: https://go-pay-sea-cfx.herokuapp.com/api/transactions/1/

__RETURN HTTP 204 No Content__


## List Transactions By Username
URL: GET - `https://go-pay-sea-cfx.herokuapp.com/api/transactions/all/<username>/`

Example: https://go-pay-sea-cfx.herokuapp.com/api/transactions/all/compfest/

Example Response Body:

```json
[
    {
        "id": 2,
        "user": "compfest",
        "changed_balance": 20000,
        "description": "top up"
    },
    {
        "id": 1,
        "user": "compfest",
        "changed_balance": -10000,
        "description": "jalan jalan"
    }
]
```


## Top Up Balance
URL: POST - `https://go-pay-sea-cfx.herokuapp.com/api/transactions/top-up/<username>/`

Example: https://go-pay-sea-cfx.herokuapp.com/api/transactions/top-up/compfest/

Example Request Body:

```json
{
    "changed_balance": 10000,
    "description": "top up boy"
}
```

Example Response Body:

```json
{
    "id": 3,
    "changed_balance": 10000,
    "description": "top up boy",
    "finished": true,
    "user": "compfest"
}
```