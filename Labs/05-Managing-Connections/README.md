# Managing Connections
- Airflow needs to know how to connect to your environment. Information such as hostname, port, login and passwords to other systems and services is handled in the Admin->Connections section of the UI. The pipeline code you will author will reference the 'conn_id' of the Connection objects.

- Connections can be created and managed using either the UI or environment variables.

## Creating a Connection with the UI
- Open the Admin->Connections section of the UI. Click the Create link to create a new connection.
  - Fill in the Connection Id field with the desired connection ID. It is recommended that you use lower-case characters and separate words with underscores.
  - Choose the connection type with the Connection Type field.
  - Fill in the remaining fields. See Encoding arbitrary JSON for a description of the fields belonging to the different connection types.
  - Click the Save button to create the connection


## Editing a Connection with the UI
- Open the Admin->Connections section of the UI. Click the pencil icon next to the connection you wish to edit in the connection list.
- Modify the connection properties and click the Save button to save your changes

