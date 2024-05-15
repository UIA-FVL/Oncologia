# corpus de topografías

# * primarios
primario_keys = [
    "Mama",
    "Genitales femeninos",
    "Genitales masculinos",
    "Órganos digestivos",
    "Pulmón",
    "Sistema respiratorio",
    "Corazón et al",
    "Hematopoyético",
    "Encéfalo",
    "Tracto urinario",
    "Tiroides y otras glándulas",
    "Peritoneo",
    "Sistema nervioso central",
    "Ojo",
    "Hueso",
    "Piel",
    "Boca y faringe",
    "Ganglio linfático",
    "Nervios",
    "Tejido conjuntivo",
    "Mal definido",
]


primario_C00_C14 = r"""
labi(o|al|i)
l[ei]ngual?
encía|gingiva
paladar|úvula
bucal|boca
\boral
parótida|Stensen
saliva|Wharton
am[íi]gdal(a|iana)
far[ií]ngea?|Rosenmüller|epigl[oó]ti(s|co)
piriforme
garganta
anillo de Waldeyer
"""

primario_C15_C26 = r"""
es[óo]f[aá]g(o|ico)
estómago|gástric(o|a)
intestin(o|al)
duodeno|yeyuno|íleon|Meckel
colon
rect(o|al)
\ban(o|al)
h[íi]gado|hep[aá]t\w+
Oddi|Vater
p[áa]ncre[aá](tico|s)|Santorini|Wirsung|Langerhans
tracto intestin(o|al)
"""

primario_C30_C33 = r"""
na(sal|riz)
oído|auditivo
senos? (para)?nasal(es)?
lar[ií]ngea?|gl[oó]tis?
(cuerda|pliegue) vocal
tr[áa]queal?
respiratori(o|a)s?
"""
primario_C34_pulmon = r"""
pulm[óo]n(ar)?|neumo\w+
bronquio(lo)?
broncogénico
carina
"""
primario_C37_C38 = r"""
timo
corazón|card[ií](o|ac[oa])
mediastino
pleura
"""

primario_C40_C41 = r"""
hueso
articulación
cartílago articular
esqueleto
acromioclavicular
cintura escapular
cúbito
húmero
radio
escápula
tarso
metatarsiano
rótula
falange
carpiano
metacarpiano
fémur
peroné
tibia
menisco
semilunar
calvario
cráneo
cráneo
cigomático
esfenoides
etmoides
hioides
(temporo)?mand[íi]bular?
maxilar
v[ée]rtebral?
espinal?
atlas
axis
núcleo pulposo
clavícula
esternón
costilla
costovertebral
esternocostal
costal
acetábulo
cóccix
isquión
íleon
sacro
sínfisis del pubis
"""


primario_C42_hemato = r"""
hematopoyético
m[ée]dula [óo]sea
reticuloendotelial
bazo
sangre
leu[ck]emia
"""

primario_C44_piel = r"""
piel
párpado
palpebral
Meibomio
meato
cerumen
hélix
ala nasal
columela
ceja
mejilla
mentón
nariz
sien
cuero cabelludo
ombligo
perianal
"""

primario_C47_nervios = r"""
nervios periféricos
"""

primario_C48_peritoneo = r"""
peritoneo
peritoneal
retroperitoneo
periadrenal
perinéfrico
peripancreático
perirrenal
retrocecal
retroperitoneal
epiplón
mesenterio
mesoapéndice
mesocolon
omento
Douglas
"""

primario_C49_tejidos = r"""
aponeurosis
arteria
fascia
ligamento
m[úu]scul(o|ar)
sinovia
tejido adiposo
tejido conjuntivo
tejido fibroso
tejido subcutáneo
tendón
vaina tendinosa
vaso sanguíneo
vena
"""

primario_C50_mama = r"""
mama(ri[ao])?
pezón
aréola
"""

primario_C51_C58 = r"""
vulvar?
clítoris
labios
Bartholin
vaginal?
Gartner
fórnix
himen
[úu]ter(in)?os?
cérvix
Naboth
escamocolumnar
ovario
trompas
falopio
mesoovario
paraovárica
endometrio
endometrial
miometrio
parametrio
uterosacro
tuboováricos
uteroováricos
Wolffian
uretrovaginal
vesicovaginal
vesicocervical
placenta
fetales
"""

primario_C60_C63 = r"""
pene
prepucio
glande
pr[óo]st[áa]t(ic)?(a|o)
test[ií]culo
escrotal?
ectópico
genitourinario
seminal
espermático
epidídimo
"""

primario_C64_C68 = r"""
riñ[óo]n
renal(es)?
parénquima
pelviureteral
urinaria
uréter
uretral?
uraco
vesical
"""

