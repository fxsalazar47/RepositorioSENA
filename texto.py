# # texto = """Hamas y la "promocion de la democracia" Noam Chomsky

# # Hamas gano combinando una fuerte resistencia contra la ocupacion militar con la creacion de organizaciones sociales de base y de servicio a los pobres, una plataforma y una practica que probablemente haria ganar votos en cualquier lugar. La victoria electoral de Hamas es ominosa pero comprensible, a la luz de los acontecimientos. Es enteramente justo describir a Hamas como fundamentalista, extremista y violentista, y como una seria amenaza a la paz y a un acuerdo politicamente justo. Sin embargo, es útil recordar que en aspectos importantes, Hamas no es tan extremista como otros. Por ejemplo, declara que estaría de acuerdo con una tregua con Israel sobre la base de la frontera reconocida a nivel internacional antes de la guerra arabe-israeli de junio de l967. ..

# # La posición de Washington hacia las elecciones en Palestina ha sido coherente. Las elecciones fueron postergadas hasta la muerte de Yasser Arafat, que fue recibida como una oportunidad para la realización de la "visión" de Bush sobre un eventual Estado palestino democrativo, que es una palido y vago reflejo del consenso internacional sobre una acuerdo de dos entidades estatales en la zona, que Estados Unidos viene bloqueando desde hace 30 años....

# # El compromiso formal de Hamas de "destruir Israel" lo pone a la par con Estados Unidos e Israel, que prometieron por mucho tiempo que no habria ningun "Estado palestino adicional" (aparte de Jordania", hasta que ambas naciones aflojaron parcialmente su posicion, para aceptar un mini Estado constituido por los fragmentos que queden despues que Israel se apropie de todas las partes de Palestina que desea....

# # Simplemente como conjetura, imagine el lector una inversion de las circunstancias: que Hamas permitiese a los israelies vivir en cantones desparramados e invariables, virtualmente separados unos de otros, y en alguna pequeña parte de Jerusalen, mientras los palestinos construyen enormes asentamientos y proyectos de infraestructura para apoderarse de las tierras y los recursos de Israel, Y que, ademas Hamas acepte llamar a esos fragmentos "un Estado". Si se hicieran propuestas para esta empobrecida "categoria de Estado", nosotros nos sentiriamos, con razon, horrorizados. Pero con ese tipo de propuestas, la posicion de Hamas seria esencialmente igual a la de Estados Unidos e Israel.

# # """
# # buscar = texto.find("empobrecida")
# # print(buscar)

# #--------------------------------------------------------

# texto = """Hamas y la "promocion de la democracia" Noam Chomsky

# Hamas gano combinando una fuerte resistencia contra la ocupacion militar con la creacion de organizaciones sociales de base y de servicio a los pobres, una plataforma y una practica que probablemente haria ganar votos en cualquier lugar. La victoria electoral de Hamas es ominosa pero comprensible, a la luz de los acontecimientos. Es enteramente justo describir a Hamas como fundamentalista, extremista y violentista, y como una seria amenaza a la paz y a un acuerdo politicamente justo. Sin embargo, es útil recordar que en aspectos importantes, Hamas no es tan extremista como otros. Por ejemplo, declara que estaría de acuerdo con una tregua con Israel sobre la base de la frontera reconocida a nivel internacional antes de la guerra arabe-israeli de junio de l967. ..

# La posición de Washington hacia las elecciones en Palestina ha sido coherente. Las elecciones fueron postergadas hasta la muerte de Yasser Arafat, que fue recibida como una oportunidad para la realización de la "visión" de Bush sobre un eventual Estado palestino democrativo, que es una palido y vago reflejo del consenso internacional sobre una acuerdo de dos entidades estatales en la zona, que Estados Unidos viene bloqueando desde hace 30 años....

# El compromiso formal de Hamas de "destruir Israel" lo pone a la par con Estados Unidos e Israel, que prometieron por mucho tiempo que no habria ningun "Estado palestino adicional" (aparte de Jordania", hasta que ambas naciones aflojaron parcialmente su posicion, para aceptar un mini Estado constituido por los fragmentos que queden despues que Israel se apropie de todas las partes de Palestina que desea....

