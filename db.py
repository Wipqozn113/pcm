import sqlite3

class Player:
    def __init__(self, name, sheet):
        self.name = name
        self.sheet = sheet

class DatabaseHandler:
    def __init__(self):
        self.connection = sqlite3.connect("pcm.db")
        self.cursor = self.connection.cursor()
        self.__CreateTables__()

    def __TableExists__(self, name):
        res = self.cursor.execute(f"SELECT name FROM sqlite_master WHERE name='{name}'")
        return res.fetchone() is not None
    
    def __CreateTable__(self, tablename, columns):
        if not self.__TableExists__(tablename):
            print(f"Creating table {tablename}...")
            self.cursor.execute(f"CREATE TABLE {tablename}{columns}")

    def __CreateTables__(self):
        self.__CreateTable__("players", ("name", "sheet"))

    ###################
    # Player Handlers #
    ###################
    def GetPlayers(self):
        players = []
        for row in self.cursor.execute("SELECT name, sheet FROM players"):
            players.append(Player(row[0], row[1]))
        return players
    
    def PopulatePlayers(self, players):
        self.cursor.execute("DELETE FROM players")
        self.connection.commit()
        for player in players:
            self.CreatePlayer(player.name, player.sheet)

    def CreatePlayer(self, name, sheet):
        self.cursor.execute(f"INSERT INTO players VALUES (\"{name}\", \"{sheet}\")")
        self.connection.commit()