primario_C69_ojo = r"""
\bojo
ocular
intraocular
extraocular
conjuntiva
córnea
retina
ciliar
esclerótica
iris
uveal
la[cg]rimal
nasola[cg]rimal
retrobulbar
"""

primario_C70_C71 = r"""
mening(ioma|es)
aracnoides
duramadre
piamadre
pineal
hoz
cerebr(o|al(es)?)
cerebelo
encéfalo
rinencéfalo
tálamo
hipotálamo
hipocampo
uncus
Varolio
tentorio
supratentorial
infratentorial
ganglios basales
globus pallidus
Reil
opérculo
palio
putamen
tapetum
epéndimo
supraselar
pontocerebeloso
vermis
médula oblonga
mesencéfalo
oliva
pedúnculo
"""

primario_C72_nervios_centrales = r"""
médula
epidural
raqu[ií]de(o|a)
cefalorraqu[ií]deo
cerebroespinal
extradural
parasellar
cono medular
filum terminale
cauda equina
tracto
quiasma
nervio(so)?
"""

complementario_C72 = r"""
espinal
cervical
lumbar
sacra
torácica
olfatorio
óptico
auditivo
craneal
abductor
accesorio
accesorio espinal
glosofaríngeo
hipogloso
motor
ocular
trigémino
troclear
vago
"""

primario_C73_C75 = r"""
endocrinas?
pluriglandular
tiroide(s|o)
tirogloso
suprarrenal
adrenal
paratiroides
pituitaria
hipófisis
Rathke
silla turca
paraganglios?
Zuckerkandl
glomo
"""


# * secundarios
# secundario = "|".join(
#     secundario.splitlines()[1:]
#     + adjetivos.splitlines()[1:]
#     + partes.splitlines()[1:]
#     + posiciones.splitlines()[1:]
# )

secundario = r"""
tejido
glándulas?
sistema
mucosa
conducto
vías
amígdala
fren(illo|ulum)
tonsila
maxilar
axilar
alv[ée]ol(o|ar)
d[oe]nta(al|rio)
glosopalatino
mejilla
faucal
palatina
vall[ée]cula
adenoide
coana
cricoide
ariteno(ide[os]?)?
cervical
torácico
abdominal
cardi(as|o)
pil[óo]r(o|ico)
divertículo
gastro
ciego
ileocecal
sigmoide(a|o)?
p[ée]lvi(co)?
hep[áa]t(o|ico)
transverso
esplénico
apéndice
ampolla
cloacogénica
esfinter
biliar(es)?
bilioso
colangiolo
cístico
colédoco
endocrino
digestivos
alimentario
órganos
tracto
cornete
tabique
cart[íi]lag(o|inoso)
orificio
mastoideo
timpánica
Eustaquio
etmoidal
esfenoidal
cuneiforme
tiroideo
ventr[ií]cul(o|ar(es)?)
hilio
vias
aurícula
lóbulo
visceral
facial
nasal
columna
cervical
supraclavicular
escapular
glútea
infraclavicular
inguinal
sacrococcígea
genitales
horquilla
monte (púbico|de venus)
pudendo
cervical
estroma
ligamentos?
membranas?
cavernoso
túnica
ves[ií]cula
cáli(z|ces)
cúpula
vesical
limbo
coroide
órbita
lentes
cristalinas
músculo
craneal
espinal
polo
hemisferio
plexo
coroideo
basal
craneofaríngeo
pineal
carotídeo
aórtico
coccígeo
paraaórtico
yugular
cuadrante
"""

posiciones = r"""
(izquierd|derech)[oa]
(supe|infe|poste|ante)rior
(ex|in)te(rn[oa]|rior)
(ex|in)trinsec[oa]
(dors|ventr|later|centr)al
(occipit|orbit|front|pariet|tempor)al
(proxim|dist|axi)al
(as|des)cendente
(men|may)or(es)?
medi[oa]
cuadrante(\w+)
tercer
cuarto
"""

adjetivos = r"""
periféric[ao]s?
autónom[ao]
roj[oa]s?
blanc[oa]s
rosad[ao]
dur[ao]
bland[ao]
delgado
grueso
verdader[oa]
fals[oa]
principal
femeninos?
masculinos?
anch[ao]
redond[ao]
descendido
retenid[ao]
deferentes
callos[ao]
"""

partes = r"""
parte
cara
superficie
prolongación
área
zona
región
porción
línea
ángulo
base
tallo
raíz
borde
punta
unión
comisura
surco
vasos
triángulo
trígono
tercio
cavidad
pliegue
válvula
seno
fosa
pilar
fauces
hendidura
pared
piso
techo
fondo
cuerpo
corpus
antro
canal
lesión
curvatura
canalículos?
islotes
islas
cabeza
cuerpo
cola
cuello
vestíbulo
bandas
disco
frente
orificios?
canal
muñón
istmo
segmento
anexos
pirámide
puente
fosa
localización
saco
bolsa
l[íi]quido
"""


