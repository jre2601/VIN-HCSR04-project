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
  
  // Sproži HC-SR04 meritev
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Prebere echoPin in vrne čas potovanja zvoka [µs]
  duration = pulseIn(echoPin, HIGH);
  
  // Hitrost zvoka pri 20°C = 343 m/s
  distance = duration * 0.0343 / 2;
  
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  delay(10);
}
