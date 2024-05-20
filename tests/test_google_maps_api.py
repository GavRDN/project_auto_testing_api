
import allure
from utils.checking import Checking
from utils.api import Google_maps_api

"""Создание, изменение и удаление новой локации"""

@allure.epic("Создание новой локации")
class Test_create_place:

    @allure.description("Создание, изменение и удаление новой локации")
    def test_create_new_place(self):
        print("\nМетод POST")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')
        # token = json.loads(result_post.text)      # Чтобы увидеть какие поля присутствуют
        # print(list(token))

        print("\nМетод GET для новой локации")
        result_get = Google_maps_api.get_place(place_id)
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')
        # token = json.loads(result_get.text)
        # print(list(token))

        print("\nМетод PUT")
        result_put = Google_maps_api.put_place(place_id)
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("\nМетод GET для измененной локации")
        result_get = Google_maps_api.get_place(place_id)
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("\nМетод DELETE")
        result_delete = Google_maps_api.delete_place(place_id)
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("\nМетод GET для удаленной локации")
        result_get = Google_maps_api.get_place(place_id)
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        # Checking.check_json_value(result_get, 'msg', "Delete operation failed, looks like the data doesn't exists")       # Если в строке есть ковычка (doesn't), то проверка провалится
        Checking.check_json_search_word_in_value(result_get, 'msg', 'Get operation failed')

        print("\nМетод DELETE для удаленной локации")
        result_delete = Google_maps_api.delete_place(place_id)
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_delete, 404)
        Checking.check_json_token(result_delete, ['msg'])
        Checking.check_json_search_word_in_value(result_delete, 'msg', 'Delete operation failed')

        print("\nТестирование прошло успешно")
