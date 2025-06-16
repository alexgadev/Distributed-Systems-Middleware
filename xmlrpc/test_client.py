import xmlrpc.client
import time

insult_srv = xmlrpc.client.ServerProxy("http://localhost:9000/")
filter_srv = xmlrpc.client.ServerProxy("http://localhost:9001/")

insult_srv.add_insult("idiot")
insult_srv.add_insult("stupid")

time.sleep(1)
filter_srv.update_insults()

print(filter_srv.submit_text("You are such an idiot!"))
print(filter_srv.submit_text("Don't be stupid."))
print("Filtered text: ", filter_srv.get_filtered())