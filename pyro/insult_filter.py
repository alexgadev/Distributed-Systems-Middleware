import Pyro4

@Pyro4.expose
class InsultFilter:
    def __init__(self):
        self.filtered = []
        self.insults = []
        self.insult_proxy = None

    def submit_service_uri(self, uri):
        self.insult_proxy = Pyro4.Proxy(uri)

    def update_insults(self):
        self.insults = self.insult_proxy.get_insults()
        print(self.insults)
        return True
    
    def submit_text(self, text):
        for insult in self.insults:
            text = text.replace(insult, "CENSORED")
        self.filtered.append(text)
        return text
    
    def get_filtered(self):
        return self.filtered

#Daemon
daemon = Pyro4.Daemon()
uri = daemon.register(InsultFilter)
print("InsultFilter PyRO URI: ", uri)

daemon.requestLoop()