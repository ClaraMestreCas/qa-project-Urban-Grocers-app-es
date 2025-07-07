import requests
import configuration
import data as data


# Función para crear usuario y obtener token
def get_new_user_token(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=user_body,
                             headers=data.headers
    )


# Función para crear un kit personal
def post_new_client_kit(kit_body, auth_token):
    headers_dic = data.headers.copy()
    headers_dic['Authorization'] = f"Bearer {auth_token}";
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers_dic
                         )