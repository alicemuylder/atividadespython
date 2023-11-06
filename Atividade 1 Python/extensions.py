extensoes = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

nome_arquivo = input("Digite o nome do arquivo: ")

extensao = nome_arquivo.split(".")[-1].lower() if "." in nome_arquivo else ""

if extensao in extensoes:
    print(extensoes[extensao])
else:
    print("application/octet-stream")




