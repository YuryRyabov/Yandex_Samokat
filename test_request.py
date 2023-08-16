# Юрий Рябов, 7-я когорта — Финальный проект. Инженер по тестированию плюс
import stand_request
import data


def test_create_order_and_check_status():
    # Шаг 1: Создать заказ
    create_response = stand_request.create_order(data.ORDER_DATA)
    assert create_response.status_code == 201

    # Сохранить номер трека заказа
    order_tracking_number = create_response.json().get("track")

    # Шаг 2: Получить заказ по номеру отслеживания
    get_response = stand_request.get_order_by_track(order_tracking_number)

    # Проверить, что код ответа равен 200
    assert get_response.status_code == 200

    print(order_tracking_number)  # Вывести номер трека
    print(get_response.status_code)  # Вывести код ответа


if __name__ == '__main__':
    test_create_order_and_check_status()
