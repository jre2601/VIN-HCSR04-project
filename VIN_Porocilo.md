<center>
<h1>VIN Poročilo - 1. DN - 2021/22</h1>

<h2>Ultrazvočni senzorji razdalje (HC-SR04)</h2>

15.03.2022

Jan Renar  
</center>

## Grafična skica


## Predstavitev naprave

### Opis in speficikacije
HC-SR04 je preprosta različica ultrazvočnih tipal za merjenje razdalje z uporabo ultrazvočnih valov. Sestavljata ga ultrazvočni oddajnik (zvočnik) in sprejemnik (mikrofon). Ti dve komponenti sta zalotani na sprednjem delu tiskanega vezja, na zadnji strani pa so ostale potrebne komponente za delovanje tega tipala. Tipalo se napaja z 5V enosmernega toka in ima porabo 15mA [1]. V podatkovni listini [1] je specificiran tudi doseg in *vidno polje* tega tipala, merilo naj bi do 4 metre v daljavo in 15° vidno polje v vsako stran, v nadaljevanju bodo predstavljene meritve, ki nakazujejo, da so te vrednosti veljavne le za idealne razmere, katere pa je v realni uporabi skoraj nemogoče doseči.

Tipalo razdaljo izmeri tako, da po oddanem ultrazvočnem signalu, meri čas dokler sprejemnik ne zazna odboja in iz izmerjenega časa izračuna prepotovano razdaljo zvočnega valova. Ta princip uporabljajo tudi laserski merilniki razdalje, le da upoštevajo hitrost svetlobe in ne hitrost zvoka, tako kot ultrazvočna tipala. 


![](src/Opis.jpg.svg)

### Kaj je ultrazvok in kratka zgodovina

Ultrazvok je definiran kot zvok, ki ima frekvenco višjo od 20kHz, kar je tudi zgornja meja človeškega sluha. Zvok takih frekvenc ima valovno dolžino 1.9cm ali manj [2].

Začetek uporabe ultrazvoka v tehnološke namene sega v leto 1917, ko so uporabili prvo ultrazvočno tipalo za zaznavanje podmornic (imenovano tudi *sonar*). Z nadaljnim razvojem tehnologije, se pojavi uporaba ultrazvoka za namene testiranja materialov in njihovih šibkih točk (npr. varjene kovine) ter uporaba v medicinske namene [3]. Odvisno od namena in materiala, so frekvence ultrazvokov različne. Za ugotavljanje razdalje po zraku, do nekega predmeta je uporabljena frekvenca okoli 40kHz. Za medicinske namene se frekvence gibajo od 1MHz do 18MHz, saj je od frekvence odvisna prodornost zvočnih valov skozi dano tkivo.


## Arhitektura in tehnologije
![](src/HCSR04_PCB_scheme.png)
Shema vezja

### Oddajnik, sprejemnik

### Integrirana vezja

**LM32**

**RCWL-9300**

**RCWL-9200**

## Opis delovanja
Ojačevalci LM324 in njihova uporaba
Bandpass filter (določi sprejete frekvence)
    http://www.learningaboutelectronics.com/Articles/Bandpass-filter-calculator.php
 delovanje le teh, pulse generator, oječevalci, rx,tx
 + moje meritve/testi

## Uporaba s kratkim opisom delovanja

Povezava tipala HC-SR04 z Arduino platformo je preprosto, saj potrebuje le 2 signalni povezavi in napajanje. To tipalo deluje z napetostjo napajanja 5V, kar pomeni, da je kompatibilno z veliko različnih sistemov. Omenjeni signalni povezavi pa sta *TRIG*, ki služi kot vhod tipala in *ECHO* kot izhod. V sladu s tem moramo v programski kodi povezane vhode na Arduinu pravilno nastaviti. Spodnja Arduino koda TRIG povezavo za 10 milisekund nastavi na HIGH/5V kar sporoči krmilniku na tipalu, da sproži 8 zvočnih impulzov frekvence približno 40kHz. Po tem pa mikrokrmilnik čaka, dokler se vhod ECHO nastavi na HIGH/5V in ob pozitivni fronti prične meriti čas trajanja visokega stanja na ECHO vhodu. Iz trajanja visokega stanja se z konstanto hitrosti zvoka izračuna izmerjena razdalja.

<img src="https://render.githubusercontent.com/render/math?math=Razdalja[cm] = \frac{Izmerjencas[\mu S] * 343 m/s * 10^{-6} }{2}">

<br>

<img src="src/HCsr04_shema.png">

```
#define echoPin 3
#define trigPin 2

long duration;
int distance;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // trigPin postavi na HIGH za 10 milisekund in tako sproži meritev na tipalu
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // pulseIn vrne čas trajanja stanja HIGH, ki ga tipalo nastavi na echoPin povezavo
  duration = pulseIn(echoPin, HIGH);
  
  // Izračun razdalje - 20°C => 343 m/s
  distance = duration * 0.0343 / 2;
  
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  delay(10);
}
```

## Zaključek

## Literatura

[1]
https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf

[2]
https://en.wikipedia.org/wiki/Ultrasound

[3]
https://en.wikipedia.org/wiki/Medical_ultrasound

https://www.intorobotics.com/8-tutorials-to-solve-problems-and-improve-the-performance-of-hc-sr04/

Podobne meritve kot moje
https://www.intorobotics.com/object-detection-hc-sr04-arduino-millis/


http://www.pcserviceselectronics.co.uk/arduino/Ultrasonic/HC-SR04-cct.pdf