import time

contador = 30

while contador > 0:
    print(f"Contagem: {contador:2}", end="\r", flush=True)
    contador -= 1
    time.sleep(1)

print("Fim!")
