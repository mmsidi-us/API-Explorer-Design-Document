4. Authentication & Authorization Mapping Matrix
Strategic Security Mechanism
The architecture runs via JWT (JSON Web Tokens) passed across target header layouts using standard notation formatting: Authorization: Bearer <JWT_STRING>.

Route Authorization Clearances
Public Open Targets (No Auth Check Validation Required):

POST /users (Account generation)

GET /recipes & GET /recipes/{id} (Recipe inspection views)

GET /recipes/{id}/ratings (Review audit inspection)

Authenticated System Targets (Valid JWT Authentication Required):

POST /recipes (Any valid user account can author a cooking listing)

POST /recipes/{id}/ratings (Any valid user account can rate alternative recipes)

Granular Object-Level Verification Validation Handlers:

PUT/PATCH/DELETE transformations pointing directly to /recipes/{id} check if the requesting identity ID matches the internal database value stored under author_id. Non-matching clients fail with permission warnings.

PATCH/DELETE transformations pointing directly to /ratings/{id} allow mutations exclusively if the current token matches the reviewer_user_id.