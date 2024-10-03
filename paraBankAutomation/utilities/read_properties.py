import configparser
import os.path

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir,'..'))
file_path = os.path.join(project_root,'configurations\\config.ini')

config = configparser.RawConfigParser()
config.read(file_path)

class Read_Config:
    @staticmethod
    def get_base_url():
        url = config.get('login info','base_Url')
        return url
    @staticmethod
    def get_username():
        username = config.get('login info', 'username')
        return username
    @staticmethod
    def get_password():
        password = config.get('login info','password')
        return password