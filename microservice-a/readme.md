Search Bar Microservice
Overview
This microservice provides a search bar functionality that allows users to query a predefined dataset and receive results in JSON format. The dataset is hardcoded, and the service is designed to be simple, lightweight, and easy to integrate.

Communication Contract
This document serves as the communication contract between the microservice and its users. Once defined, this contract should not change to ensure smooth integration.

How to Request Data
Endpoint
GET /search

Query Parameters
query (required): A string that represents the search term.

Example HTTP Request:
curl "http://127.0.0.1:5000/search?query=ap"

Example Python Request:
import requests

response = requests.get("http://127.0.0.1:5000/search?query=ap")
print(response.json())

How to Receive Data
The microservice responds with a JSON array containing objects for all matching items. Each object has the following structure:

id: A unique identifier for the item.
name: The name of the item.
Example JSON Response
If the query is ap, the response will look like this:
[
    {
        "id": 1,
        "name": "Apple"
    }
]


If no matches are found:
[]

UML Sequence Diagram
The UML sequence diagram below illustrates how data flows between the client and the microservice:

The Client Program sends an HTTP GET request with the search term to the /search endpoint.
The Microservice processes the request, filters the dataset, and prepares the response.
The Microservice sends the JSON response back to the Client Program.

![Microservice A](Sequence.png)

Important Notes for Integration
Access the Microservice:

Clone the repository:
git clone <repository_url>

Navigate to the project directory and start the server:
python main.py
The microservice will run locally at http://127.0.0.1:5000.

Key Details:
Use the /search endpoint for all requests.
Ensure the query parameter is correctly formatted.

Assistance:
If issues arise, contact [your contact information].
I am available Monday–Friday, 10 AM–6 PM.
Please report any issues by [specific date].

