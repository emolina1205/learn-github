import hashlib

mensaje = "Hola Mundo"
hash_sha256 = hashlib.sha256(mensaje.encode()).hexdigest()

print(hash_sha256)
