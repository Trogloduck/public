Used in modern authentication

The client no longer directly provides name and password (credentials) to the server

1. Client sends credentials to identity provider
2. Identity provider generates token and sends it to client
3. Client sends token to server
4. Server gets token from identity provider (whom it *trusts*)
5. Server checks tokens are identical

**Token** ***claims*** (attributes):
- **Subject**: who?
- **Issued at**: when?
- **Expiration**: when no longer valid?
- **Audience**: for who?