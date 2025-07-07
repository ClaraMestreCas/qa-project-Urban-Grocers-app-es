from sender_stand_request import get_new_user_token, post_new_client_kit
import data as data

# Función para clonar y modificar kit_body
def get_kit_body(name):
    body = data.kit_body.copy()
    body["name"] = name
    return body

def positive_assert(kit_body):
        resp_user = get_new_user_token(data.user_body)
        assert resp_user.status_code == 201
        assert  resp_user.json()['authToken'] != ''
        auth_token = resp_user.json()['authToken']

        response = post_new_client_kit(kit_body, auth_token)
        assert response.status_code == 201
        assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
        resp_user = get_new_user_token(data.user_body)
        assert resp_user.status_code == 201
        assert  resp_user.json()['authToken'] != ''
        auth_token = resp_user.json()['authToken']

        response = post_new_client_kit(kit_body, auth_token)
        assert response.status_code == 400

#PRUEBAS
# 1. Un solo carácter
def test_kit_name_min_length():
    kit_body = get_kit_body(data.kit_name_1_char)
    positive_assert(kit_body)

# 2. 511 caracteres
def test_kit_name_max_valid_length():
    kit_body = get_kit_body(data.kit_name_511_char)
    positive_assert(kit_body)

# 3. 0 caracteres (vacío)
def test_kit_name_zero_length():
    kit_body = get_kit_body(data.kit_name_0_char)
    negative_assert_code_400(kit_body)

# 4. 512 caracteres (exceso)
def test_kit_name_too_long():
    kit_body = get_kit_body(data.kit_name_512_char)
    negative_assert_code_400(kit_body)

# 5. Caracteres especiales
def test_kit_name_special_chars():
    kit_body = get_kit_body(data.kit_name_special_char)
    positive_assert(kit_body)

# 6. Espacios incluidos
def test_kit_name_with_spaces():
    kit_body = get_kit_body(data.kit_name_space_char)
    positive_assert(kit_body)

# 7. Números
def test_kit_name_with_numbers():
    kit_body = get_kit_body(data.kit_name_number_char)
    positive_assert(kit_body)

# 8. Falta el parámetro "name"
def test_kit_name_missing_param():
    auth_token, user_id = get_new_user_token()
    kit_body = {}  # No name key
    response = post_new_client_kit(kit_body, auth_token, user_id)
    assert response.status_code == 400

# 9. Tipo de dato incorrecto (entero en lugar de string)
def test_kit_name_wrong_type():
    kit_body = get_kit_body(data.kit_name_incorrect_char)
    negative_assert_code_400(kit_body)