prefijos = r"""
sub
pre
perio?
para
extra
intra
inter
supra
endo
exo
epi
mio
oro
meso
naso
hipo
laringo
crico
ariteno
retro
(en)?cefalo
"""

# * miembros

miembros = r"""
extremidad(es)?
miembros?
codo
hombro
antebrazo
brazo
pierna
rodilla
tobillo
talón
pie
dedo
pulgar
muñeca
mano
"""

otros_sitios = r"""
nasal
oído
aurícula
auditivo
espalda
cadera
p[eé]lvi(s|co)
p[uú]bi(s|co)
cara
frente
mandíbula
mejilla
mentón
nariz
sien
cuello
cabeza
tronco
abdomen
ano
axila
espalda
flanco
ingle
mama
nalga
ombligo
pecho
periné
tórax
tronco
antebrazo
brazo
codo
dedo
hombro
mano
muñeca
palma
pulgar
dedo
cadera
dedo
hueco poplíteo
miembro inferior
muslo
pantorrilla
pie
pierna
rodilla
talón
tobillo
"""

primario_mal_definido = miembros + otros_sitios.strip("\n")

# * Complementario ganglios

complementario_C77_0 = r"""
auricular
cervical
escaleno
mandibular
occipital
parotídeo
preauricular
prelaríngeo
pretraqueal
retrofaríngeo
sublingual
submandibular
submaxilar
submentoniano
supraclavicular
yugular
"""

complementario_C77_1 = r"""
intratorácico
broncopulmonar
bronquial
diafragmático
esofágico
hiliar
hiliar pulmonar
innominado
intercostal
mediastínico
paraesternal
pulmonar
torácico
traqueal
traqueobronquial
"""

complementario_C77_2 = r"""
intrabdominal
abdominal
aórtico
celíaco
cólico
conducto común
esplénico
gástrico
hepático
hiliar esplénico
ileocólico
intestinal
lumbar
mesentérico
mesocólico
pancreático
paraaórtico
periaórtico
peripancreático
pilórico
portahepático
portal
retroperitoneal
"""

complementario_C77_3 = r"""
axilar
braquial
cubital
extremidad
epitroclear
infraclavicular
pectoral
subclavicular
subescapular
"""

complementario_C77_4 = r"""
crural
Cloquet
extremidad
Rosenmüller
femoral
inguinal
poplíteo
subinguinal
tibial
"""

complementario_C77_5 = r"""
epigástrico
hipogástrico
ilíaco
intrapélvico
obturador
paracervical
parametrial
presinfisial
sacro
"""

# Lateralidad
lat_emparejado = [
    "l[óo]bulo frontal",
    "l[óo]bulo parietal",
    "l[óo]bulo temporal",
    "l[óo]bulo occipital",
    "l[óo]bulo",
    "ventrículos cerebrales",
    "l[óo]bulo superior",
    "ojo",
    "glandula lacrimal",
    "oido",
    "seno paranasal maxilar",
    "seno paranasal frontal",
    "orejas",
    "coclea",
    "canales semicirculares",
    "hueso",
    "mastoides",
    "hueso temporal",
    "hueso parietal",
    "hueso maxilar",
    "hueso nasal",
    "coanas",
    "amigdalas faringeas",
    "amigdala faringea",
    "adenoides",
    "parotida",
    "glandula submandibular",
    "glandula sublingual",
    "glandula paratiroides",
    "pulm[óo]n(es)?",
    "bronquios principales",
    "bronquio",
    "mama",
    "clavicula",
    "costilla",
    "humero",
    "radio",
    "cubito",
    "dedo( de)? mano",
    "labio",
    "riñon",
    "riñones",
    "glandulas suprarrenales",
    "ureter",
    "testiculo",
    "testiculos",
    "conducto deferente",
    "glandulas seminales",
    "glandula seminal",
    "ovarios",
    "ovario",
    "trompa de falopio",
    "tuba uterina",
    "tuba de falopio",
    "femur",
    "rotula",
    "tibia",
    "fibula",
    "perone",
    "hueso de tarso",
    "huesos de tarso",
    "calcaneo",
    "astragalo",
    "cuboide",
    "navicular",
    "escafoides",
    "cuneiforme interno",
    "cuneiforme medio",
    "cuneiforme externo",
    "dedos? del pie",
    "muslo",
]

