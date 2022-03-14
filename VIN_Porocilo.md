<center>
<h1>VIN Poročilo - 1. DN - 2021/22</h1>

<h2>Ultrazvočni senzorji razdalje (HC-SR04)</h2>

15.03.2022

Jan Renar  
</center>

## Grafična skica


## Predstavitev naprave: opis, slika in razvoj


Mogoče skupaj združit?
## Arhitektura in tehnologije
Shema vezja, Vsi AMPi, filtri,

## Opis delovanja
Ojačevalci LM324 in njihova uporaba
Bandpass filter (določi sprejete frekvence)
    http://www.learningaboutelectronics.com/Articles/Bandpass-filter-calculator.php
 delovanje le teh, pulse generator, oječevalci, rx,tx
 + moje meritve/testi

## Uporaba s kratkim opisom delovanja
opis povezav, delovanje kode

Povezava tipala HC-SR04 z Arduino platformo je preprosto, saj potrebuje le 2 signalni povezavi in napajanje. To tipalo deluje z napetostjo napajanja 5V, kar pomeni, da je kompatibilno z veliko različnih sistemov. Omenjeni signalni povezavi pa sta *TRIG*, ki služi kot vhod tipala in *ECHO* kot izhod. V sladu s tem moramo v programski kodi povezane vhode na Arduinu pravilno nastaviti. Spodnja Arduino koda TRIG povezavo za 10 milisekund nastavi na HIGH/5V kar sporoči krmilniku na tipalu, da sproži 8 zvočnih impulzov frekvence približno 40kHz. Po tem pa mikrokrmilnik čaka, dokler se vhod ECHO nastavi na HIGH/5V in ob pozitivni fronti prične meriti čas trajanja visokega stanja na ECHO vhodu. Iz trajanja visokega stanja se z konstanto hitrosti zvoka izračuna izmerjena razdalja.

$ Razdalja[cm] = \frac{Izmerjen čas[\mu S] * 343 m/s * 10^{-6} }{2} $


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
  
  // Trigger HC-SR04 ping
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  
  // Speed of sound at 20°C = 343 m/s
  distance = duration * 0.0343 / 2;
  
  // Displays the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  delay(10);
}
```

## Zaključek

## Literatura

https://www.intorobotics.com/8-tutorials-to-solve-problems-and-improve-the-performance-of-hc-sr04/

Podobne meritve kot moje
https://www.intorobotics.com/object-detection-hc-sr04-arduino-millis/

http://www.pcserviceselectronics.co.uk/arduino/Ultrasonic/HC-SR04-cct.pdf