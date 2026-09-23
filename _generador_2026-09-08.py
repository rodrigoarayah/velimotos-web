#!/usr/bin/env python3
# Genera el sitio Velimotor España en la dirección negro / azul eléctrico.
# Todo el contenido proviene de velimotorespaña.com y de la ficha de fábrica de velimotor.com
import pathlib, html

S = pathlib.Path('/mnt/user-data/outputs/velimotor-web'); S.mkdir(parents=True, exist_ok=True)

TEL_T, TEL_U, MAIL = '636 546 877', '+34636546877', 'rodrigoarayah@gmail.com'
CDN = 'https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1600/dJoZGpyJ8zS69rKD/'
FOTO = {
 'hero':   CDN + 'img_0292-Aq2GqNEv03cb3O1G.png',
 'cierre': CDN + 'd69f404f-7477-419d-9555-daab1fc7999b-5wk5fB6x8VBTAlcJ.png',
 'marca':  CDN + 'a61864cb-0254-4bca-8814-df298d79a934-m5K8vNv85MF6aGlX.png',
 'vmx8000-mx': CDN + 'vmx8000-mx-lateral-3UOJRlUtRyBFsV5i.png',
}
NAV = [('modelos.html','Modelos'),('tecnologia.html','Tecnología'),
       ('financiacion.html','Financiación'),('puntos-de-venta.html','Puntos de venta'),
       ('empresas.html','Empresas'),('nosotros.html','Nosotros')]

# ══════════════════════════════════════════════════ MODELOS
M = {
'vmx10s': dict(n='VMX 10S', s='12/18 kW', cat='trail', foto='vmx8000-mx',
  rol='Trail homologada L3e',
  gancho='La única que se matricula',
  txt='Vas a trabajar por asfalto el lunes y subes al monte el sábado, con el mismo carné B '
      'que ya llevas en la cartera. Homologada L3e, equivalente a una 125.',
  med=[('18 kW','Potencia máx.'),('480 N·m','Par'),('110 km/h','Vel. máx.'),
       ('150 km','Autonomía'),('118 kg','Peso'),('2,5 h','Carga')],
  por=[('Carga Type 2','El estándar europeo. Enchufas en la misma red pública que cualquier '
        'coche eléctrico, no solo en el garaje de casa. Ningún rival directo de campo lo tiene.'),
       ('Celdas Farasis','Más de 1.200 ciclos, de un proveedor de la industria del automóvil. '
        'No es un pack genérico de origen desconocido.'),
       ('IP67 en toda la moto','Estanqueidad certificada del conjunto, no solo de la batería. '
        'Vadeo, barro y manguera sin abrir el manual de garantía.'),
       ('Batería fuera en segundos','Compartimento con apertura por botón, 21,9 kg y app '
        'Bluetooth. El baúl admite un segundo pack y duplicas la ruta.')],
  ficha=[('Homologación','L3e con certificado EEC/COC, equivalente a 125 cc'),
    ('Permiso','Carné B con tres años de antigüedad, válido en España. También A1'),
    ('Motor','72 V sin escobillas de imán permanente, central'),
    ('Potencia','12 kW pico (4 kW nominal) o 18 kW pico (6 kW nominal)'),
    ('Par máximo','420 N·m o 480 N·m según versión'),
    ('Transmisión','Automática, relación 2,2:1, con marcha atrás'),
    ('Controlador','Vectorial de onda senoidal con comunicación CAN'),
    ('Velocidad máxima','100 km/h o 110 km/h según versión'),
    ('0 a 100 km/h','9,2 s o 7,8 s según versión'),
    ('Batería','72 V 58 Ah de litio, extraíble, 21,9 kg, con aplicación Bluetooth'),
    ('Celdas','Farasis, más de 1.200 ciclos'),
    ('Cargador','De a bordo 22 A, con puerto estándar y puerto Type 2 europeo'),
    ('Tiempo de carga','2,5 h. Cargadores externos opcionales de 12, 22 y 30 A'),
    ('Autonomía','150 km a 35 km/h, 120 km a 45 km/h, 100 km a 55 km/h'),
    ('Frenos','Disco hidráulico delante y detrás, sistema CBS, dos manetas'),
    ('Suspensión','Horquilla invertida ajustable y monoamortiguador ajustable con botella'),
    ('Neumáticos','90/90-19 delantero y 4.60-18 trasero, marca Kenda'),
    ('Peso','118 kg con batería'),('Carga máxima','150 kg'),
    ('Medidas','2.077 × 815 × 1.215 mm'),('Altura del asiento','880 mm'),
    ('Altura libre al suelo','340 mm'),('Distancia entre ejes','1.342 mm'),
    ('Estanqueidad','IP67 del conjunto de la motocicleta'),
    ('Chasis','Tubo de acero, carrocería en ABS, barra de protección'),
    ('Iluminación','Faro LED'),('Transmisión final','Cadena 520'),
    ('Rampa máxima','35°'),('Instrumentación','Pantalla LCD digital, TFT opcional'),
    ('Arranque','Por llave, con mando a distancia y antirrobo')]),

'vmx800-enduro': dict(n='VMX 800', s='Enduro', cat='cross', foto=None,
  rol='Enduro, tope de gama', gancho='Máxima potencia y máxima autonomía',
  txt='La más completa del catálogo. Rutas largas de montaña sin pensar en dónde está el '
      'siguiente enchufe, y cinco segundos de cero a cien.',
  med=[('25 kW','Potencia máx.'),('5 s','0 a 100'),('140 km/h','Vel. máx.'),
       ('180 km','Autonomía'),('134 kg','Peso'),('2 h','Carga rápida')],
  por=[('180 km reales de ruta','La cifra más alta de la gama de campo. Una jornada completa '
        'sin volver al remolque a cambiar batería.'),
       ('Cinco segundos a cien','Par completo desde parado, sin embrague y sin cambio que '
        'gestionar en una rampa técnica.'),
       ('Dos horas de carga rápida','Comes y vuelves a salir.')],
  ficha=[('Uso','Enduro y rutas de montaña'),('Potencia máxima','25 kW'),
    ('Velocidad máxima','140 km/h'),('Autonomía','150 a 180 km'),('0 a 100 km/h','5 s'),
    ('Peso con batería','134 kg'),('Carga rápida','2 h')]),

'vmx8000-mx': dict(n='VMX 8000', s='MX', cat='cross', foto='vmx8000-mx',
  rol='Motocross', gancho='Entrena una mañana entera sin volver al box',
  txt='Chasis de motocross con la autonomía más alta de la gama. Y en circuitos con '
      'restricción horaria por ruido, entras cuando los demás no pueden.',
  med=[('25 kW','Potencia máx.'),('5 s','0 a 100'),('140 km/h','Vel. máx.'),
       ('180 km','Autonomía'),('132 kg','Peso'),('2 h','Carga rápida')],
  por=[('180 km de autonomía','Sesiones largas sin repostar ni cambiar pack a media mañana.'),
       ('Silencio total','Circuitos con horario limitado, fincas cerca de núcleos urbanos, '
        'zonas protegidas. Sitios donde una de gasolina ya no entra.'),
       ('Sin puesta a punto','Nada de carburación, filtros ni aceite después de un día de polvo.')],
  ficha=[('Uso','Motocross, circuito y campo abierto'),('Potencia máxima','25 kW'),
    ('Velocidad máxima','140 km/h'),('Autonomía','180 km'),('0 a 100 km/h','5 s'),
    ('Peso con batería','132 kg'),('Carga rápida','2 h')]),

'vmx10s-cross': dict(n='VMX 10S', s='Cross', cat='cross', foto=None,
  rol='Cross', gancho='Diez kilos menos y reglaje de campo',
  txt='Misma base que la trail homologada, aligerada y preparada para tierra. La carga rápida '
      'más veloz de los modelos grandes.',
  med=[('18 kW','Potencia máx.'),('5 s','0 a 100'),('140 km/h','Vel. máx.'),
       ('180 km','Autonomía'),('108 kg','Peso'),('1,5 h','Carga rápida')],
  por=[('108 kg','Diez kilos por debajo de la versión de carretera. Se nota en cada cambio '
        'de dirección y al levantarla del suelo.'),
       ('Hora y media de carga','La recarga más rápida de la gama grande.'),
       ('Hasta 180 km','Autonomía de trail dentro de un chasis de campo.')],
  ficha=[('Uso','Cross y campo'),('Potencia máxima','18 kW'),('Velocidad máxima','140 km/h'),
    ('Autonomía','150 a 180 km'),('0 a 100 km/h','5 s'),('Peso con batería','108 kg'),
    ('Carga rápida','1,5 h')]),

'havocker': dict(n='Havocker', s='E-Dirtbike', cat='cross', foto=None,
  rol='Dirtbike', gancho='89 kilos y de 0 a 50 en 2,1 segundos',
  txt='La más explosiva de la gama y la que cabe en un maletero grande. Para quien busca '
      'reacción inmediata más que kilómetros. Sin matrícula y sin ITV.',
  med=[('24 kW','Potencia máx.'),('2,1 s','0 a 50'),('120 km/h','Vel. máx.'),
       ('100 km','Autonomía'),('89 kg','Peso'),('1,5 h','Carga rápida')],
  por=[('89 kg','La más ligera de las grandes. Se levanta entre dos personas.'),
       ('2,1 s de 0 a 50','Es el dato que la vende, y solo se entiende subiéndose.'),
       ('Cero trámites','No se matricula, no pasa ITV y no necesita seguro de circulación '
        'para rodar en recinto privado.')],
  ficha=[('Uso','Dirtbike, recinto privado y finca'),('Potencia máxima','24 kW'),
    ('Velocidad máxima','120 km/h'),('Autonomía','100 km'),('0 a 50 km/h','2,1 s'),
    ('Peso con batería','89 kg'),('Carga rápida','1,5 h')]),

'fay-kids': dict(n='Fay', s='Electric Kids', cat='infantil', foto=None,
  rol='Infantil', gancho='La primera moto, sin gasolina en el garaje',
  txt='48 kilos y velocidad limitable por los padres. Sin escape al rojo vivo, sin bidón en '
      'casa y sin arrancar a patada.',
  med=[('5 kW','Potencia máx.'),('45 km/h','Vel. máx.'),('60 km','Autonomía'),
       ('48 kg','Peso'),('5 s','0 a 40'),('3 h','Carga')],
  por=[('Velocidad limitable','Se ajusta a la edad y a la confianza del crío, y se sube a '
        'medida que aprende.'),
       ('Sin escape ni combustible','No hay tubo caliente al alcance de la mano ni gasolina '
        'almacenada en casa.'),
       ('48 kg','Un peso que un niño puede manejar y levantar con ayuda.')],
  ficha=[('Uso','Infantil, recinto privado'),('Potencia máxima','5 kW'),
    ('Velocidad máxima','45 km/h, limitable'),('Autonomía','60 km'),('0 a 40 km/h','5 s'),
    ('Peso con batería','48 kg'),('Carga','3 h')]),

'vl5000-utv': dict(n='VL 5000', s='UTV', cat='utv', foto=None,
  rol='UTV de trabajo', gancho='El vehículo de flota de la gama',
  txt='Para explotaciones agrícolas, ayuntamientos, campos de golf y grandes recintos donde el '
      'ruido y el humo son un coste operativo y no una preferencia.',
  med=[('18 kW','Potencia máx.'),('60 km/h','Vel. máx.'),('120 km','Autonomía'),
       ('798 kg','Peso'),('7 s','0 a 60'),('6–8 h','Carga')],
  por=[('Cero emisiones locales','Trabaja dentro de naves e invernaderos donde un motor de '
        'combustión no puede entrar.'),
       ('Sin mantenimiento de motor','Ni aceite ni filtros ni revisiones de admisión. Menos '
        'horas de taller y menos vehículo parado.'),
       ('Silencio','Rondas nocturnas, hoteles y zonas residenciales sin generar una queja.')],
  ficha=[('Uso','Utility, finca, obra y servicios municipales'),('Potencia máxima','18 kW'),
    ('Velocidad máxima','60 km/h'),('Autonomía','120 km'),('0 a 60 km/h','7 s'),
    ('Peso con batería','798 kg'),('Carga completa','6 a 8 h')]),
}
ORDEN = ['vmx10s','vmx800-enduro','vmx8000-mx','vmx10s-cross','havocker','fay-kids','vl5000-utv']

