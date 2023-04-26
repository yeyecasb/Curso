while True:
    print('Bienvenido al juego de adivinanzas de personajes Marvel')
    print('Respobda las siguientes preguntas para adivinar tu personaje:')
    puede_volar = input('Tu personaje puede volar? (si/no)').lower
    es_humano = input('Tu personaje es humano? (si/no)').lower
    tiene_mascara = input('Tu personaje tiene mascara? (si/no)').lower

    if (puede_volar == 'si' and es_humano == 'si' and tiene_mascara == 'si'):
        print('Tu personaje es un Ironman')
    elif (puede_volar == 'si' and es_humano == 'si' and tiene_mascara == 'no'):
        print('Tu personaje es Capitana Marvel')
    elif (puede_volar == 'si' and es_humano == 'no' and tiene_mascara == 'si'):
        print('Tu personaje es Ronan Accuser')
    elif (puede_volar == 'si' and es_humano == 'no' and tiene_mascara == 'no'):
        print('Tu personaje es VISION')
    elif (puede_volar == 'no' and es_humano == 'si' and tiene_mascara == 'si'):
        print('Tu personaje es Spiderman')
    elif (puede_volar == 'no' and es_humano == 'si' and tiene_mascara == 'no'):
        print('Tu personaje es Hulk')
    elif (puede_volar == 'no' and es_humano == 'no' and tiene_mascara == 'si'):
        print('Tu personaje es Black Bolt')
    elif (puede_volar == 'no' and es_humano == 'no' and tiene_mascara == 'no'):
        print('Tu personaje es Thanos')
    print('Desea volver a jugar? (si/no)')
    respuesta = input()
    if respuesta == 'no':
        print('Gracias por jugar')
        break