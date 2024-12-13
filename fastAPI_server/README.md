# Project Documentation

## Description
This FastAPI-based application displays random jokes in JSON format by fetching data from an external API. 
The application handles requests asynchronously and returns a joke to the user as a JSON object.

## Installation
1. Ensure you have Python version 3.7 or higher installed.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Windows, use `venv\Scripts\activate`
   ```
3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
To run the application, execute the following command:
```bash
uvicorn main:app --reload
```

Once the server is running, it will be accessible at: `http://127.0.0.1:8000/`.

## Usage
The application has one endpoint:
- **`GET /`**: Returns a random joke in JSON format.

Example response:
```json
{
  "type": "general",
  "setup": "What do you call a droid that takes the long way around?",
  "punchline": "R2 detour.",
  "id": 201
}
```

## Example Operation
When accessing the root URL (`/`), the application sends an asynchronous request to the 
external API at `https://official-joke-api.appspot.com/random_joke`. If the request is successful 
(status 200), the application returns a JSON object with the joke. In case of an error,
a JSON message with the error is returned:
```json
{
  "error": "Failed to fetch the joke"
}
```

## Notes
- The application operates in asynchronous mode, allowing for more efficient request handling.
- If there is an issue connecting to the API, the application properly handles the error and returns an appropriate message.

## Contribution
If you have ideas for new mini-applications or improvements to existing ones, you can create a pull request or open an issue in the repository.