# ══════════════════════════════════════════════════ plantilla
def top(t, d, act):
    n = ''.join('<li><a href="%s"%s>%s</a></li>' % (u, ' aria-current="page"' if u == act else '', x)
                for u, x in NAV)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t)}</title>
<meta name="description" content="{html.escape(d)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@112..125,500..800&family=Sora:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="estilo.css">
</head>
<body>
<header class="barra">
  <div class="env">
    <a class="logo" href="index.html">VELIMOT<i>O</i>R</a>
    <button class="abrir" aria-expanded="false" aria-controls="nav">Menú</button>
    <ul class="nav" id="nav">{n}</ul>
    <a class="cta-barra" href="contacto.html">Reservar prueba</a>
  </div>
</header>
<main>
"""

def bottom(extra=''):
    mods = ''.join('<li><a href="%s.html">%s %s</a></li>' % (k, M[k]['n'], M[k]['s']) for k in ORDEN)
    return f"""</main>
<footer>
  <div class="env">
    <div class="pie">
      <div><h4>Gama</h4><ul>{mods}</ul></div>
      <div><h4>Comprar</h4><ul>
        <li><a href="contacto.html">Reservar prueba</a></li>
        <li><a href="financiacion.html">Financiación y ayudas</a></li>
        <li><a href="puntos-de-venta.html">Puntos de venta</a></li>
      </ul></div>
      <div><h4>Profesional</h4><ul>
        <li><a href="empresas.html">Empresas y flotas</a></li>
        <li><a href="puntos-de-venta.html#distribuidor">Ser distribuidor</a></li>
        <li><a href="tecnologia.html">Tecnología</a></li>
      </ul></div>
      <div><h4>Contacto</h4><ul>
        <li><a href="nosotros.html">Quiénes somos</a></li>
        <li><a href="tel:{TEL_U}">+34 {TEL_T}</a></li>
        <li><a href="mailto:{MAIL}">{MAIL}</a></li>
      </ul></div>
    </div>
    <div class="pie-fin">
      <span>Velimotor España, motos eléctricas de enduro, trail y trabajo</span>
      <span><a href="aviso-legal.html">Aviso legal</a> &nbsp; <a href="privacidad.html">Privacidad</a> &nbsp; <a href="cookies.html">Cookies</a></span>
    </div>
  </div>
