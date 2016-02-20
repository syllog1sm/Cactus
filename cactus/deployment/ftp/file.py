#coding:utf-8

from cactus.deployment.file import BaseFile
from cactus.utils.helpers import CaseInsensitiveDict


class FtpFile(BaseFile):
    def remote_changed(self):
        return True

    def do_upload(self):
        # TODO
        raise NotImplementedError
