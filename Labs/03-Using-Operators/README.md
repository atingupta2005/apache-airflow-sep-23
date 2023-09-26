# Using Operators
- An operator represents a single, ideally idempotent, task
- Operators determine what actually executes when your DAG runs.



## BashOperator
- To execute commands in a Bash shell.

```
run_this = BashOperator(
    task_id='run_after_loop',
    bash_command='echo 1',
)
```

- Templating
  - You can use Jinja templates to parameterize the bash_command argument.
```
also_run_this = BashOperator(
    task_id='also_run_this',
    bash_command='echo "run_id={{ run_id }} | dag_run={{ dag_run }}"',
)
```

## PythonOperator
- To execute Python callables

```
def print_context(ds, **kwargs):
    """Print the Airflow context and ds variable from the context."""
    pprint(kwargs)
    print(ds)
    return 'Whatever you return gets printed in the logs'

run_this = PythonOperator(
    task_id='print_the_context',
    python_callable=print_context,
)
```

### Passing in arguments
```
def my_sleeping_function(random_base):
    """This is a function that will run within the DAG execution"""
    time.sleep(random_base)

# Generate 5 sleeping tasks, sleeping from 0.0 to 0.4 seconds respectively
for i in range(5):
    task = PythonOperator(
        task_id='sleep_for_' + str(i),
        python_callable=my_sleeping_function,
        op_kwargs={'random_base': float(i) / 10},
    )

    run_this >> task
```


## BranchDayOfWeekOperator
- To branch your workflow based on week day value.

```
dummy_task_1 = DummyOperator(task_id='branch_true', dag=dag)
dummy_task_2 = DummyOperator(task_id='branch_false', dag=dag)

branch = BranchDayOfWeekOperator(
    task_id="make_choice",
    follow_task_ids_if_true="branch_true",
    follow_task_ids_if_false="branch_false",
    week_day="Monday",
)

# Run dummy_task_1 if branch executes on Monday
branch >> [dummy_task_1, dummy_task_2]
```


## Cross-DAG Dependencies
- When two DAGs have dependency relationships, it is worth considering combining them into a single DAG, which is usually simpler to understand
- Airflow also offers better visual representation of dependencies for tasks on the same DAG.
- ExternalTaskSensor can be used to establish such dependencies across different DAGs. When it is used together with ExternalTaskMarker, clearing dependent tasks can also happen across different DAGs.

### ExternalTaskSensor
- To make tasks on a DAG wait for another task on a different DAG for a specific execution_date
- ExternalTaskSensor also provide options to set if the Task on a remote DAG succeeded or failed via allowed_states and failed_states parameters.
```
child_task1 = ExternalTaskSensor(
    task_id="child_task1",
    external_dag_id=parent_dag.dag_id,
    external_task_id=parent_task.task_id,
    timeout=600,
    allowed_states=['success'],
    failed_states=['failed', 'skipped'],
    mode="reschedule",
)
```

