# API-test-task

# Stack
- Python
- FastAPI
- SQLAlchemy 
- Networkx
- Pydantic

## How to start

### Clone the Repository

```
git clone https://github.com/v-bohdan-v/API-test-task.git
```

### Install dependencies

`pip install -r requirements.txt`


### Run project

You can run it from main.py file or using command

`uvicorn src.api:app --reload`

The API will be available on `http://127.0.0.1:8000/docs`

### Database
Run the database locally, for example, PostgreSQL, and create a '.env' file with credentials in the root directory
Example of '.env' file
`
DB_HOST=localhost`<br>`
DB_PORT=7997`<br>`
DB_USER=postgres`<br>`
DB_PASS=test`<br>`
DB_NAME=postgres`<br>`
`


## APIs

Workflow
- get all workflows `GET /workflows/v1/get/all`
- get specific workflow `GET /workflows/v1/get/workflow/{workflow_id}`
- workflow creation `POST workflows/v1/create`
- update workflow `PUT workflows/v1/update/workflow/{w_id}`
- delete workflow `DELETE workflows/v1/delete/workflow/{w_id}`

Nodes
- get all nodes `GET /nodes/v1/all`
- create start or end node `POST /nodes/v1/create/node`
- create message node `POST /nodes/v1/create/node/message`
- create condition node `POST /nodes/v1/create/node/condition`
- links to nodes (add edge to graph) `PUT /nodes/v1/links-node`
- update node `PUT /nodes/v1/update/node`
- delete node `DELETE /nodes/v1//delete/node`