</footer>
<script>
(function(){{
  var b=document.querySelector('.abrir'), m=document.getElementById('nav');
  if(b) b.addEventListener('click',function(){{
    b.setAttribute('aria-expanded',String(m.classList.toggle('abierta')));
  }});
}})();
</script>
{extra}
</body>
</html>
"""

def pag(f, t, d, cuerpo, act='', extra=''):
    (S / f).write_text(top(t, d, act) + cuerpo + bottom(extra), encoding='utf-8')

def medidas(ms):
    return '<div class="medidas">' + ''.join('<div><b>%s</b><small>%s</small></div>' % v for v in ms) + '</div>'

def visor(k):
    m = M[k]
    img = ('<img src="%s" alt="Velimotor %s %s" loading="lazy">' % (FOTO[m['foto']], m['n'], m['s'])
           if m['foto'] else '')
    return ('<div class="visor"><div class="marco">Foto %s %s, lateral 3/4 sobre fondo neutro</div>%s</div>'
            % (m['n'], m['s'], img))

def cierre(titulo, texto):
    return f"""
<section class="cierre">
  <img src="{FOTO['cierre']}" alt="">
  <div class="env">
    <h2>{titulo}</h2>
    <p>{texto}</p>
    <div class="acc">
      <a class="btn btn-p" href="contacto.html">Reservar una prueba</a>
      <a class="btn btn-s" href="tel:{TEL_U}">{TEL_T}</a>
    </div>
  </div>
</section>"""

GRAFICO = """
    <figure class="grafico ent">
      <h2>Par disponible según régimen del motor</h2>
      <svg viewBox="0 0 460 260" role="img" aria-label="Comparativa: el par del motor eléctrico está al máximo desde cero revoluciones y se mantiene plano; el del motor de combustión sube progresivamente hasta un pico y después cae.">
        <defs><linearGradient id="bc" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#22E4FF" stop-opacity=".22"/>
          <stop offset="100%" stop-color="#22E4FF" stop-opacity="0"/></linearGradient></defs>
        <line x1="42" y1="212" x2="440" y2="212" stroke="#1A2334"/>
        <line x1="42" y1="20" x2="42" y2="212" stroke="#1A2334"/>
        <g stroke="#111A28"><line x1="42" y1="164" x2="440" y2="164"/>
          <line x1="42" y1="116" x2="440" y2="116"/><line x1="42" y1="68" x2="440" y2="68"/></g>
        <path class="traza dibuja" d="M42 212 C 120 208, 168 150, 232 74 C 268 34, 316 40, 352 82 C 386 120, 414 160, 440 196"
              stroke="#4A5670" stroke-width="2.4" style="animation-delay:.35s"/>
        <path d="M42 52 L 316 52 C 372 52, 408 108, 440 178 L 440 212 L 42 212 Z" fill="url(#bc)"
              opacity="0" style="animation:sube 1s ease 1.9s forwards"/>
        <path class="traza dibuja" d="M42 52 L 316 52 C 372 52, 408 108, 440 178"
              stroke="#22E4FF" stroke-width="3.2" style="animation-delay:.9s"/>
        <circle cx="42" cy="52" r="5" fill="#22E4FF" opacity="0" style="animation:sube .5s ease 1.7s forwards"/>
        <text x="6" y="56" fill="#8A97B0" font-family="Sora,sans-serif" font-size="11">máx</text>
        <text x="18" y="216" fill="#8A97B0" font-family="Sora,sans-serif" font-size="11">0</text>
        <text x="386" y="232" fill="#8A97B0" font-family="Sora,sans-serif" font-size="11">régimen</text>
      </svg>
      <div class="leyenda">
        <span><i style="background:#22E4FF"></i> Eléctrico</span>
        <span><i style="background:#4A5670"></i> Combustión</span>
      </div>
      <p class="nota-grafico">Curvas ilustrativas de la forma de entrega, no valores medidos.
        Lo que compara el gráfico es cuándo llega el par, no cuánto.</p>
    </figure>"""

ARGS = [
 ('01','Pasas donde ya no se pasa','Cada temporada se cierran más pistas y montes por quejas '
  'de ruido. Una eléctrica no las genera. No es una ventaja ecológica abstracta: es acceso a '
  'terreno que estás perdiendo.'),
 ('02','Con el carné que ya tienes','La VMX 10S está homologada L3e, equivalente a una 125. En '
  'España se conduce con el carné B con tres años de antigüedad. Sin cursos y sin esperar al A2.'),
 ('03','Se carga como un coche','Puerto Type 2, el estándar europeo. Enchufas en la misma red '
  'pública que cualquier eléctrico, no solo en el garaje. Ningún rival directo de campo lo ofrece.'),
 ('04','El motor no se mantiene','Ni aceite, ni filtros, ni bujías, ni carburación después de un '
  'día de polvo. El tiempo que dedicabas al taller lo dedicas a rodar.'),
]
TEC = [
 ('Celdas Farasis','Más de 1.200 ciclos de vida, de un proveedor de la industria del automóvil. '
  'No es un pack genérico de origen desconocido.'),
 ('Estanqueidad IP67','Certificada para el conjunto de la moto, no solo para la batería. Vadeo, '
  'barro y manguera sin abrir el manual de garantía.'),
 ('Controlador vectorial CAN','Onda senoidal con comunicación CAN. Entrega progresiva en '
  'tracción baja en lugar de un interruptor de todo o nada.'),
 ('Batería extraíble','Compartimento de apertura por botón, 21,9 kg y aplicación Bluetooth. El '
  'baúl admite un segundo pack y duplicas la ruta.'),
 ('Frenada regenerativa','Recupera energía en cada deceleración y en cada bajada larga, y '
  'reduce el desgaste de pastillas.'),
 ('Marcha atrás','Parece un detalle hasta que estás encajado en una vereda con 130 kilos de '
  'moto y pendiente en contra.'),
 ('Homologación EEC/COC','Certificado europeo y matriculación española con etiqueta CERO en los '
  'modelos de carretera.'),
 ('Carga Type 2','El mismo conector que un coche eléctrico, más cargadores externos opcionales '
  'de 12, 22 y 30 A.'),
]

# ══════════════════════════════════════════════════ PORTADA
destacados = ''
for k in ORDEN[:3]:
    m = M[k]
    destacados += f"""
    <article class="panel">
      <div>
        <h3><a href="{k}.html">{m['n']} {m['s']}</a></h3>
        <p class="rol">{m['rol']}</p>
        <p class="txt">{m['txt']}</p>
        {medidas(m['med'])}
        <div class="pie-precio">
          <span class="precio">Desde <span class="pendiente">precio pendiente</span></span>
          <a class="btn btn-s" href="{k}.html">Ficha completa</a>
        </div>
      </div>
      {visor(k)}
    </article>"""

pag('index.html',
 'Velimotor España · El enduro ya es eléctrico',
 'Motos de enduro, cross y trail 100% eléctricas homologadas para España. Par máximo desde cero '
 'revoluciones, carga Type 2, celdas Farasis y estanqueidad IP67.',
 f"""