# Simplemente como conjetura, imagine el lector una inversion de las circunstancias: que Hamas permitiese a los israelies vivir en cantones desparramados e invariables, virtualmente separados unos de otros, y en alguna pequeña parte de Jerusalen, mientras los palestinos construyen enormes asentamientos y proyectos de infraestructura para apoderarse de las tierras y los recursos de Israel, Y que, ademas Hamas acepte llamar a esos fragmentos "un Estado". Si se hicieran propuestas para esta empobrecida "categoria de Estado", nosotros nos sentiriamos, con razon, horrorizados. Pero con ese tipo de propuestas, la posicion de Hamas seria esencialmente igual a la de Estados Unidos e Israel  """

# buscar = texto.find("imagine")
# buscar2 = texto.find("Israel")
# print(f"{buscar} y {buscar2}")
# extraer = texto[704:1726]
# print(extraer)

#-------------------------------------------------------------

# texto = """Bienvenido al mundo de Terraria. Una tierra llena de misterio y maravillas, con gran parte de su destino dejado a las imaginaciones más salvajes... sin embargo, algunas leyendas antiguas se han abierto camino hasta nuestro tiempo presente. Transmitidos por innumerables generaciones de la Orden del Guía, estos pocos fragmentos de información te ayudarán a navegar tu viaje y superar las amenazas que acechan en las sombras. Este conocimiento ahora se transmite a ti, el valiente aventurero, con la esperanza de que te ayude en tu búsqueda para salvar nuestro mundo... 

# Al principio, los dioses establecieron un equilibrio para garantizar la equidad para todas las criaturas vivientes. Este equilibrio iba a ser de suma importancia, sin un costo demasiado grande en la búsqueda de su cumplimiento. Han pasado eones desde que los dioses comenzaron a probar las complejidades de la vida en su experimento de justicia. En este proceso, se crearon innumerables mundos vivos y ahora existen dentro del universo de Terraria. Cada mundo de Terraria es un ser sensible que sabe todo lo que sucede y puede sentir los pensamientos de todas las criaturas vivientes: con el único propósito de garantizar que se mantenga el equilibrio deseado, a menudo de forma violenta. Los mundos utilizan muchos mecanismos de defensa para garantizar que el equilibrio se mantenga a toda costa; algunos de ellos se conocen como Hallow, Corruption y Crimson."""

# buscar = texto.find("Transmitidos")
# buscar2 = texto.find("sombras")
# print(f"{buscar} y {buscar2}")
# extraer = texto [240:416]
# print(extraer)

#-----------------------------------------------------------

texto = """Hace mucho tiempo, muchas razas convivían en armonía, incluyendo humanos, lizahrds y dríades. Sin embargo, un día, Cthulhu, una antigua deidad lunar, llegó de origen desconocido y comenzó a sembrar el caos en el reino.

En respuesta, los lizahrds construyeron un templo que la bestia no pudo penetrar. Como el Señor de la Luna era una deidad lunar, el templo estaba custodiado por un gólem solar (muchas de sus gotas están relacionadas con el sol, lo que alude a su condición de elemental solar), creado por los lizahrds. También instalaron numerosas trampas para proteger el templo y lo sellaron, entregando la llave a una bestia que vive en la selva (plantador) para que la custodiara. También rompieron la placa solar, un objeto capaz de provocar el eclipse, ocultando así el sol y potenciando la luna, invocando así a muchos monstruos de Cthulhu.

Las dríadas se comportaron de forma diferente. Se esforzaron activamente por detener a Cthulhu y lograron arrancarle trozos de cerebro, columna vertebral y ojos. Sin embargo, la consecuencia de la guerra fue la muerte de todas las dríadas, excepto una.

Los numerosos ojos de Cthulhu vagaban por el mundo buscando la manera de reunirse con la deidad lunar."""

buscar1 = texto.find("lizahrds")
buscar2 = texto.find("Cthulhu.")
print(f"{buscar1} y {buscar2}")
extraer = texto[74:850]
print(extraer)