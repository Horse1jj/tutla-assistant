mods = []
class Mod:
    def __init__(self,name,description):
        global mods
        self.name = name
        self.description = description

        self.initial = None
        self.onMessage = None
        self.onDelete = None

        self.bot = None

        mods.append(self)
    async def initial_executor(self,function):
        self.initial = function
        await function()
    def on_message(self, function):
        self.onMessage = function
    def on_delete(self,function):
        self.onDelete = function
    