<section class="hero">
  <div class="hero-foto"><img src="{FOTO['hero']}" alt="" aria-hidden="true"></div>
  <div class="reticula" style="opacity:.5"></div>
  <div class="env">
    <div>
      <span class="pastilla ent">Homologada L3e</span>
      <h1 class="ent"><em>El enduro</em><em class="hueca">ya no</em><em>espera</em><em>vueltas</em></h1>
      <p class="bajada ent">Un motor de combustión necesita subir de régimen para dar su par. El
        eléctrico lo entrega <b>completo desde parado</b>. Sin embrague, sin cambio y sin calarse
        en una rampa de piedra a la primera.</p>
      <div class="acc ent">
        <a class="btn btn-p" href="contacto.html">Reservar una prueba</a>
        <a class="btn btn-s" href="modelos.html">Ver la gama</a>
      </div>
    </div>
    {GRAFICO}
  </div>
  <div class="env"><div class="rail"><div class="rail-in">
    <div><b>480 N·m</b><small>Par máximo</small></div>
    <div><b>25 kW</b><small>Potencia máxima</small></div>
    <div><b>180 km</b><small>Autonomía</small></div>
    <div><b>1,5 h</b><small>Carga rápida</small></div>
  </div></div></div>
</section>

<section class="sec">
  <div class="reticula" style="opacity:.25"></div>
  <div class="env">
    <div class="sec-cab">
      <h2>Ya no es la moto del futuro</h2>
      <p>Durante años el enduro eléctrico fue una promesa con media hora de autonomía. Eso se
        acabó. Hoy la conversación es otra: qué puedes hacer con una eléctrica que con una de
        gasolina ya no puedes.</p>
    </div>
    <div class="args args-2">{''.join('<div class="arg"><span class="arg-num">%s</span><h3>%s</h3><p>%s</p></div>' % a for a in ARGS)}</div>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="sec-cab"><h2>La gama</h2>
      <p>Siete vehículos, de la trail homologada para carretera al UTV de trabajo. Una se
        matricula; el resto son de campo puro y no necesitan trámites.</p></div>
    {destacados}
    <div class="acc"><a class="btn btn-p" href="modelos.html">Ver los siete modelos</a></div>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="sec-cab"><h2>Lo que hay dentro</h2>
      <p>La diferencia entre una eléctrica seria y una eléctrica barata no se ve en la ficha de
        potencia. Se ve aquí.</p></div>
    <div class="tec">{''.join('<article><h3>%s</h3><p>%s</p></article>' % t for t in TEC[:6])}</div>
    <div class="acc"><a class="btn btn-s" href="tecnologia.html">Ver la tecnología</a></div>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="sec-cab"><h2>Lo que te ahorras cada año</h2>
      <p>Mueve los kilómetros que haces al año y compáralo con una moto de campo de gasolina
        equivalente.</p></div>
    <div class="calc">
      <div>
        <label for="km">Kilómetros al año</label>
        <div class="km"><span id="km-valor">5.000</span> km</div>
        <input type="range" id="km" min="1000" max="20000" step="500" value="5000" aria-describedby="sup">
      </div>
      <div class="resultado">
        <div class="ahorro"><span>€</span><span id="ahorro">390</span></div>
        <p style="margin:14px 0 0">de ahorro en combustible al año, solo en energía.</p>
        <p id="sup" class="supuestos">Cálculo con una moto de campo de 5 l/100 km a 1,65 €/l
          frente a 3 kWh/100 km a 0,15 €/kWh. No incluye el ahorro en aceite, filtros, bujías
          ni puestas a punto.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="cols">
      <div>
        <h3>Empresas y administraciones</h3>
        <p>Donde el ruido, el humo y el mantenimiento son un coste directo, una flota eléctrica se
          amortiza sola. Ayuntamientos, fincas, campos de golf y seguridad privada.</p>
        <a class="btn btn-s" href="empresas.html">Ver flotas</a>
      </div>
      <div>
        <h3>Quiero ser distribuidor</h3>
        <p>Estamos abriendo puntos de venta por provincias. Buscamos concesionarios y tiendas
          especializadas con taller propio y capacidad real de posventa.</p>
        <a class="btn btn-s" href="puntos-de-venta.html#distribuidor">Ver condiciones</a>
      </div>
    </div>
  </div>
</section>

{cierre('Esto no se compra leyendo',
 'Súbete. La primera vez que abres gas desde parado y no pasa nada de lo que esperabas, la '
 'conversación se acaba sola.')}
""", extra="""
<script>
(function(){
  var r=document.getElementById('km'); if(!r) return;
  var vk=document.getElementById('km-valor'), va=document.getElementById('ahorro');
  function up(){var km=Number(r.value);
    vk.textContent=km.toLocaleString('es-ES');
    va.textContent=Math.round(km/100*5*1.65 - km/100*3*0.15).toLocaleString('es-ES');}
  r.addEventListener('input',up); up();
})();
</script>
""")

# ══════════════════════════════════════════════════ ÍNDICE DE MODELOS
filas = ''
for k in ORDEN:
    m = M[k]
    filas += f"""
    <article class="panel" data-cat="{m['cat']}">
      <div>
        <h3><a href="{k}.html">{m['n']} {m['s']}</a></h3>
        <p class="rol">{m['rol']}</p>
        <p class="txt">{m['txt']}</p>
        {medidas(m['med'])}
        <div class="pie-precio">
          <span class="precio">Desde <span class="pendiente">precio pendiente</span></span>
          <a class="btn btn-s" href="{k}.html">Ficha completa</a>
        </div>
      </div>
      {visor(k)}
    </article>"""

pag('modelos.html', 'La gama Velimotor, siete modelos eléctricos | Velimotor España',
 'Trail homologada, enduro, motocross, dirtbike, infantil y UTV. Especificaciones de los siete '
 'vehículos eléctricos Velimotor disponibles en España.',
 f"""
<section class="cabecera">
  <div class="env">
    <h1>La gama</h1>
    <p class="bajada">Siete vehículos que juegan en cuatro mercados distintos. Uno se matricula y
      se conduce con el carné B; el resto son de recinto privado y no necesitan trámites.</p>
  </div>
