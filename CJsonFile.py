import json
import io


class JsonFile:

    def __init__(self, _json_file_name):
        self.file_name = _json_file_name

    def json_details_write(self, _list_size, _current_number, _current_link):
        percent = (_current_number/_list_size)*100  # percent calc
        # Define data
        data = {'%': percent,
                'range': _list_size,
                'current': _current_number,
                'link': _current_link}
        # Write JSON file
        with io.open(self.file_name + '.json', 'w') as outfile:
            str_ = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
            outfile.write(str_)