latnot_emparejado = [
    "piel",
    "cuerpo calloso",
    "tallo cerebral",
    "bulbo raquideo",
    "cerebelo",
    "medula espinal",
    "tercer ventriculo cerebral",
    "cuarto ventriculo cerebral",
    "pituitaria",
    "hueso frontal",
    "hueso occipital",
    "hueso mandibular",
    "hueso maxilar",
    "hueso esfenoidal",
    "hueso etmoidal",
    "tabique nasal",
    "nariz",
    "lengua",
    "encia superior",
    "encia inferior",
    "faringe",
    "laringe",
    "epiglotis",
    "traquea",
    "tiroides",
    "hueso hioides",
    "corazón",
    "timo",
    "diafragma",
    "estomago",
    "omento",
    "epiplon",
    "h[ií]gado",
    "vesicula biliar",
    "intestino grueso",
    "colon",
    "intestino delgado",
    "duodeno",
    "yeyuno",
    "ileon" "recto",
    "ano",
    "pancreas",
    "bazo",
    "utero",
    "vejiga",
    "uretra",
    "pr[oó]stata",
    "pene",
    "epididimo",
    "clitoris",
    "vulva",
    "vagina",
    "cervix",
    "[úu]tero",
]

tomia = {
    "apéndice": "apendice",
    "mama": "cuadrante|maste",
    "estómago": "gastre",
    "colon": "hemicole",
    "hígado": "hepate",
    "útero": "histere",
    "laringe": "laringe",
    "ganglios linfáticos": "linfadene",
    "mandíbula": "mandibule",
    "riñón": "nefre",
    "ovario": "ofore",
    "omento": "omente",
    "recto": "proctosigmoide",
    "próstata": "prostate",
    "tiroides": "tiroide",
}

primario_values = [
    primario_C50_mama,
    primario_C51_C58,
    primario_C60_C63,
    primario_C15_C26,
    primario_C34_pulmon,
    primario_C30_C33,
    primario_C37_C38,
    primario_C42_hemato,
    primario_C70_C71,
    primario_C64_C68,
    primario_C73_C75,
    primario_C48_peritoneo,
    primario_C72_nervios_centrales,
    primario_C69_ojo,
    primario_C40_C41,
    primario_C44_piel,
    primario_C00_C14,
    "\nganglios? (linf[aá]ticos?)?",
    primario_C47_nervios,
    primario_C49_tejidos,
    primario_mal_definido,
]

complementario_values = [
    primario_C50_mama
    + posiciones.strip("\n")
    + adjetivos.strip("\n")
    + secundario.strip("\n"),
    primario_C51_C58 + posiciones.strip("\n") + secundario.strip("\n"),
    primario_C60_C63 + posiciones.strip("\n") + partes.strip("\n"),
    primario_C15_C26 + posiciones.strip("\n") + partes.strip("\n"),
    primario_C34_pulmon + posiciones.strip("\n") + secundario.strip("\n"),
    primario_C30_C33 + secundario.strip("\n"),
    primario_C37_C38 + posiciones.strip("\n") + secundario.strip("\n"),
    primario_C42_hemato,
    primario_C70_C71 + posiciones.strip("\n") + partes.strip("\n"),
    primario_C64_C68 + posiciones.strip("\n") + partes.strip("\n"),
    primario_C73_C75 + secundario.strip("\n"),
    primario_C48_peritoneo + secundario.strip("\n"),
    primario_C72_nervios_centrales
    + complementario_C72.strip("\n")
    + posiciones.strip("\n")
    + miembros.strip("\n"),
    primario_C69_ojo
    + secundario.strip("\n")
    + posiciones.strip("\n")
    + partes.strip("\n"),
    primario_C40_C41
    + miembros.strip("\n")
    + posiciones.strip("\n")
    + adjetivos.strip("\n"),
    primario_C44_piel + posiciones.strip("\n") + primario_mal_definido.strip("\n"),
    primario_C00_C14 + posiciones.strip("\n") + secundario.strip("\n"),
    "\nganglios? (linf[aá]ticos?)?\n"
    + complementario_C77_0.strip("\n")
    + complementario_C77_1.strip("\n")
    + complementario_C77_2.strip("\n")
    + complementario_C77_3.strip("\n")
    + complementario_C77_4.strip("\n")
    + complementario_C77_5.strip("\n"),
    primario_C47_nervios + miembros.strip("\n"),
    primario_C49_tejidos + miembros.strip("\n"),
    primario_mal_definido,
]


primario = dict(zip(primario_keys, primario_values))
primario = {k: v.splitlines()[1:] for k, v in primario.items()}

complementario = dict(zip(primario_keys, complementario_values))
complementario = {k: v.splitlines()[1:] for k, v in complementario.items()}
