uint8_t read(byte pin) {
	uint8_t a = (uint8_t)(pulseIn(pin, HIGH) / 3.88 - 255);
	return a;
}

void setup() {
	Serial.begin(115200);
}

void loop() {
	while(!Serial.available());
	uint8_t x = Serial.read();
	Serial.write(read(16)); //lr
	Serial.write(read(10)); //ud
}
