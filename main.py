import discord
from revChatGPT.V1 import Chatbot

TOKEN = "MTEyNjg2NzIzMDc4NTgxMDQ2Mg.GdZ7I-.PhQlxwWluj5dhGfT6Ai_B0MqqGFoX0Xofn121s"
self_tag = '<@1126867230785810462>'

chatbot = Chatbot(config={
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJvbGRvbGRwaG90b3MxMjM0NTY3ODlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItRkF1WTBRQUhSRldQRXdmU2h5WFNJUG9jIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNDcxOTY5Mzc3MzA1ODEzMTcyNSIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODk3ODczNDAsImV4cCI6MTY5MDk5Njk0MCwiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.Ygq4CSNhQVYcSFUtxE1MulfZ2IKZdGqnAHJhbxxZHf0mjg-kfqakrLliJTmG9PnzwPGVxTPKt0bX0DtpG_zu4Nl51FsOC1j0zyIUiXVpwL9OujnjH1OYp3w9wvpXeaUeIBNd-8ClEj_attezKrZBd5r0fbVpzqAroibCXrPRTqSnXwDkTorfW3fhoC2vZZyAZcKgi2L5gNCJxXq0HnMu1sv8yZPxQq4o4MeiKG_K7TUUMySKpnAgPfdFEfEDsPA99qXhdSdx1YRV-A1wdpKAyIQag8YmdOONuA7lOaFWA_bKMD2Pbq2dd1fz-RRmvSP-_aYACbgTkMJEWwUQnVEtaQ"
})

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def send_message(message, user_message):
    if user_message == 'help':
        response = f'{message.author.mention}, `Start by tagging @Shiba123 along with the Prompt.`'
        await message.reply(response)
        return
	
    try:
        response = ""
        for data in chatbot.ask(
          user_message
        ):
            response = data["message"]

        Responses = []
        for i in range(0, len(response), 1950):
            Responses.append(response[i:i+1950])

        for Response in Responses:
            await message.reply(f"{message.author.mention}, {Response}")
        
    except Exception as e:
        await message.reply(f'{message.author.mention}, Sorry!! The Following exception occurred.\n\n' + str(e))

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
	
    user_message = str(message.content)
    
    if not isinstance(message.channel, discord.DMChannel):
        group_tag = user_message[:len(self_tag)]
        if group_tag != self_tag:
            return
        else:
           user_message = user_message[len(self_tag)+1:]
    else:
        if user_message[:len(self_tag)] == self_tag:
            user_message = user_message[len(self_tag)+1:]

    async with message.channel.typing():                  
		# Debug printing
        # print(f"{username} said: '{user_message}' ({channel})")
        await send_message(message, user_message)

client.run(TOKEN)
