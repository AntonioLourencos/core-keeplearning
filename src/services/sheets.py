import gspread
from oauth2client.service_account import ServiceAccountCredentials
from src.models.user import User


class Sheets:
    def __init__(self):
        self.scope = [
            "https://spreadsheets.google.com/feeds",
            'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(
            "src/config/keeplearning-348211-ffa98db84399.json",
            self.scope
        )
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("KeepLearning")

    def register(self, data: User):
        sheet = self.sheet.get_worksheet(0)
        sheet.insert_rows(
            [[
                data.name,
                data.email,
                data.discord,
                data. description
            ]],
            row=2)
        return 'Sucesso!'
