from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

from threading import Thread
import random, time

import xmlrpc.client

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    class InsultService:
        def __init__(self):
            self.insults = []
            self.running = False
            self.subscribers = []

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
                    if self.insults and len(self.subscribers) > 0:
                        for subscriber in self.subscribers:
                            subscriber.send_broadcast(random.choice(self.insults))
                    elif not len(self.subscribers) > 0:
                        break
                    time.sleep(5)
            Thread(target=run, daemon=True).start()
            return True

        def subscribe_broadcaster(self, port):
            self.subscribers.append(xmlrpc.client.ServerProxy("http://localhost:" + port))
            if not self.running:
                self.running = True
                self.start_broadcast()
            return True


    # Register the InsultService instance; all methods of the instance are
    # published as XML-RPC methods
    server.register_instance(InsultService())
    
    # Run the server's main loop
    print("InsultService XMLRPC running on port 8000")

    server.serve_forever()