</section>
<section class="sec">
  <div class="env">
    <div class="filtros" role="group" aria-label="Filtrar por tipo">
      <button data-cat="todos" aria-pressed="true">Todos</button>
      <button data-cat="trail" aria-pressed="false">Trail</button>
      <button data-cat="cross" aria-pressed="false">Enduro y cross</button>
      <button data-cat="infantil" aria-pressed="false">Infantil</button>
      <button data-cat="utv" aria-pressed="false">UTV</button>
    </div>
    <div id="lista">{filas}</div>
  </div>
</section>
{cierre('Pruébala antes de decidir',
 'Esta categoría no se vende con una ficha técnica. Dinos tu provincia y organizamos una prueba '
 'con la unidad de demostración.')}
""", act='modelos.html', extra="""
<script>
(function(){
  var bs=document.querySelectorAll('.filtros button'), ms=document.querySelectorAll('#lista .panel');
  bs.forEach(function(b){b.addEventListener('click',function(){
    var c=b.dataset.cat;
    bs.forEach(function(o){o.setAttribute('aria-pressed',String(o===b));});
    ms.forEach(function(m){m.hidden=!(c==='todos'||m.dataset.cat===c);});
  });});
})();
</script>
""")

# ══════════════════════════════════════════════════ FICHAS
for k in ORDEN:
    m = M[k]
    otros = ''.join('<li><a href="%s.html">%s %s</a></li>' % (x, M[x]['n'], M[x]['s'])
                    for x in ORDEN if x != k)
    por = ''.join('<div class="arg"><h3>%s</h3><p>%s</p></div>' % p for p in m['por'])
    tabla = ''.join('<tr><th scope="row">%s</th><td>%s</td></tr>' % f for f in m['ficha'])
    aviso = ('' if k == 'vmx10s' else
      '<p class="legal">Ficha en ampliación. Los datos completos de este modelo están pendientes '
      'de recibir del fabricante.</p>')
    pag(f'{k}.html', f"{m['n']} {m['s']}, {m['rol'].lower()} | Velimotor España",
     f"{m['n']} {m['s']}. {m['gancho']}. {m['txt'][:100]}",
     f"""
<section class="cabecera">
  <div class="env">
    <p class="miga"><a href="index.html">Inicio</a> / <a href="modelos.html">Modelos</a> / {m['n']} {m['s']}</p>
    <h1>{m['n']} {m['s']}</h1>
    <p class="rol">{m['rol']}</p>
    <p class="bajada">{m['gancho']}. {m['txt']}</p>
    <div class="acc">
      <a class="btn btn-p" href="contacto.html">Reservar una prueba</a>
      <a class="btn btn-s" href="financiacion.html">Financiación y ayudas</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="con-foto">
      <div>{medidas(m['med'])}
        <div class="pie-precio"><span class="precio">Desde <span class="pendiente">precio pendiente</span></span></div>
      </div>
      {visor(k)}
    </div>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="sec-cab"><h2>Por qué esta</h2></div>
    <div class="args">{por}</div>
  </div>
</section>

<section class="sec">
  <div class="env">
    <table class="ficha"><caption>Ficha técnica</caption><tbody>{tabla}</tbody></table>
    {aviso}
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="cols">
      <div><h3>Otros modelos</h3><ul>{otros}</ul>
        <a class="btn btn-s" href="modelos.html">Ver la gama completa</a></div>
      <div><h3>Pruébala</h3>
        <p>Dinos tu provincia y te avisamos cuando tengamos una unidad de demostración cerca.</p>
        <a class="btn btn-p" href="contacto.html">Reservar una prueba</a></div>
    </div>
  </div>
</section>
""", act='modelos.html')

# ══════════════════════════════════════════════════ TECNOLOGÍA
pag('tecnologia.html', 'Tecnología de las motos eléctricas Velimotor | Velimotor España',
 'Celdas Farasis, estanqueidad IP67, controlador vectorial CAN, carga Type 2 y batería '
 'extraíble. Lo que separa una eléctrica seria de una barata.',
 f"""
<section class="cabecera">
  <div class="env">
    <h1>Lo que hay dentro</h1>
    <p class="bajada">La diferencia entre una eléctrica seria y una eléctrica barata no se ve en
      la ficha de potencia. Cualquiera pone un número grande de kilovatios. Se ve en la celda, en
      la estanqueidad y en cómo entrega el par.</p>
  </div>
</section>
<section class="sec">
  <div class="env">
    <div class="tec">{''.join('<article><h3>%s</h3><p>%s</p></article>' % t for t in TEC)}</div>
  </div>
</section>
<section class="sec">
  <div class="env">
    <div class="sec-cab"><h2>El par, en un gráfico</h2>
      <p>Es el argumento entero. Un motor de combustión tiene que subir de vueltas para dar lo
        que tiene; el eléctrico lo da desde el primer grado de gas.</p></div>
    <div style="max-width:640px">{GRAFICO}</div>
  </div>
</section>
{cierre('El par no se explica, se nota',
 'Una vuelta de cinco minutos convence más que cualquier gráfico de esta página.')}
""", act='tecnologia.html')

# ══════════════════════════════════════════════════ FINANCIACIÓN
pag('financiacion.html', 'Financiación y ayudas del Programa Auto+ | Velimotor España',
 'Financiación para comprar una moto eléctrica Velimotor en España y ayudas públicas del '
 'Programa Auto+ para los modelos homologados.',
 f"""
<section class="cabecera">
  <div class="env">
    <h1>Financiación y ayudas</h1>
    <p class="bajada">Son dos vías distintas y conviene no confundirlas: la financiación del
      precio y la subvención pública. La segunda solo aplica a los modelos que se matriculan.</p>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="sec-cab"><h2>Financiación</h2>
      <p>Compra a plazos para particulares, autónomos y empresas.</p></div>
    <div class="cols">
      <div><h3>Particulares</h3>
        <ul>
          <li>Entrada: <span class="pendiente">pendiente</span></li>
          <li>Plazos: <span class="pendiente">pendiente</span></li>
          <li>TAE: <span class="pendiente">pendiente</span></li>
        </ul>
        <p>Respuesta habitual en 24 o 48 horas con la documentación completa.</p></div>
      <div><h3>Autónomos y empresas</h3>
        <ul>
          <li>Renting y leasing: <span class="pendiente">pendiente</span></li>
          <li>Cuota mensual desde: <span class="pendiente">pendiente</span></li>
          <li>IVA deducible según la actividad</li>
        </ul>
        <p>Para flotas de más de cinco unidades hacemos presupuesto cerrado.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="sec-cab"><h2>El Programa Auto+</h2>
      <p>El plan estatal de ayudas a la compra de vehículos eléctricos, en vigor hasta el 31 de
        diciembre de 2030 con convocatorias anuales.</p></div>
    <div class="args">
      <div class="arg"><h3>Cuánto es</h3>
        <p>La ayuda máxima para motocicletas es de 1.100 €, y puede llegar a 2.000 € si la
          convocatoria se cofinancia con el Fondo Social para el Clima. La cuantía no es fija:
          se calcula con un sistema de puntuación que valora el nivel de electrificación, el
          precio y el origen europeo de fabricación del vehículo y de su batería.</p></div>
      <div class="arg"><h3>Qué modelos entran</h3>
        <p>Solo los que se matriculan y obtienen etiqueta CERO. En nuestra gama, la
          <a href="vmx10s.html">VMX 10S homologada</a>. Los modelos de recinto privado no se
          matriculan y por tanto no acceden a la ayuda, igual que ningún competidor equivalente,
          así que la comparación entre ellos es directa.</p></div>
      <div class="arg"><h3>Cómo se tramita</h3>
        <p>Hacen falta la ficha técnica y el permiso de circulación definitivos; la normativa
          rechaza documentos provisionales. El punto de venta puede actuar como representante del
          comprador con una simple autorización, así que lo tramitamos nosotros.</p></div>
    </div>
    <p class="legal">Cuantías y requisitos según el Real Decreto 609/2026. El importe exacto
      aplicable a cada modelo se confirma en el momento de la compra, según la convocatoria
      vigente.</p>
  </div>
