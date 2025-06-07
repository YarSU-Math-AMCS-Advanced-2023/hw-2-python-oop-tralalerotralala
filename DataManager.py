import json
import os
from typing import List, Dict
from datetime import datetime


class DataManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.users_file = "users.json"
        self.ads_file = "ads.json"
        self.current_user = None
        self.users = self._load_data(self.users_file)
        self.ads = self._load_data(self.ads_file)

    def _load_data(self, filename: str) -> Dict:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f, indent=4)

    def save_ads(self):
        with open(self.ads_file, 'w') as f:
            json.dump(self.ads, f, indent=4)

    def register_user(self, user_data: Dict) -> bool:
        if user_data['login'] in self.users:
            return False
        self.users[user_data['login']] = user_data
        self.save_users()
        return True

    def authenticate_user(self, login: str, password: str) -> bool:
        if login in self.users and self.users[login]['password'] == password:
            self.current_user = login
            return True
        return False

    def add_ad(self, ad_data: Dict):
        if not self.ads:
            ad_id = "1"
        else:
            max_id = max(int(k) for k in self.ads.keys())
            ad_id = str(max_id + 1)

        ad_data['id'] = ad_id
        ad_data['owner'] = self.current_user
        ad_data['popularity'] = 0
        ad_data['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ads[ad_id] = ad_data
        self.save_ads()

    def update_ad(self, ad_id: str, ad_data: Dict):
        if ad_id in self.ads:
            self.ads[ad_id].update(ad_data)
            self.save_ads()

    def delete_ad(self, ad_id: str):
        if ad_id in self.ads:
            del self.ads[ad_id]
            self.save_ads()

    def increment_popularity(self, ad_id: str):
        if ad_id in self.ads:
            self.ads[ad_id]['popularity'] += 1
            self.save_ads()

    def get_user_ads(self) -> List[Dict]:
        return [ad for ad in self.ads.values() if
                ad['owner'] == self.current_user]

    def get_all_ads(self) -> List[Dict]:
        return list(self.ads.values())