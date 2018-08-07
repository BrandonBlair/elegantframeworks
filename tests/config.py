class Config:
    def __init__(self, env):
        
        self.base_url = {
            'dev': 'https://mydev-env.com',
            'qa': 'https://myqa-env.com',
            'staging': 'staging'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80,
            'staging': 8088
        }[env]
        