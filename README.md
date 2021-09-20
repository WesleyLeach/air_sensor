# SDS011 Air Quality Sensor Project
A repository for the code and documentation for the SDS011 air sensor.

## Data Packet from SDS011

| Byte Number | Name | Contents
|---|---|---|
| 0 | Message Header | AA
| 1 | Commander No. | C0
| 2 | DATA 1 | PM 2.5 Low Byte
| 3 | DATA 2 | PM 2.5 High Byte
| 4 | DATA 3 | PM 10 Low Byte
| 5 | DATA 4 | PM 10 High Byte
| 6 | DATA 5 | ID Byte 1
| 7 | DATA 6 | ID Byte 2
| 8 | Check-sum | Check-sum
| 9 | Message tail | AB

## Air Quality Index

| Range | PM 2.5 / 10 
|---|---|
| 0 to 50 | Healthy air quality
| 51 to 100 | Moderate, not uncommon in some cities
| 101 to 150 | Unhealthy for sensitive groups, limit activity
| 151+ | Probably best to stay inside
### Known Issues

* After prolonged use the sensor can become clogged with dust. The sensor should be disassembled and cleaned periodically.

## Sources
1. https://www.raspberrypi.org/blog/monitor-air-quality-with-a-raspberry-pi/
2. https://www.amazon.com/SDS011-Quality-Detection-Conditioning-Monitor/dp/B07FSDMRR5
3. https://aqicn.org/sensor/sds011/
4. https://cdn-reichelt.de/documents/datenblatt/X200/SDS011-DATASHEET.pdf
5. https://www.airnow.gov/sites/default/files/2018-04/aqi_brochure_02_14_0.pdf
