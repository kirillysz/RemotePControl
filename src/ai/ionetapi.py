from aiohttp import ClientSession

class IONetAPI:
    def __init__(self, api_token: str):
        self.token = api_token

        self.urls = {
            "models": "https://api.intelligence.io.solutions/api/v1/models",
            "chat_completions": "https://api.intelligence.io.solutions/api/v1/chat/completions"
        }

        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.token}",  
        }

    async def get_models_list(self) -> dict:
        """
        Get list of available models for Chat Completions API
        """
        async with ClientSession() as session:
            async with session.get(url=self.urls.get("models"), 
                                   headers=self.headers) as response:
                return await response.json()
            

    async def create_chat_completion(self, model: str, message: str) -> dict:
        """
        Creates a model response for the given chat conversation.
        """
        
        data = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        }
        
        async with ClientSession() as session:
            async with session.post(url=self.urls.get("chat_completions"),
                                    headers=self.headers,
                                    json=data) as response:
                return await response.json()
            
    