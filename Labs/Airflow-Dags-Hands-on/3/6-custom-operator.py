from airflow.models.baseoperator import BaseOperator
from pendulum import datetime
from airflow.decorators import dag, task

class MyBasicMathOperator(BaseOperator):
    """
    Example Operator that does basic arithmetic.
    :param first_number: first number to put into an equation
    :param second_number: second number to put into an equation
    :param operation: mathematical operation to perform
    """

    # provide a list of valid operations
    valid_operations = ("+", "-", "*", "/")
    # define which fields can use Jinja templating
    template_fields = ("first_number", "second_number")
    ui_color = "#ff0000"
    ui_fgcolor = "#000000"

    def __init__(
        self,
        first_number: float,
        second_number: float,
        operation: str,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.first_number = first_number
        self.second_number = second_number
        self.operation = operation

        # raise an import error if the operation provided is not valid
        if self.operation not in self.valid_operations:
            raise ValueError(
                f"{self.operation} is not a valid operation. Choose one of {self.valid_operations}"
            )

    def execute(self, context):
        self.log.info(
            f"Equation: {self.first_number} {self.operation} {self.second_number}"
        )
        if self.operation == "+":
            res = self.first_number + self.second_number
            self.log.info(f"Result: {res}")
            return res
        if self.operation == "-":
            res = self.first_number - self.second_number
            self.log.info(f"Result: {res}")
            return res
        if self.operation == "*":
            res = self.first_number * self.second_number
            self.log.info(f"Result: {res}")
            return res
        if self.operation == "/":
            try:
                res = self.first_number / self.second_number
            except ZeroDivisionError as err:
                self.log.critical(
                    "If you have set up an equation where you are trying to divide by zero, you have done something WRONG. - Randall Munroe, 2006"
                )
                raise ZeroDivisionError

            self.log.info(f"Result: {res}")
            return res


@dag(
    dag_id="6-custom-operator",
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    # render Jinja template as native Python object
    catchup=False,
    render_template_as_native_obj=True,  ## To maintain the data type as original type so that it is not converted to the string type
)

def my_math_dag():
    add = MyBasicMathOperator(
        task_id="add",
        first_number=23,
        second_number=19,
        operation="+",
        # any BaseOperator arguments can be used with the custom operator too
        doc_md="Addition Task.",
    )

    multiply = MyBasicMathOperator(
        task_id="multiply",
        # use the return value from the add task as the first_number, pulling from XCom
        first_number="{{ ti.xcom_pull(task_ids='add', key='return_value') }}",
        second_number=35,
        operation="-",
    )

    add >> multiply


my_math_dag()