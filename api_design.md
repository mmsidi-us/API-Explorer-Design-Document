# Application Architecture Plan: Recipe Manager API

## Application Description
The Recipe Manager API delivers a backend framework allowing home chefs to store, structure, scale, and evaluate culinary recipes. The system coordinates instructions alongside real-world inventory ingredients, classifies collections via categories, and exposes nested processing structures to submit user reviews and multi-tier star evaluations.

---

## 1. Resources & Relationships

### Tracked Resources
1. **User Resource** (`/users`): Represents system cooks, managing authorization tracking blocks.
2. **Recipe Resource** (`/recipes`): Core entity asset mapping title strings, directions, prep metrics, and array items.
3. **Rating Resource** (`/ratings`): Metric tracking blocks calculating subjective user quality values.

### Structural Entity Relationships
* **User to Recipe (`One-to-Many`)**: One user profile can craft multiple distinct culinary recipe documents; an individual recipe item maps back to exactly one author owner user.
* **Recipe to Rating (`One-to-Many`)**: One recipe item can accumulate thousands of distinct ranking reviews; any individual rating maps natively to exactly one parent recipe.

---

## 2. CRUD Route Architecture List

The interface exposes **13 well-formed endpoints** prioritizing standard REST naming mechanics:

| HTTP Method | URI Path Template | Concrete Action Description |
| :--- | :--- | :--- |
| **POST** | `/users` | Registers a new unique user profile asset into storage. |
| **GET** | `/users/{id}` | Retrieves distinct account properties by explicit profile ID. |
| **GET** | `/recipes` | Fetches a public list of recipes (supports pagination query parameters). |
| **POST** | `/recipes` | Creates and saves a new recipe entity instance. |
| **GET** | `/recipes/{id}` | Collects detailed profile configuration values for a distinct recipe. |
| **PUT** | `/recipes/{id}` | Idempotently replaces an active recipe configuration state with new data. |
| **PATCH** | `/recipes/{id}` | Mutates partial fields of a recipe record (e.g., tweaking prep times). |
| **DELETE** | `/recipes/{id}` | Eliminates a target recipe asset securely from standard records. |
| **GET** | `/recipes/{id}/ratings` | Reads all nested review records compiled under a target parent recipe. |
| **POST** | `/recipes/{id}/ratings`| Constructs a new review record nested directly within a specified recipe. |
| **GET** | `/ratings/{id}` | Safely evaluates a distinct single rating configuration instance. |
| **PATCH** | `/ratings/{id}` | Alters the comment text or rating score values of an existing entry. |
| **DELETE** | `/ratings/{id}` | Erases a rating entity profile out of system memory. |

---

## 3. Data Transfer Schema Layouts

### Schema 1: POST `/recipes` (Client Request Body)
```json
{
  "title": "string (Minimum 3 characters, e.g., 'Skillet Garlic Pork Chops')",
  "prep_time_minutes": "integer (e.g., 15)",
  "cook_time_minutes": "integer (e.g., 20)",
  "ingredients": "array of strings (e.g., ['4 pork chops', '6 cloves garlic', '2tbsp butter'])",
  "instructions": "string (Detailed chronological step descriptions)",
  "is_released_publicly": "boolean (Default true state toggle)"
}
### Schema 2: POST /recipes/{id}/ratings (Client Request Body)
{
  "numerical_score": "integer (Value scale limits restricted from 1 to 5)",
  "review_comment": "string (Optional descriptive text feedback field)"
}

### Schema 3: GET /recipes/{id} (Server Response Representation)
{
  "id": "integer (Unique lookup primary key auto-generated value)",
  "title": "string",
  "prep_time_minutes": "integer",
  "cook_time_minutes": "integer",
  "ingredients": "array of strings",
  "instructions": "string",
  "is_released_publicly": "boolean",
  "author_id": "integer (Foreign relationship key mapping back to creating User)",
  "created_at": "datetime (ISO 8601 representation: '2026-07-04T16:56:00Z')",
  "updated_at": "datetime (ISO 8601 representation: '2026-07-04T16:57:15Z')"
}

### Schema 4: GET /recipes/{id}/ratings (Server Response Representation Array)
[
  {
    "id": "integer (Unique lookup identity track ID)",
    "recipe_id": "integer (Parent tracking relationship constraint)",
    "reviewer_user_id": "integer (Identifies profile entity submitting code feedback)",
    "numerical_score": "integer",
    "review_comment": "string",
    "submitted_at": "datetime (ISO 8601 string)"
  }
]
