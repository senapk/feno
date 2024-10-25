import chardet
import os

class Decoder:

    @staticmethod
    def load(file_path: str) -> str:
        with open(file_path, "rb") as file:
            raw_data = file.read()
            enc_dict = chardet.detect(raw_data)
            encoding = enc_dict["encoding"]
            if encoding is None:
                encoding = "utf-8"
            try:
                content = raw_data.decode(encoding)
            except UnicodeDecodeError as e:
                content = raw_data.decode("utf-8")
            return content

    @staticmethod
    def save(file_path: str, content: str):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
