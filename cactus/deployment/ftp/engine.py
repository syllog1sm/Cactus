#coding:utf-8

from cactus.deployment.engine import BaseDeploymentEngine
from cactus.deployment.ftp.auth import FtpCredentialsManager
from cactus.deployment.ftp.file import FtpFile


class FtpDeploymentEngine(BaseDeploymentEngine):
    CredentialsManagerClass = FtpCredentialsManager
    FileClass = FtpFile
    
    def deploy(self):
        # TODO
        raise NotImplementedError
