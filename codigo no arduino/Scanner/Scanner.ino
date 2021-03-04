#include  <Stepper.h> 

char SuaString[5] = "";
long int passo;
long int passo2;
long int Numero = 0;

const int PassoPorVolta = 500; // Passo por Volta do motor de passo, aqui definimos a velocidade de rotação

// Inicializa a biblioteca Stepper.h
// O motor de passo =>  MotorP
Stepper MotorP(PassoPorVolta, 8, 10, 9, 11);

void setup() {
  
  // Ajusta velocidade para 60 RPM
  MotorP.setSpeed(60);
  Serial.begin(9600);
}
void loop() {

  //Recebe uma string de 3 caracteres pela serial

   if (Serial.available()) {

     for (int i=0;i<5;i++){

      //Armazena na string (array de char)

      SuaString[i] = Serial.read();

      delay(10);

   }
      Numero = atoi(SuaString);
  //Codição de controle
      if( Numero > 0){
        //Serial.println("entrou no if");
        passo =( ((2050 * (Numero))/ 360));
        Serial.println(passo);
        MotorP.step(passo);

      }else{
        //Serial.println("entrou no else");
        passo =( ((2050 * (Numero))/ 360));
        Serial.println(passo); 
        MotorP.step(passo);

      }

   } 
}
