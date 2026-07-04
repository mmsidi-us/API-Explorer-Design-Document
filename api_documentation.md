# Public API Exploration Log

## 1. JSONPlaceholder API
* **Base URL**: `https://jsonplaceholder.typicode.com`
* **Authentication Method**: None

### Endpoints Verified
* **GET `/users`**: Collection read capturing list profiles. Returns collection blocks containing structural identifier fields.
* **GET `/users/{id}/posts`**: Hierarchical path filtering targeting relative records. Returns collection metadata objects matching targeted profile keys.
* **POST `/posts`**: Entity payload creation processing. Emits validation acknowledgments matching sent fields.

* **Observed Rate Limits**: Non-throttled public proxy layout.
* **Unexpected Behaviors / Surprises**: State updates (`POST`/`PUT`/`DELETE`) behave realistically, returning successful response tracking objects (e.g., ID `101`), but these updates are completely ephemeral and are not actually persisted on subsequent requests.

## 2. PokeAPI
* **Base URL**: `https://pokeapi.co/api/v2`
* **Authentication Method**: None

### Endpoints Verified
* **GET `/pokemon/{name}`**: Concrete individual record parsing. Yields explicit physical statistics arrays and ability mapping indices.

* **Observed Rate Limits**: Configured limit up to 100 queries tracking across single IP blocks per minute.
* **Unexpected Behaviors / Surprises**: The resource response payload data structure is exceptionally verbose. Retrieving a single item passes an incredibly dense JSON map containing nested URLs pointing to deeper structural assets.

## 3. Open-Meteo API
* **Base URL**: `https://api.open-meteo.com/v1`
* **Authentication Method**: None

### Endpoints Verified
* **GET `/forecast`**: Query-parameter-driven forecast calculation engine requiring dynamic parameters (`latitude`, `longitude`).

* **Observed Rate Limits**: Throttling kicks in once traffic benchmarks exceed 10,000 distinct entries inside single-day windows.
* **Unexpected Behaviors / Surprises**: Omitting critical float parameters triggers an instant error condition instead of falling back to default global coordinates (like `0,0`).