import json
import os
from typing import List, Dict
from datetime import datetime
from Manager import Manager
from UserManager import UserManager
from AdManager import AdManager
from typing import List


class DataManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.__user_manager = UserManager()
        self.__ad_manager = AdManager()

    @property
    def users(self) -> List:
        return self.__user_manager.users

    @property
    def current_user(self) -> str:
        return self.__user_manager.current_user

    @property
    def ads(self) -> List:
        return self.__ad_manager.ads

    def add_ad(self, ad_data: Dict):
        self.__ad_manager.add_ad(self.current_user)

    def get_user_ads(self) -> List[Dict]:
        return self.__ad_manager.get_user_ads(self.current_user)
