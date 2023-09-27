# Make First Conditional Task Using Branching
- How to conditionaly execute tasks
- Refer branch_dag.py
- This DAG is for requesting different APIs in order to geolocate IP addresses
- There is a function - check_api(). It checks the API if that is working. If API return data having the field country, this function returns that
- The returned value is then processed by the BranchPythonOperator in order to execute the corresponding task
  - If the value returned is "ipstack", then the task "ipstack" will be executed and the other tasks will be skipped
- If no API is available, the check_api function returns "none" and so only the task "none" will be executed
- If the tasks corresponding to the APIs are created from the "for loop" as well as the dependencies with the branch task and the store task
