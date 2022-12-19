//for functions that can be used in broad scenarios

//get nth bit of a char
bool getBit(char x, unsigned short n);
//sets the nth bit of a char to 1 or 0
char setBit(char c, bool b, unsigned short n);

//pause the program for t ms
void waitMillis(int t);

void send_data(char data, int startLine, int dataLine);

char get_data(int startLine, int dataLine);