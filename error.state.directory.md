# Error State Directory

This matrix details how the server handles edge cases, data boundaries, and security violations on your most critical nested interaction endpoint: `POST /recipes/{id}/ratings`.

| Status HTTP Code | Literal Context Meaning | Exact System Trigger Mechanism |
| :--- | :--- | :--- |
| **`400 Bad Request`** | Data Parsing Failure | The client passed an invalid score type, or passed a score integer outside the restricted 1 to 5 boundary scale limits. |
| **`401 Unauthorized`**| Identity Check Absent | The request header missed its token entirely or passed an expired token signature block. |
| **`403 Forbidden`** | System Access Refused | An authenticated user tried to post a rating on their own authored recipe entry (prohibits ballot self-padding). |
| **`404 Not Found`** | Resource Missing Match | The structural lookup path matching `/recipes/99999` points to a non-existent recipe ID in the index database. |
| **`409 Conflict`** | Storage State Collision| The client identity record has already logged an assessment rating tracking row inside this recipe's index (prevents duplicate voting). |
| **`500 Internal Error`**| Infrastructure Failure | The primary database engines went offline or encountered severe deadlocks while running structural write operations. |
