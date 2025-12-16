import xmlrpc.client


def subscription_helper():
    from xmlrpc.server import SimpleXMLRPCServer
    from xmlrpc.server import SimpleXMLRPCRequestHandler

    class RequestHandler(SimpleXMLRPCRequestHandler):
        rpc_paths = ('/RPC2',)
    
    server = SimpleXMLRPCServer(('localhost', 8001),
                            requestHandler=RequestHandler, 
                            logRequests=False,
                            allow_none=True)
    server.register_introspection_functions() # not really needed

    def send_broadcast(message):
        print("Broadcasting: ", message)

    server.register_function(send_broadcast)

    return server
    #server.handle_request()


if __name__ == "__main__":
    insult_srv = xmlrpc.client.ServerProxy("http://localhost:8000")

    insult_srv.add_insult("idiot")
    insult_srv.add_insult("stupid")

    print(insult_srv.get_insults())

    server = subscription_helper()
    insult_srv.subscribe_broadcaster("8001")
    server.serve_forever()