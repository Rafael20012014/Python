import keyboard

texto = ""

while True:
    evento = keyboard.read_event()
    print("O evento executado foi: ", evento)

    if evento.event_type == keyboard.KEY_DOWN:
        letra = evento.name
        print("O nome do evento/letra é:", letra)
        texto += letra
        print("O texto é:", texto)

        if texto == "ola":
            print(texto + " mundo!")
