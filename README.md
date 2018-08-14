### Account API List
* List of accounts:
    * GET http://localhost:8000/api/account/
* Create new account:
    * POST http://localhost:8000/api/account/
* Get an account info:
    * GET http://localhost:8000/api/account/10/
* Delete account info:
    * DELETE http://localhost:8000/api/account/10/

### Transaction API List
* List of all transactions:
    * GET http://localhost:8000/api/transaction/
* Create new transaction:
    * POST http://localhost:8000/api/transaction/
* Top up account balance:
    * POST http://localhost:8000/api/transaction/top-up/10
* Get a transaction detail:
    * GET http://localhost:8000/api/transaction/1/
* Finalize transaction info:
    * PUT http://localhost:8000/api/transaction/1/

