

from typing import Dict
import logging


class BaseService:
    def __init__(self) -> None:
       self.logger = logging.getLogger(
           f"{__name__}.{self.__class__.__name__}",)


class UserService(BaseService):
    def __init__(self,db:str) -> None:
        super().__init__()

    def get_user(self, email:str)-> Dict[str,str]:
        self.logger.debug("User %s has been found",email)
        return { "email": email , "password" : 1234}