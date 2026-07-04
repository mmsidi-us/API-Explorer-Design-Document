import requests

# Set base domain constants for clean target URI structures
JSONPLACEHOLDER_BASE = "https://jsonplaceholder.typicode.com"
POKEAPI_BASE = "https://pokeapi.co/api/v2"
OPENMETEO_BASE = "https://api.open-meteo.com/v1"

def print_separator():
    print("\n" + "=" * 60 + "\n")

def print_metric(method, uri, resp):
    """Helper formatting block to enforce clean presentation layers instead of dumps."""
    print(f"HTTP Method : {method}")
    print(f"URI Target  : {uri}")
    print(f"Status Code : {resp.status_code} {resp.reason}")
    print(f"Content-Type: {resp.headers.get('Content-Type', 'N/A')}")

# ---------------------------------------------------------------------
# CALL 1: GET a Collection
# REST Concept: Target points to a plural resource collection to read plural states.
# ---------------------------------------------------------------------
def run_collection_get():
    print("[Call 1: GET Collection]")
    uri = f"{JSONPLACEHOLDER_BASE}/users"
    try:
        r = requests.get(uri, timeout=10)
        r.raise_for_status()
        print_metric("GET", uri, r)
        
        data = r.json()
        print(f"Parsed Summary: Retrieved {len(data)} user entities.")
        print(f"Sample Records: {[{'id': u['id'], 'name': u['name']} for u in data[:2]]}")
    except requests.exceptions.RequestException as error:
        print(f"Network error intercepted: {error}")

# ---------------------------------------------------------------------
# CALL 2: GET a Specific Resource
# REST Concept: Target references an individual resource entity using a unique key identifier.
# ---------------------------------------------------------------------
def run_specific_get():
    print("[Call 2: GET Specific Resource]")
    uri = f"{POKEAPI_BASE}/pokemon/charizard"
    try:
        r = requests.get(uri, timeout=10)
        r.raise_for_status()
        print_metric("GET", uri, r)
        
        data = r.json()
        print(f"Parsed Summary: Name: {data['name']} | National ID: {data['id']} | Base XP: {data['base_experience']}")
    except requests.exceptions.RequestException as error:
        print(f"Network error intercepted: {error}")

# ---------------------------------------------------------------------
# CALL 3: GET with Query Parameters
# REST Concept: Modifies collection state visibility or acts as filters without modifying base route layouts.
# ---------------------------------------------------------------------
def run_query_params_get():
    print("[Call 3: GET with Query Parameters]")
    uri = f"{OPENMETEO_BASE}/forecast"
    query_payload = {"latitude": 38.0401, "longitude": -84.5003, "current_weather": "true"}
    try:
        r = requests.get(uri, params=query_payload, timeout=10)
        r.raise_for_status()
        print_metric("GET", r.url, r)
        
        data = r.json()
        weather = data.get("current_weather", {})
        print(f"Parsed Summary: Location Coord: {data.get('latitude')}, {data.get('longitude')}")
        print(f"Metrics Read  : Temp: {weather.get('temperature')}°C | Wind: {weather.get('windspeed')} km/h")
    except requests.exceptions.RequestException as error:
        print(f"Network error intercepted: {error}")

# ---------------------------------------------------------------------
# CALL 4: Request to a Nested Resource
# REST Concept: Sub-resources path patterns represent clear, hierarchical relational ownership maps.
# ---------------------------------------------------------------------
def run_nested_get():
    print("[Call 4: GET Nested Resource]")
    uri = f"{JSONPLACEHOLDER_BASE}/users/2/posts"
    try:
        r = requests.get(uri, timeout=10)
        r.raise_for_status()
        print_metric("GET", uri, r)
        
        data = r.json()
        print(f"Parsed Summary: Discovered {len(data)} sub-resource post items owned by User ID 2.")
        if data:
            print(f"First Entry   : Title -> '{data[0].get('title')}'")
    except requests.exceptions.RequestException as error:
        print(f"Network error intercepted: {error}")

# ---------------------------------------------------------------------
# CALL 5: POST to Create a Resource
# REST Concept: State changes use entity payload submissions. Status 201 validates explicit generation.
# ---------------------------------------------------------------------
def run_state_creation_post():
    print("[Call 5: POST State Creation]")
    uri = f"{JSONPLACEHOLDER_BASE}/posts"
    new_entity = {"title": "REST Design Fundamentals", "body": "Clean architectural design decouples implementations.", "userId": 2}
    try:
        r = requests.post(uri, json=new_entity, timeout=10)
        r.raise_for_status()
        print_metric("POST", uri, r)
        
        data = r.json()
        print(f"Parsed Summary: Mock engine returned status and tracked a persistent placeholder item ID: {data.get('id')}")
    except requests.exceptions.RequestException as error:
        print(f"Network error intercepted: {error}")

# ---------------------------------------------------------------------
# ERROR HANDLING SHOWCASE
# Demonstrates robust containment blocking execution crashes on bad endpoints.
# ---------------------------------------------------------------------
def run_graceful_error_test():
    print("[Showcase: Safe Error Handling Context]")
    uri = f"{JSONPLACEHOLDER_BASE}/missing-route-exception-test"
    try:
        r = requests.get(uri, timeout=10)
        r.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print_metric("GET", uri, error.response)
        print(f"Safe Handler Conclusion: Intercepted clean error tracking without script crashes.")

if __name__ == "__main__":
    print("Initiating Master API Engine Diagnostics...")
    print_separator()
    run_collection_get()
    print_separator()
    run_specific_get()
    print_separator()
    run_query_params_get()
    print_separator()
    run_nested_get()
    print_separator()
    run_state_creation_post()
    print_separator()
    run_graceful_error_test()
    print_separator()
    print("Diagnostics complete. Workspace secure.")