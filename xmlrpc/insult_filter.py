from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

class InsultFilter:
    def __init__(self):
        self.filtered = []
        self.insults = []
    
    def update_insults(self):
        proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")
        self.insults = proxy.get_insults()
        return True
    
    def submit_text(self, text):
        for insult in self.insults:
            text = text.replace(insult, "CENSORED")
        self.filtered.append(text)
        return text
    
    def get_filtered(self):
        return self.filtered
    
server = SimpleXMLRPCServer(("localhost", 9001))
filter_service = InsultFilter()
server.register_instance(filter_service)
print("InsultFilter XMLRPC running on port 9001")
server.serve_forever()