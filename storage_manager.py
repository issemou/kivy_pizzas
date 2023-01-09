import json


class StorageManager:
    def load_data(self, data_name):
        filename = self.get_filename(data_name)
        try:
            file = open(filename, "r")
            datas = file.read()
            file.close()
        except:
            return None

        return json.loads(datas)

    def save_data(self, data_name, data_content):
        filename = self.get_filename(data_name)
        datas_str = json.dumps(data_content)
        file = open(filename, "w")
        file.write(datas_str)
        file.close()

    def get_filename(self, data_name):
        return data_name + ".json"
