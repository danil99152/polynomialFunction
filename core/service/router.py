import datetime

import numpy as np
from fastapi import APIRouter
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sqlalchemy import insert


from service.configs import PolynomialParams, LaunchFact
from service.models import launch_facts, engine

router = APIRouter()


# Эндпоинт для приема данных полиномиальной функции
@router.post("/polynomial")
def fit_polynomial(params: PolynomialParams) -> dict:
    error_message = None
    model_parameters: list[float] = []
    predicted_values: list[float] = []
    data: dict = {}
    try:
        degree: int = params.degree
        feature_values: list[float] = params.feature_values
        target_values: list[float] = params.target_values

        # Преобразование признаков в матрицу полиномиальных признаков
        poly_features = PolynomialFeatures(degree=degree)
        x = poly_features.fit_transform(np.array(feature_values).reshape(-1, 1))

        # Обучение модели линейной регрессии
        model = LinearRegression()
        model.fit(x, target_values)

        # Получение предсказанных значений
        predicted_values = model.predict(x).tolist()

        # Получение коэффициентов модели
        model_parameters = [model.intercept_] + list(model.coef_[1:])

        data = {"predicted_values": predicted_values,
                "model_parameters": model_parameters}

    except Exception as e:
        error_message = e
        data['polynom_exception'] = e
    finally:
        try:
            # Сохранение факта запуска в базе данных
            launch_fact = LaunchFact(
                launch_date=datetime.datetime.now(),
                function_name="polynomial",
                arguments=params.json(),
                result_parameters=str(model_parameters),
                result_values=str(predicted_values),
                error_message=error_message
            )
            statement = insert(launch_facts).values(launch_fact.dict())
            with engine.connect() as conn:
                conn.execute(statement)
                conn.commit()
        except Exception as e:
            data['db_exception'] = e
        finally:
            return data
