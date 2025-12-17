from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer(('localhost', 9000),
                        requestHandler=RequestHandler) as server:
    class InsultFilter:
        def __init__(self):
            self.filtered = []
            self.insults = ["idiot", "stupid", "nerd"]

        def submit_text(self, text):
            for insult in self.insults:
                text = text.replace(insult, "CENSORED")
            self.filtered.append(text)
            return text

        def get_filtered(self):
            return self.filtered
    
    server.register_instance(InsultFilter())
    
    # Run the server's main loop
    print("InsultFilter XMLRPC running on port 8000")

    server.serve_forever()