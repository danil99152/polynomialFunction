from datetime import datetime

from pydantic import BaseModel


# Модель данных для передачи параметров функции
class PolynomialParams(BaseModel):
    target_values: list[float]
    feature_values: list[float]
    degree: int


class LaunchFact(BaseModel):
    launch_date: datetime
    function_name: str
    arguments: str
    result_parameters: str
    result_values: str
    error_message: str | None
