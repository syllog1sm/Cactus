#coding:utf-8
from cactus.deployment.auth import BaseKeyringCredentialsManager


class FTPCredentialsManager(BaseKeyringCredentialsManager):
    _username_config_entry = "ftp-username"
    _password_display_name = "FTP Password"
    _keyring_service = "cactus/ftp"
