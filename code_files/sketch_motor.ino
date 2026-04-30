#include <AFMotor.h>

// Motors
AF_DCMotor m1(1);
AF_DCMotor m2(2);
AF_DCMotor m3(3);
AF_DCMotor m4(4);

char cmd = 'S';  // default stop

void setup() {
  Serial.begin(9600);

  m1.setSpeed(200);
  m2.setSpeed(200);
  m3.setSpeed(200);
  m4.setSpeed(200);

  Serial.println("READY");
}

void loop() {

  // -------- SERIAL COMMAND --------
  if (Serial.available() > 0) {
    cmd = Serial.read();

    // Ignore unwanted characters
    if (cmd == '\n' || cmd == '\r') return;

    Serial.print("CMD: ");
    Serial.println(cmd);

    executeCommand(cmd);
  }

  // -------- OPTIONAL IR SENSOR --------
  static unsigned long lastPrint = 0;

  if (millis() - lastPrint > 500) {   // print every 0.5 sec only
    lastPrint = millis();

    int ir1 = analogRead(A0);
    int ir2 = analogRead(A5);

    Serial.print("IR1: ");
    Serial.print(ir1);
    Serial.print(" | IR2: ");
    Serial.println(ir2);
  }
}

// -------- COMMAND HANDLER --------
void executeCommand(char c) {
  switch (c) {
    case 'F': forward(); break;
    case 'B': backward(); break;
    case 'L': left(); break;
    case 'R': right(); break;
    case 'S': stopCar(); break;
    default: stopCar(); break;
  }
}

// -------- MOVEMENT --------
void forward() {
  m1.run(FORWARD);
  m2.run(FORWARD);
  m3.run(FORWARD);
  m4.run(FORWARD);
}

void backward() {
  m1.run(BACKWARD);
  m2.run(BACKWARD);
  m3.run(BACKWARD);
  m4.run(BACKWARD);
}

void left() {
  m1.run(BACKWARD);
  m2.run(FORWARD);
  m3.run(BACKWARD);
  m4.run(FORWARD);
}

void right() {
  m1.run(FORWARD);
  m2.run(BACKWARD);
  m3.run(FORWARD);
  m4.run(BACKWARD);
}

void stopCar() {
  m1.run(RELEASE);
  m2.run(RELEASE);
  m3.run(RELEASE);
  m4.run(RELEASE);
}