</section>
{cierre('Dinos tu caso y te lo desglosamos',
 'Modelo, si compras como particular o como empresa, y tu provincia. Te mandamos la ayuda que te '
 'corresponde y la cuota.')}
""", act='financiacion.html')

# ══════════════════════════════════════════════════ PUNTOS DE VENTA
pag('puntos-de-venta.html', 'Puntos de venta y red de distribuidores | Velimotor España',
 'Dónde probar y comprar una Velimotor en España, y condiciones para entrar en la red de '
 'distribuidores oficiales por provincia.',
 f"""
<section class="cabecera">
  <div class="env">
    <h1>Puntos de venta</h1>
    <p class="bajada">Estamos construyendo la red por provincias. Si en tu zona todavía no hay
      punto de venta, escríbenos: te avisamos cuando abramos y organizamos una prueba con la
      unidad de demostración.</p>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="vacio">
      <h3>La red está en construcción</h3>
      <p>Todavía no hay puntos de venta publicados. Dinos tu provincia y te ponemos en la lista
        de aviso, o te atendemos directamente mientras tanto.</p>
      <div class="acc"><a class="btn btn-p" href="contacto.html">Dinos tu provincia</a></div>
    </div>
  </div>
</section>

<section class="sec" id="distribuidor">
  <div class="env">
    <div class="sec-cab"><h2>Ser distribuidor</h2>
      <p>Buscamos concesionarios, talleres y tiendas especializadas con taller propio y capacidad
        real de posventa. Tres niveles, según lo que quieras asumir.</p></div>
    <div class="args">
      <div class="arg"><h3>Distribuidor Master</h3>
        <p>Exclusividad por comunidad autónoma, compra en firme, stock mínimo de quince unidades
          y obligación de dar servicio a los puntos de su zona. Margen del 30 al 35 %.</p></div>
      <div class="arg"><h3>Punto de Venta Oficial</h3>
        <p>Stock mínimo de tres unidades más una de demostración, sin exclusividad. Margen del 22
          al 25 % y formación técnica de dos días incluida.</p></div>
      <div class="arg"><h3>Punto de Prueba</h3>
        <p>Para circuitos, escuelas off-road, empresas de rutas y hoteles rurales. No compras
          stock: tienes motos en depósito y cobras del 8 al 10 % por venta referida.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="sec-cab"><h2>Qué te damos</h2></div>
    <div class="tec">
      <article><h3>Zona</h3><p>Exclusividad territorial por escrito, con radio definido en
        kilómetros. Sin sorpresas a treinta minutos de tu puerta.</p></article>
      <article><h3>Recambio</h3><p>Stock en España con plazo de entrega comprometido, no pedidos
        a China cada vez que se rompe una pieza.</p></article>
      <article><h3>Formación</h3><p>Dos días de formación técnica y acceso directo al soporte del
        importador, no a un formulario.</p></article>
      <article><h3>Demostración</h3><p>Unidad de demostración para pruebas, que es exactamente
        como se cierra esta venta.</p></article>
    </div>
    <div class="acc"><a class="btn btn-p" href="contacto.html">Hablar con nosotros</a></div>
  </div>
</section>
""", act='puntos-de-venta.html')

# ══════════════════════════════════════════════════ EMPRESAS
pag('empresas.html', 'Flotas para empresas y administraciones | Velimotor España',
 'Vehículos eléctricos de trabajo para ayuntamientos, explotaciones agrícolas, campos de golf y '
 'seguridad privada. Presupuesto cerrado para flotas.',
 f"""
<section class="cabecera">
  <div class="env">
    <h1>Empresas y administraciones</h1>
    <p class="bajada">Donde el ruido, el humo y el mantenimiento son un coste operativo y no una
      preferencia, una flota eléctrica se amortiza sola.</p>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="sec-cab"><h2>Dónde funciona</h2></div>
    <div class="cols">
      <div><h3>Administración pública</h3><ul>
        <li>Vigilancia de parques, playas y polígonos</li>
        <li>Servicios municipales en casco histórico</li>
        <li>Protección civil y accesos forestales</li></ul></div>
      <div><h3>Sector agrícola</h3><ul>
        <li>Fincas y explotaciones extensivas</li>
        <li>Invernaderos y naves, sin emisiones en interior</li>
        <li>Control de riego y perímetros</li></ul></div>
      <div><h3>Turismo y ocio</h3><ul>
        <li>Campos de golf y resorts</li>
        <li>Hoteles rurales y rutas guiadas</li>
        <li>Escuelas de conducción off-road</li></ul></div>
      <div><h3>Seguridad privada</h3><ul>
        <li>Grandes recintos y campus</li>
        <li>Rondas nocturnas sin generar ruido</li>
        <li>Plantas industriales y logísticas</li></ul></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="con-foto">
      <div class="sec-cab" style="margin-bottom:0">
        <h2>El UTV de trabajo</h2>
        <p>El <a href="vl5000-utv.html">VL 5000</a> es el vehículo de flota de la gama: 120 km de
          autonomía, 60 km/h y cero emisiones locales, así que entra en naves e invernaderos donde
          un motor de combustión no puede trabajar.</p>
      </div>
      {visor('vl5000-utv')}
    </div>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="sec-cab"><h2>Cómo trabajamos una flota</h2></div>
    <div class="args">
      <div class="arg"><span class="arg-num">01</span><h3>Prueba en tus instalaciones</h3>
        <p>Llevamos una unidad a tu finca, recinto o dependencia municipal y la usáis en
          condiciones reales durante unos días. Sin compromiso.</p></div>
      <div class="arg"><span class="arg-num">02</span><h3>Presupuesto cerrado</h3>
        <p>A partir de cinco unidades trabajamos precio de flota, con formación al personal y
          plan de mantenimiento incluido.</p></div>
      <div class="arg"><span class="arg-num">03</span><h3>Licitación pública</h3>
        <p>Preparamos la documentación técnica que exige un pliego: homologaciones, fichas,
          certificados y declaraciones responsables.</p></div>
    </div>
    <div class="acc"><a class="btn btn-p" href="contacto.html">Pedir propuesta de flota</a></div>
  </div>
