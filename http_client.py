import json

from kivy.network.urlrequest import UrlRequest


class HttpClient:
    def get_pizzas(self, on_complete, on_error):
        url = "https://issppizzamamdjango.herokuapp.com/api/GetPizzas"

        def data_receive(request, result):
            data = json.loads(result)
            pizzas_dict = []
            for i in data:
                pizzas_dict.append(i["fields"])
            print("data_receive")
            if on_complete:
                on_complete(pizzas_dict)

        def data_error(request, error):
            if on_error:
                on_error(str(error))

        def data_failure(req, result):
            if on_error:
                on_error(f"Erreur serveur :  {req.resp_status}")

        req = UrlRequest(url, on_success=data_receive, on_error=data_error, on_failure=data_failure)
