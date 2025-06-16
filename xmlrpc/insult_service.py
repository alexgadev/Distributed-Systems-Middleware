from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread
import random, time

class InsultService:
    def __init__(self):
        self.insults = []
        self.running = True

    def add_insult(self, insult):
        if insult not in self.insults:
            self.insults.append(insult)
            return True
        return False
    
    def get_insults(self):
        return self.insults
    
    def start_broadcast(self):
        def run():
            while self.running:
                if self.insults:
                    print("Broadcasting: ", random.choice(self.insults))
                time.sleep(5)
        Thread(target=run, daemon=True).start()
        return True

server = SimpleXMLRPCServer(("localhost", 9000))
service = InsultService()
server.register_instance(service)
service.start_broadcast()
print("InsultService XMLRPC running on port 9000")
server.serve_forever()