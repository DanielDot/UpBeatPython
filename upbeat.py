import requests
class stats:
    class song:
        def title():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["song"]["title"])
            return t
        def artist():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["song"]["artist"])
            return t
        def combined():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = f'{j["song"]["title"]} - {j["song"]["artist"]}'
            return t
        def cover():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["song"]["art"])
            return t
        def mp3preview():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["song"]["preview"])
            if t == "-1":
                f = "Not Available"
            else:
                f = t
            return f
        def spotifyid():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["song"]["spotify_id"])
            if t == "-1":
                f = "Not Available"
            else:
                f = t
            return f
        def likes():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["song"]["likes"])
            return t
        def dislikes():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["song"]["dislikes"])
            return t
        def favourites():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["song"]["favourites"])
            return t
        def played():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["song"]["played"])
            return t
    class presenter:
        def name():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["onair"]["name"])
            if t == "Auto DJ":
                f = "UpBeat Stream"
            else:
                f = t
            return f
        def likes():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["onair"]["likes"])
            if t == "-1":
                f = "Not Available"
            else:
                f = t
            return f
        def profileurl():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["onair"]["profile_url"])
            return t
        def avatar():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["onair"]["avatar"])
            return t
        def userid():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["onair"]["id"])
            if t == "-1":
                f = "N/A"
            else:
                f = t
            return f
        def show():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            try:
                t = str(j["onair"]["show"])
            except KeyError:
                t = "false"
            return t
        class socials:
            def snapchat():
                r = requests.get("https://upbeatradio.net/api/v1/stats")
                j = r.json()
                try:
                    t = str(j["onair"]["socials"]["snapchat"])
                except KeyError:
                    t = "Not Available"
                return t
            def spotify():
                r = requests.get("https://upbeatradio.net/api/v1/stats")
                j = r.json()
                try:
                    t = str(j["onair"]["socials"]["spotify"])
                except KeyError:
                    t = "Not Available"
                return t
            def twitter():
                r = requests.get("https://upbeatradio.net/api/v1/stats")
                j = r.json()
                try:
                    t = str(j["onair"]["socials"]["twitter"])
                except KeyError:
                    t = "Not Available"
                return t
            def instagram():
                r = requests.get("https://upbeatradio.net/api/v1/stats")
                j = r.json()
                try:
                    t = str(j["onair"]["socials"]["instagram"])
                except KeyError:
                    t = "Not Available"
                return t
                return t
            def youtube():
                r = requests.get("https://upbeatradio.net/api/v1/stats")
                j = r.json()
                try:
                    t = str(j["onair"]["socials"]["youtube"])
                except KeyError:
                    t = "Not Available"
                return t
    class booking:
        def day():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["onair"]["day"])
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
            else:
                f = "N/A"
            return f
        def hour():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["onair"]["hour"])
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
            else:
                f = "N/A"
            return f
        def combined():
            r = requests.get("https://upbeatradio.net/api/v1/stats")
            j = r.json()
            t = str(j["onair"]["day"])
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
            else:
                f = "N/A"
            j = str(j["onair"]["hour"])
            if j == "1":
                m = "01:00 - 02:00"
            elif j == "2":
                m = "02:00 - 03:00"
            elif j == "3":
                m = "03:00 - 04:00"
            elif j == "4":
                m = "04:00 - 05:00"
            elif j == "5":
                m = "05:00 - 06:00"
            elif j == "6":
                m = "06:00 - 07:00"
            elif j == "7":
                m = "07:00 - 08:00"
            elif j == "8":
                m = "08:00 - 09:00"
            elif j == "9":
                m = "09:00 - 10:00"
            elif j == "10":
                m = "10:00 - 11:00"
            elif j == "11":
                m = "11:00 - 12:00"
            elif j == "12":
                m = "12:00 - 13:00"
            elif j == "13":
                m = "13:00 - 14:00"
            elif j == "14":
                m = "14:00 - 15:00"
            elif j == "15":
                m = "15:00 - 16:00"
            elif j == "16":
                m = "16:00 - 17:00"
            elif t == "17":
                m = "17:00 - 18:00"
            elif t == "18":
                m = "18:00 - 19:00"
            elif j == "19":
                m = "19:00 - 20:00"
            elif j == "20":
                m = "20:00 - 21:00"
            elif j == "21":
                m = "21:00 - 22:00"
            elif j == "22":
                m = "22:00 - 23:00"
            elif j == "23":
                m = "23:00 - 00:00"
            elif j == "24":
                m = "00:00 - 01:00"
            else:
                m = "N/A"
            k = f+" at "+m
            return k
    def updated():
        r = requests.get("https://upbeatradio.net/api/v1/stats")
        j = r.json()
        t = str(j["last_updated"])
        return t
    def listeners():
        r = requests.get("https://upbeatradio.net/api/v1/stats")
        j = r.json()
        t = str(j["listeners"])
        return t
def version():
    return "V1.0.0"
