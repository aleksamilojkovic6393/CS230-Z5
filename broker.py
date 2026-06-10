import analitika_server

registar_funkcija = {
    "analizaPodataka": analitika_server
}

def prosledi_zahtev(naziv_funkcije):
    if naziv_funkcije in registar_funkcija:
        server = registar_funkcija[naziv_funkcije]

        if naziv_funkcije == "analizaPodataka":
            return server.analizaPodataka()

    return "Funkcija nije pronađena."