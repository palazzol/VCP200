
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

#define SETTING_TIME_US (10)

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
int data_memory_started = 0;
int mode = 0; // 0 = program memory dump = 0, 1 = data memory dump

void PrintHex8(int b)
{
  if (b<0x10) Serial.print("0");
  Serial.print(b,HEX);
}

static unsigned int count = 0xff;

void ProcessDataMemoryFrame()
{
  static int checksum = 0;
  if (address == -1)
    return;
  //Serial.print(count,HEX);
  //Serial.print(" ");
  //Serial.println((data>>2)&0xff);
  if ((address == last_address) && ((address&1) == 0))
  {
    //unsigned int new_address = ((address>>1)-2) % 0x100;
    unsigned int new_address = (count-1)%0x100;
    if (new_address == 0) {
      data_memory_started = 1;  
      Serial.println();
      Serial.println();
      Serial.println("Data Memory, Motorola S-Record Format:");
      Serial.print("S00600004844521B");  
    }
    if (data_memory_started)
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

      if (new_address % 256 == 0xff)
      {
        Serial.println();
        Serial.println("S5030008F4");
        Serial.println("S9030000FC");
        mode = 0;
        data_memory_started = 0;
      }
    }
  }
  last_address = address;
  
  /*
  PrintHex8(address>>8);
  PrintHex8(address%256);
  Serial.print(" ");
  PrintHex8((data>>11)&0x01);
  Serial.print(" ");
  PrintHex8((data>>10)&0x01);
  Serial.print(" ");
  PrintHex8((data>>2)&0xff);
  Serial.print(" ");
  PrintHex8((data>>1)&0x01);
  Serial.print(" ");
  PrintHex8((data>>0)&0x01);
  Serial.println();
  */
}

void ProcessProgramMemoryFrame()
{
  static int checksum = 0;
  if (address == -1)
    return;
  if (address == last_address)
  {
    unsigned int new_address = (address - 1) % 0x1000;
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
      if ((new_address % 0x1000) == 0xfff)
      {
        Serial.println();
        Serial.println("S50300807C");
        Serial.println("S9030000FC");
        mode = 1;
        program_memory_started = 0;
      }
    }
  }
  last_address = address;
}

void ProcessFrame()
{
  if (mode == 0)
    ProcessProgramMemoryFrame();
  else // mode == 1
    ProcessDataMemoryFrame();
}

int ProcessClockRisingEdge()
{
  static int bitcount = 0;
  
  if (sync)
  {
    ProcessFrame(); 
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
  /*
  static int opcodes[12] = { 0xac, 0xff, 0xff, 0xff,   // LDA  X
                             0xe0, 0xff, 0xff, 0xff,   // LDA  [X]
                             0xa8, 0xff, 0xff, 0xff,   // INC  X
                            };
  static int opcode_index = 2;
  */
  /*
  static int opcodes[20] = { 0x00, 0x00, 0x00, 0x00, 0x00,
                             0xe8, 0x00, 0xff,  // LDA  #$00
                             0xbc, 0xff, 0xff, 0xff,   // STA  X
                             //0xac, 0xff, 0xff, 0xff,   // LDA  X
                             0xe0, 0xff, 0xff, 0xff,   // LDA  [X]
                             0xa8, 0xff, 0xff, 0xff,   // INC  X
                           };
  */                         
                        
  static int opcodes[10] = { 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                             0xf8, 0x55, 0xff, 0xff
                           };
                             
  static int opcode_index = 0;
  
  static int test_opcode;
  static int bitcount = 0;
    
  sync = digitalRead(SYNC);

  if (mode == 1) {
  if (sync)
  {
    bitcount = 0;
    opcode_index += 1;
    if (opcode_index > 9) opcode_index = 6;
    //if (opcode_index == 6)
      //Serial.println();
    if (opcodes[opcode_index] == 0x55)
    {
      //PrintHex8(count);
      test_opcode = (count<<1) | 0xe01;
      count = (count + 1) % 0x100;
    }
    else
    {
      //PrintHex8(opcodes[opcode_index]);
      test_opcode = (opcodes[opcode_index]<<1) | 0xe01;
    }
    //Serial.print(": ");
  }
  
  //if (test_opcode == 0xfff)
  //  pinMode(DATAIN, INPUT);
  //else
  //{
    //pinMode(DATAIN, OUTPUT);
    digitalWrite(DATAIN,(test_opcode>>bitcount)&1);
  //}
  
  bitcount++;
  }
}

void ProcessExtalEdge(int state)
{
  static int last_clock_state;
  static int clock_state = 0;
  int rv = mode;
  
  digitalWrite(EXTAL, state);
  delayMicroseconds(SETTING_TIME_US);
  
  last_clock_state = clock_state;
  clock_state = digitalRead(CLOCK);
  if ((last_clock_state == 1) && (clock_state == 0))
    ProcessClockFallingEdge();
  if ((last_clock_state == 0) && (clock_state == 1))
    rv = ProcessClockRisingEdge(); 
  return rv;
}

void loop() {

  // Rom Verify Mode for Program data

  // Some clocks in reset
  for(int i=0;i<100;i++) {
    digitalWrite(EXTAL, 0);
    digitalWrite(EXTAL, 1);
  }
  digitalWrite(nRESET, 1);
  digitalWrite(LED, 1);

  while (mode == 0) {
    ProcessExtalEdge(0);
    ProcessExtalEdge(1);
  }

  mode = 1;
  
  digitalWrite(LED, 0);
  digitalWrite(nRESET, 0);

  // Non-user mode
  digitalWrite(PA7, 0);
  digitalWrite(DATAIN, 1);   // Execute 0xFF
  
  for(int i=0;i<100;i++) {
    digitalWrite(EXTAL, 0);
    digitalWrite(EXTAL, 1);
  }
  digitalWrite(nRESET, 1);
  digitalWrite(LED, 1);

  last_address = -1;
  while (mode == 1) {
    ProcessExtalEdge(0);
    ProcessExtalEdge(1);
  }

  Serial.println();
  Serial.println();
  Serial.println("Done! - Please hit reset button to redump");
  while(1);

  /*
  last_address = -1;
  mode = 0;
  digitalWrite(LED, 0);
  digitalWrite(nRESET, 0);

  // Back to Rom Verify
  digitalWrite(DATAIN, 0);
  digitalWrite(PA7, 1);
  */
}