</section>
""", act='empresas.html')

# ══════════════════════════════════════════════════ NOSOTROS
pag('nosotros.html', 'Quiénes somos | Velimotor España',
 'Velimotor España es la estructura de importación, homologación y distribución de la marca '
 'Velimotor en el mercado español.',
 f"""
<section class="cabecera">
  <div class="env">
    <h1>Quiénes somos</h1>
    <p class="bajada">La estructura comercial de Velimotor en España: importación, homologación,
      red de venta y posventa.</p>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="con-foto">
      <div>
        <div class="args" style="grid-template-columns:1fr">
          <div class="arg"><h3>La marca</h3>
            <p>Velimotor es la marca de vehículos eléctricos de Veli Technology Industrial,
              fabricante especializado en dos y cuatro ruedas eléctricas, con gama homologada
              según normativa europea EEC/COC.</p></div>
          <div class="arg"><h3>Nuestro papel</h3>
            <p>Nosotros no fabricamos. Hacemos lo que a un fabricante a diez mil kilómetros le
              resulta imposible: tener el recambio en España, responder al teléfono en tu mismo
              horario y estar delante cuando hay que reparar algo. Es la parte donde las marcas
              importadas suelen fallar.</p></div>
          <div class="arg"><h3>Lo que nos importa</h3>
            <p>Que el recambio llegue en plazo. Que la garantía de batería esté por escrito y se
              cumpla. Y que puedas probar la moto antes de gastarte el dinero, porque esta
              categoría no se vende con un folleto.</p></div>
        </div>
      </div>
      <img src="{FOTO['marca']}" alt="Velimotor" loading="lazy">
    </div>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="cols">
      <div><h3>Datos de la empresa</h3><ul>
        <li>Razón social: <span class="pendiente">pendiente</span></li>
        <li>CIF: <span class="pendiente">pendiente</span></li>
        <li>Domicilio: <span class="pendiente">pendiente</span></li></ul></div>
      <div><h3>Contacto directo</h3>
        <p>Sin formularios de por medio si no quieres.</p>
        <div class="directo">
          <a href="tel:{TEL_U}">+34 {TEL_T}</a>
          <a href="mailto:{MAIL}">{MAIL}</a>
        </div></div>
    </div>
  </div>
</section>
""", act='nosotros.html')

# ══════════════════════════════════════════════════ CONTACTO
pag('contacto.html', 'Contacto y reserva de pruebas | Velimotor España',
 'Reserva una prueba, pide precio o infórmate sobre flotas y distribución de motos eléctricas '
 'Velimotor en España.',
 f"""
<section class="cabecera">
  <div class="env">
    <h1>Habla con nosotros</h1>
    <p class="bajada">Respondemos el mismo día laborable. Si prefieres el teléfono, mejor
      todavía.</p>
  </div>
</section>

<section class="sec">
  <div class="env">
    <div class="contacto">
      <div>
        <div class="directo">
          <a href="tel:{TEL_U}">+34 {TEL_T}</a>
          <a href="mailto:{MAIL}">{MAIL}</a>
        </div>
        <p style="color:var(--niebla);margin-top:26px">Si escribes para reservar una prueba, dinos
          tu provincia. Estamos montando la red y organizamos las demostraciones por zonas, así
          que saber dónde estás nos ayuda a llegar antes.</p>
      </div>
      <form id="form" novalidate>
        <div class="dos">
          <div class="campo"><label for="nombre">Nombre y apellidos</label>
            <input id="nombre" name="nombre" type="text" autocomplete="name" required></div>
          <div class="campo"><label for="telefono">Teléfono</label>
            <input id="telefono" name="telefono" type="tel" autocomplete="tel" required></div>
        </div>
        <div class="dos">
          <div class="campo"><label for="email">Correo electrónico</label>
            <input id="email" name="email" type="email" autocomplete="email" required></div>
          <div class="campo"><label for="provincia">Provincia</label>
            <input id="provincia" name="provincia" type="text" autocomplete="address-level2"></div>
        </div>
        <div class="dos">
          <div class="campo"><label for="interes">Me interesa</label>
            <select id="interes" name="interes">
              <option>Reservar una prueba</option><option>Comprar una moto</option>
              <option>Financiación y ayudas</option>
              <option>Flota para empresa o ayuntamiento</option>
              <option>Ser distribuidor</option>
            </select></div>
          <div class="campo"><label for="modelo">Modelo</label>
            <select id="modelo" name="modelo">
              <option>Todavía no lo sé</option>
              {''.join('<option>%s %s</option>' % (M[k]['n'], M[k]['s']) for k in ORDEN)}
            </select></div>
        </div>
        <div class="campo"><label for="mensaje">Cuéntanos qué necesitas</label>
          <textarea id="mensaje" name="mensaje" rows="4"></textarea></div>
        <button class="btn btn-p" type="submit">Enviar</button>
        <p class="legal">Al enviar aceptas la <a href="privacidad.html">política de
          privacidad</a>. Usaremos tus datos solo para responderte sobre esta consulta.</p>
        <p id="aviso" class="legal" role="status" style="color:var(--cian)"></p>
      </form>
    </div>
  </div>
</section>
""", act='contacto.html', extra="""
<script>
(function(){
  var f=document.getElementById('form'); if(!f) return;
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var a=document.getElementById('aviso');
    var falta=['nombre','telefono','email'].filter(function(i){
      return !document.getElementById(i).value.trim();});
    if(falta.length){
      a.textContent='Faltan por rellenar: nombre, teléfono y correo.';
      document.getElementById(falta[0]).focus(); return;}
    a.textContent='Formulario listo. Falta conectarlo al CRM o al servicio de correo.';
  });
})();
</script>
""")

# ══════════════════════════════════════════════════ LEGALES
BOR = ('<p class="borrador">Borrador. Este texto está redactado como base y contiene datos '
       'pendientes de completar. Debe revisarlo un abogado o una gestoría antes de publicar.</p>')

pag('aviso-legal.html', 'Aviso legal | Velimotor España',
 'Información legal de Velimotor España conforme a la Ley 34/2002 de servicios de la sociedad de '
 'la información.',
 f"""
<section class="cabecera"><div class="env"><h1>Aviso legal</h1></div></section>
<section class="sec"><div class="env"><div class="legalidad">
{BOR}
<h2>Datos del titular</h2>
<p>En cumplimiento del artículo 10 de la Ley 34/2002, de servicios de la sociedad de la
  información y de comercio electrónico, se informa de los siguientes datos:</p>
<ul>
  <li>Razón social: <span class="pendiente">pendiente</span></li>
  <li>CIF: <span class="pendiente">pendiente</span></li>
  <li>Domicilio social: <span class="pendiente">pendiente</span></li>
  <li>Datos de inscripción registral: <span class="pendiente">pendiente</span></li>
  <li>Correo electrónico: {MAIL}</li>
  <li>Teléfono: +34 {TEL_T}</li>
