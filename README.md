#Comnect
This has a server which has a socket only to accept connetion and acknowledge the client. Then server program uses the client socket and register its service to a new thread and continues listening for more clients. The thread know the client socket and deals with it. The client is a simple one. See how sockets behave differently in server; server's native socket listens for new connections that is it. The actual client-server conversation is more of a client(at server side) socket - client socket conversation.

