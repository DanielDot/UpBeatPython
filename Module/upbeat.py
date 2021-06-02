import httpx
class stats:
    async def session():
        async with httpx.AsyncClient() as client:
            response = await client.get("https://upbeatradio.net/api/v1/stats")
            response_dict = response.json()
            return response_dict
    class song:
        async def title(response: dict):
            value = str(response["song"]["title"])
            return value
        async def artist(response: dict):
            value = str(response["song"]["artist"])
            return value
        async def text(response: dict):
            value = f'{response["song"]["title"]} - {response["song"]["title"]}'
            return value
        async def cover(response: dict):
            value = str(response["song"]["art"])
            return value
        async def preview(response: dict):
            value = str(response["song"]["preview"])
            if value == "-1":
                return None
            return value
        async def spotify(response: dict):
            value = str(response["song"]["spotify_id"])
            if value == "-1":
                return None
            return value
        async def likes(response: dict):
            value = int(response["song"]["likes"])
            return value
        async def dislikes(response: dict):
            value = int(response["song"]["dislikes"])
            return value
        async def favourites(response: dict):
            value = int(response["song"]["favourites"])
            return value
        async def played(response: dict):
            value = int(response["song"]["played"])
            return value

    class presenter:
        async def name(response: dict):
            value = str(response["onair"]["name"])
            if value == "Auto DJ":
                return "UpBeat Stream"
            return value
        async def likes(response: dict):
            value = str(response["onair"]["likes"])
            if value == "-1":
                return None
            return int(value)
        async def profile(response: dict):
            value = str(response["onair"]["profile_url"])
            return value
        async def avatar(response: dict):
            value = str(response["onair"]["avatar"])
            return value
        async def userid(response: dict):
            value = str(response["onair"]["id"])
            if value == "-1":
                return None
            return int(value)
        async def show(response: dict):
            try:
                value = response["onair"]["show"]
            except KeyError:
                value = False
            return value
        
        class socials:
            async def snapchat(response: dict):
                try:
                    value = response["onair"]["socials"]["snapchat"]
                except KeyError:
                    value = None
                return value
            async def spotify(response: dict):
                try:
                    value = response["onair"]["socials"]["spotify"]
                except KeyError:
                    value = None
                return value
            async def twitter(response: dict):
                try:
                    value = response["onair"]["socials"]["twitter"]
                except KeyError:
                    value = None
                return value
            async def instagram(response: dict):
                try:
                    value = response["onair"]["socials"]["instagram"]
                except KeyError:
                    value = None
                return value
            async def youtube(response: dict):
                try:
                    value = response["onair"]["socials"]["youtube"]
                except KeyError:
                    value = None
                return value
    class booking:
        async def day(response: dict):
            t = str(response["onair"]["day"])
            if t == "1":
                f = "Monday"
            elif t == "2":
                f = "Tuesday"
            elif t == "3":
                f = "Wednesday"
            elif t == "4":
                f = "Thursday"
            elif t == "5":
                f = "Friday"
            elif t == "6":
                f = "Saturday"
            elif t == "7":
                f = "Sunday"
            return f
        async def hour(response: dict):
            t = str(response["onair"]["hour"])
            if t == "1":
                f = "01:00 - 02:00"
            elif t == "2":
                f = "02:00 - 03:00"
            elif t == "3":
                f = "03:00 - 04:00"
            elif t == "4":
                f = "04:00 - 05:00"
            elif t == "5":
                f = "05:00 - 06:00"
            elif t == "6":
                f = "06:00 - 07:00"
            elif t == "7":
                f = "07:00 - 08:00"
            elif t == "8":
                f = "08:00 - 09:00"
            elif t == "9":
                f = "09:00 - 10:00"
            elif t == "10":
                f = "10:00 - 11:00"
            elif t == "11":
                f = "11:00 - 12:00"
            elif t == "12":
                f = "12:00 - 13:00"
            elif t == "13":
                f = "13:00 - 14:00"
            elif t == "14":
                f = "14:00 - 15:00"
            elif t == "15":
                f = "15:00 - 16:00"
            elif t == "16":
                f = "16:00 - 17:00"
            elif t == "17":
                f = "17:00 - 18:00"
            elif t == "18":
                f = "18:00 - 19:00"
            elif t == "19":
                f = "19:00 - 20:00"
            elif t == "20":
                f = "20:00 - 21:00"
            elif t == "21":
                f = "21:00 - 22:00"
            elif t == "22":
                f = "22:00 - 23:00"
            elif t == "23":
                f = "23:00 - 00:00"
            elif t == "24":
                f = "00:00 - 01:00"
            return f
        async def text(response: dict):
            day = await stats.booking.day(response)
            hour = await stats.booking.hour(response)
            return f"{day} at {hour}"
async def version():
    return "V2.0.0"