</ul>
<h2>Objeto</h2>
<p>Este sitio informa sobre los vehículos eléctricos de la marca Velimotor comercializados en
  España y facilita el contacto comercial con clientes particulares, empresas y posibles
  distribuidores.</p>
<h2>Condiciones de uso</h2>
<p>El acceso a este sitio implica la aceptación de estas condiciones. El usuario se compromete a
  hacer un uso lícito del sitio y a no realizar acciones que puedan dañar su funcionamiento.</p>
<h2>Propiedad intelectual e industrial</h2>
<p>Los contenidos de este sitio, incluidos textos, imágenes, diseño y código, están protegidos
  por la normativa de propiedad intelectual. La marca Velimotor y las denominaciones de sus
  modelos son titularidad del fabricante y se utilizan aquí en el marco de la relación de
  distribución.</p>
<h2>Información sobre los productos</h2>
<p>Las especificaciones publicadas provienen de la documentación del fabricante y pueden variar
  sin previo aviso. Los datos de autonomía se obtienen en condiciones de ensayo y varían según la
  conducción, la carga, el terreno y la temperatura. Las imágenes pueden mostrar equipamiento
  opcional.</p>
<p>La homologación y el permiso de conducción requerido dependen de la versión concreta del
  vehículo. Consúltanos antes de comprar si el tipo de carné es determinante para ti.</p>
<h2>Responsabilidad</h2>
<p>No se garantiza la ausencia de errores en los contenidos ni la disponibilidad continua del
  sitio. Se excluye la responsabilidad por los daños derivados del uso de la información
  publicada, en los términos permitidos por la ley.</p>
<h2>Enlaces a terceros</h2>
<p>Este sitio puede contener enlaces a páginas de terceros. No asumimos responsabilidad sobre sus
  contenidos ni sobre sus políticas de privacidad.</p>
<h2>Legislación aplicable</h2>
<p>Estas condiciones se rigen por la legislación española. Para cualquier controversia serán
  competentes los juzgados y tribunales del domicilio del titular, salvo que la normativa de
  consumo establezca otro fuero.</p>
</div></div></section>
""")

pag('privacidad.html', 'Política de privacidad | Velimotor España',
 'Cómo trata Velimotor España los datos personales recogidos en este sitio web, conforme al '
 'Reglamento General de Protección de Datos.',
 f"""
<section class="cabecera"><div class="env"><h1>Política de privacidad</h1></div></section>
<section class="sec"><div class="env"><div class="legalidad">
{BOR}
<h2>Responsable del tratamiento</h2>
<ul>
  <li>Razón social: <span class="pendiente">pendiente</span></li>
  <li>CIF: <span class="pendiente">pendiente</span></li>
  <li>Domicilio: <span class="pendiente">pendiente</span></li>
  <li>Correo de contacto: {MAIL}</li>
</ul>
<h2>Qué datos recogemos</h2>
<p>Los que nos facilitas en el formulario: nombre y apellidos, teléfono, correo electrónico,
  provincia, modelo de interés y el contenido de tu mensaje. También los que nos das si nos
  escribes o llamas directamente.</p>
<h2>Para qué los usamos</h2>
<ul>
  <li>Responder a tu consulta y darte la información que pides</li>
  <li>Organizar una prueba y avisarte cuando haya una unidad en tu zona</li>
  <li>Elaborar presupuestos y, si procede, tramitar la financiación o las ayudas públicas</li>
  <li>Gestionar la relación comercial si acabas siendo cliente o distribuidor</li>
</ul>
<p>No usamos tus datos para enviarte comunicaciones comerciales de otros productos salvo que nos
  des tu consentimiento expreso.</p>
<h2>Base jurídica</h2>
<p>El tratamiento se basa en tu consentimiento al enviarnos el formulario y en la ejecución de la
  relación contractual o precontractual cuando pides un presupuesto o contratas.</p>
<h2>Cuánto tiempo los guardamos</h2>
<p>Conservamos los datos mientras dure la relación comercial y, después, durante los plazos de
  prescripción legal aplicables. Si tu consulta no deriva en relación comercial, los eliminamos
  cuando ya no sean necesarios para atenderla.</p>
<h2>Con quién los compartimos</h2>
<p>Podemos comunicarlos a un punto de venta de nuestra red cercano a tu provincia cuando sea
  necesario para atender tu solicitud o organizar una prueba. También a entidades financieras si
  pides financiación, y a la administración competente si tramitas una ayuda pública.</p>
<p>Utilizamos proveedores de alojamiento web y de correo que actúan como encargados del
  tratamiento. No cedemos datos a terceros con fines publicitarios.</p>
<h2>Tus derechos</h2>
<p>Puedes solicitar el acceso, la rectificación o la supresión de tus datos, la limitación u
  oposición a su tratamiento y la portabilidad, escribiendo a {MAIL}. Si consideras que no hemos
  atendido correctamente tu solicitud, puedes reclamar ante la Agencia Española de Protección de
  Datos.</p>
<h2>Seguridad</h2>
<p>Aplicamos medidas técnicas y organizativas razonables para proteger tus datos. El sitio
  utiliza conexión cifrada mediante certificado TLS.</p>
</div></div></section>
""")

pag('cookies.html', 'Política de cookies | Velimotor España',
 'Qué cookies utiliza el sitio web de Velimotor España y cómo puedes gestionarlas.',
 f"""
<section class="cabecera"><div class="env"><h1>Política de cookies</h1></div></section>
<section class="sec"><div class="env"><div class="legalidad">
{BOR}
<h2>Qué es una cookie</h2>
<p>Un archivo pequeño que un sitio web guarda en tu dispositivo para recordar información sobre
  tu visita. Algunas son imprescindibles para que la página funcione y otras sirven para medir el
  uso del sitio o para publicidad.</p>
<h2>Qué cookies usa este sitio</h2>
<p>En su estado actual, este sitio no instala cookies de análisis ni de publicidad. Solo se
  utilizan las cookies técnicas necesarias para servir la página y mantener la conexión segura.</p>
<p>Se cargan tipografías desde Google Fonts, lo que implica una conexión a servidores de Google
  que puede registrar tu dirección IP. Si se incorpora una herramienta de análisis o el píxel de
  una red social, esta política se actualizará y se activará un banner de consentimiento previo.</p>
<h2>Cómo gestionarlas</h2>
<p>Puedes configurar o eliminar las cookies desde los ajustes de tu navegador. Cada navegador
  tiene su propio procedimiento, disponible en su sección de ayuda. Bloquear las cookies técnicas
  puede impedir el funcionamiento correcto del sitio.</p>
<h2>Actualizaciones</h2>
<p>Esta política puede modificarse si cambian las herramientas del sitio o la normativa
  aplicable. La versión vigente es siempre la publicada en esta página.</p>
</div></div></section>
""")

print('Generado en', S)
for f in sorted(S.glob('*')):
    print('  %-24s %6d B' % (f.name, f.stat().st_size))
