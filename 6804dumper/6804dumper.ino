
//      6804    Arduino
#define EXTAL   (2)
#define nIRQ    (3)
#define MDS     (A5)
#define TIMER   (A4)
#define DATAOUT (8)   // PB0
#define PB1     (9)   // PB1
#define CRCL    (10)  // PB2
#define CRCH    (11)  // PB3
#define CRCSTRB (4)   // PB4
#define ADDRESS (5)   // PB5
#define SYNC    (6)   // PB6
#define CLOCK   (7)   // PB7
#define PA4     (A0)
#define DATAIN  (A1)
#define PA6     (A2)
#define PA7     (A3)
#define nRESET  (12)
#define LED     (13)

#define SETTING_TIME_US (100)

void setup() {

  Serial.begin(115200);
  
  pinMode(EXTAL, OUTPUT);
  digitalWrite(EXTAL, 0); 
  pinMode(nIRQ, OUTPUT);
  digitalWrite(nIRQ, 1);
  pinMode(MDS, OUTPUT);
  digitalWrite(MDS, 1);
    
  pinMode(TIMER, INPUT);
  pinMode(DATAOUT, INPUT);
  pinMode(PB1, INPUT);
  pinMode(CRCL, INPUT);
  pinMode(CRCH, INPUT);
  pinMode(CRCSTRB, INPUT);
  pinMode(ADDRESS, INPUT);
  pinMode(SYNC, INPUT);
  pinMode(CLOCK, INPUT);

  // Default to Rom Verify Mode
  pinMode(PA4, OUTPUT);
  digitalWrite(PA4, 1);
  pinMode(DATAIN, OUTPUT);
  digitalWrite(DATAIN, 0);
  pinMode(PA6, OUTPUT);
  digitalWrite(PA6, 1);
  pinMode(PA7, OUTPUT);
  digitalWrite(PA7, 1);
  pinMode(nRESET, OUTPUT);
  digitalWrite(nRESET, 0);

  pinMode(LED, OUTPUT);
  digitalWrite(LED, 0);

  Serial.println();
  Serial.println("*********************");
  Serial.println("*** MC6804 Dumper ***");
  Serial.println("*********************");
}

int sync = 0;
int last_address = -1;
int address = -1;
int data = -1;
int program_memory_started = 0;

void PrintHex8(int b)
{
  if (b<0x10) Serial.print("0");
  Serial.print(b,HEX);
}

void ProcessAddressAndData()
{
  static int checksum = 0;
  if (address == -1)
    return;
  if (address == last_address)
  {
    unsigned int new_address = (address - 1) % 0x800;
    if (new_address == 0) {
      program_memory_started = 1;
      Serial.println();
      Serial.println();
      Serial.println("Program Memory, Motorola S-Record Format:");
      Serial.print("S00600004844521B");
    }
    if (program_memory_started)
    {
      if (new_address % 32 == 0)
      {
        Serial.println();
        Serial.print("S123");
        PrintHex8(new_address>>8);
        PrintHex8(new_address%0x100);
        checksum = 2+32+1+(new_address>>8)+(new_address%0x100);
        //Serial.print("0 ");
      }
      PrintHex8((data>>2)&0xff);
      checksum += ((data>>2)&0xff);
      if (new_address % 32 == 31)
      {
        checksum %= 256;
        checksum ^= 255;
        PrintHex8(checksum);
      }
      if (new_address == 0x7ff)
      {
        Serial.println();
        Serial.println("S50300807C");
        Serial.println("S9030000FC");
      }
      //Serial.print(" ");
    }
  }
  last_address = address;
}

void ProcessClockRisingEdge()
{
  static int bitcount = 0;
  if (sync)
  {
    ProcessAddressAndData(); 
    address = 0;
    data = 0;
    bitcount = 0;   
  }
  if (digitalRead(ADDRESS))
    address |= (1 << bitcount);
  if (digitalRead(DATAOUT))
    data |= (1 << bitcount);    
  bitcount++;
}

void ProcessClockFallingEdge()
{
  sync = digitalRead(SYNC);
}

void ProcessExtalEdge(int state)
{
  static int last_clock_state;
  static int clock_state = 0;
  
  digitalWrite(EXTAL, state);
  delayMicroseconds(SETTING_TIME_US);
  
  last_clock_state = clock_state;
  clock_state = digitalRead(CLOCK);
  if ((last_clock_state == 1) && (clock_state == 0))
    ProcessClockFallingEdge();
  if ((last_clock_state == 0) && (clock_state == 1))
    ProcessClockRisingEdge(); 
}

void loop() {
  for(int i=0;i<100;i++) {
    digitalWrite(EXTAL, 0);
    digitalWrite(EXTAL, 1);
  }
  digitalWrite(nRESET, 1);
  digitalWrite(LED, 1);

  while (1) {
    ProcessExtalEdge(0);
    ProcessExtalEdge(1);
  }
}
