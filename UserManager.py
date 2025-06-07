from Manager import Manager


class UserManager(Manager):
    def __init__(self):
        self.users_file = "users.json"
        self.current_user = None
        self.users = self._load_data(self.users_file)

    def save(self):
        with open(self.ads_file, 'w') as f:
            json.dump(self.users, f, indent=4)

    def _load(self):
        if os.path.exists(self.ads_file):
            with open(self.users_file, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def register_user(self, user_data: Dict) -> bool:
        if user_data['login'] in self.users:
            return False
        self.users[user_data['login']] = user_data
        self.save()
        return True

    def authenticate_user(self, login: str, password: str) -> bool:
        if login in self.users and self.users[login]['password'] == password:
            self.current_user = login
            return True
        return False