import pytest
import requests


@pytest.fixture
def api_url():
    return "http://localhost:5000/polynomial"  # Укажите URL вашего API


def test_fit_polynomial(api_url):
    # Тестирование функции polynomial через HTTP запросы

    # Входные данные
    target_values = [27, 6, 72, 4, 7, -86, -10, 24, -14, -92]
    feature_values = [13, 66, -3, -99, 22, 38, 57, -85, -92, 85]
    degree = 3

    # Отправка HTTP POST-запроса
    response = requests.post(api_url, json={
        "target_values": target_values,
        "feature_values": feature_values,
        "degree": degree
    })

    # Проверка статус-кода HTTP-ответа
    assert response.status_code == 200

    # Проверка JSON-ответа
    json_data = response.json()

    # Проверка наличия ключей в JSON-ответе
    assert "predicted_values" in json_data
    assert "model_parameters" in json_data

    # Получение предсказанных значений и параметров модели
    predicted_values = json_data["predicted_values"]
    model_parameters = json_data["model_parameters"]

    # Проверка размерности векторов предсказанных значений и параметров модели
    assert len(predicted_values) == len(target_values)
    assert len(model_parameters) == degree + 1

    # Проверка значений предсказанных значений
    assert predicted_values[0] == pytest.approx(3.74725248, abs=1e-6)
    assert predicted_values[1] == pytest.approx(3.79638999, abs=1e-6)
    assert predicted_values[2] == pytest.approx(3.65947495, abs=1e-6)
    assert predicted_values[2] == pytest.approx(2.72174419, abs=1e-6)
    assert predicted_values[2] == pytest.approx(8.58886266, abs=1e-6)
    assert predicted_values[2] == pytest.approx(2.6288271, abs=1e-6)
    assert predicted_values[2] == pytest.approx(0.74721045, abs=1e-6)
    assert predicted_values[2] == pytest.approx(23.66765713, abs=1e-6)
    assert predicted_values[2] == pytest.approx(-19.65369053, abs=1e-6)
    assert predicted_values[2] == pytest.approx(-91.90372842, abs=1e-6)

    # Проверка значений параметров модели
    assert model_parameters[0] == pytest.approx(3.72238667, abs=1e-6)
    assert model_parameters[1] == pytest.approx(-0.00072476, abs=1e-6)
    assert model_parameters[2] == pytest.approx(0.00050881, abs=1e-6)
    assert model_parameters[2] == pytest.approx(0.00023531, abs=1e-6)
