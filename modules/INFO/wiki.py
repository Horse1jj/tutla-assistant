from ..Module import * 
import wikipedia
from ..Utils import * 
async def wiki_callback(CommandObject,message,self,params,command_data):
                    try: await message.channel.send(wikipedia.summary(message_without_command(CommandObject,params),3))
                    except Exception as e:
                        await message.channel.send("Error in object: \n```python\n"+str(e)+'```')

wiki_command = Command("wiki","Look something off wikipedia.",wiki_callback,INFO,aliases=["wikipedia",'what','whatis'],params=["WIKIPEDIA PROMPT"])