
public class HolaMundo {

    public static void main(String[] args) {
        //        System.out.println("Hola mundo desde java");
        //        
        //        int miVariable = 10;
        //        System.out.println(miVariable);
        //        miVariable = 5;
        //        System.out.println(miVariable);
        //        //Tipo String
        //        String miVariableCadena = "Bienvenidos";
        //        System.out.println(miVariableCadena);
        //        miVariableCadena = "Sigamos creciendo en programacion";
        //        System.out.println(miVariableCadena);
        //
        //        //var - inferencia de tipos en Java
        //        var miVariableEntera2 = 10;
        //        var miVariableCadena2 = "Seguimos estudiando";
        //        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        //        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //        //Reglas para definir una variable en Java
        //        var usuario = "Osvaldo";
        //        var titulo = "Ingeniero";
        //        var union = titulo + " " + usuario;
        //        System.out.println("union = " + union);
        //
        //        var a = 8;
        //        var b = 4;
        //        System.out.println(usuario + (a + b));
        //        //Ejercicio: caracteres especiales con Java
        //        var nombre = "Natalia";
        //        System.out.println("\nNueva linea: \n" + nombre);
        //        System.out.println("Tabulador: \t" + nombre);
        //        System.out.println("\t\t.:MENU:.");
        //        System.out.println("Retroceso: \b\b" + nombre);
        //        System.out.println("Comillas simples: \'"+nombre+"\'");
        //        System.out.println("Comillas dobles: \""+nombre+"\"");
        //        
        //        //Clase Scanner
        //        Scanner entrada = new Scanner(System.in);
        //        System.out.println("Digite su nombre: ");
        //        var usuario2 = entrada.nextLine();
        //        System.out.println("usuario2 = " + usuario2);
        //        System.out.println("Escriba el titulo: ");
        //        var titulo2 = entrada.nextLine();
        //        System.out.println("Resultado: "+titulo2+" "+usuario2);
        //        
        //        byte numEnteroByte = 127;
        //        System.out.println("numEnteroByte = " + numEnteroByte);
        //        System.out.println("Valor minimo del Byte:"+ Byte.MIN_VALUE);
        //        System.out.println("Valor maximo del Byte:"+ Byte.MAX_VALUE);
        //        
        //        short numEnteroShort = 32767;
        //        System.out.println("numEnteroShort = " + numEnteroShort);
        //        System.out.println("Valor minimo del Short:"+ Short.MIN_VALUE);
        //        System.out.println("Valor maximo del Short:"+ Short.MAX_VALUE);
        //        
        //        int numEnteroInt = 2147483647;
        //        System.out.println("numEnteroInt = " + numEnteroInt);
        //        System.out.println("Valor minimo del int:"+ Integer.MIN_VALUE);
        //        System.out.println("Valor maximo del int:"+ Integer.MAX_VALUE);
        //        
        //        long numEnteroLong = 9223372036854775807L;
        //        System.out.println("numEnteroLong = " + numEnteroLong);
        //        System.out.println("Valor minimo del long:"+ Long.MIN_VALUE);
        //        System.out.println("Valor maximo del long:"+ Long.MAX_VALUE);
        //        
        //        float numFloat = 3.4028235E38F;
        //        System.out.println("numFloat = " + numFloat);
        //        System.out.println("El valor minimo de float:"+Float.MIN_VALUE);
        //        System.out.println("El valor maximo de float:"+Float.MAX_VALUE);
        //        
        //        double numDouble = 1.7976931348623157E308;
        //        System.out.println("numDouble = " + numDouble);
        //        System.out.println("El valor minimo de double:"+Double.MIN_VALUE);
        //        System.out.println("El valor maximo de double:"+Double.MAX_VALUE);
        //        
        //        //Infetrencia de tipos var y tipos primitivos
        //        var numEntero = 20; //Las literales sin punto automaticamente son de tipo int
        //        System.out.println("numEntero = " + numEntero);
        //        var numFloat = 10.0F; // Automaticamente con el punto se transforma en tipo double
        //        System.out.println("numFloat = " + numFloat);
        //        var numDouble = 10.0;
        //        System.out.println("numDouble = " + numDouble);
        //        
        //        //Tipos primitivos char
        //        char miVariableChar = 'a';
        //        System.out.println("miVariableChar = " + miVariableChar);
        //        
        //        char varCaracter = '\u0024'; //asig con unicode
        //        System.out.println("varCaracter = " + varCaracter);
        //        char varCaracterDecimal = 36; //valor decimal del unicode
        //        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        //        char varCaracterSimbolo = '$';
        //        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        //        
        //        var varCaracter1 = '\u0024'; //asig con unicode
        //        System.out.println("varCaracter1 = " + varCaracter1);
        //        var varCaracterDecimal1 = (char)36; //valor entero y le asigna un tipo int
        //        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        //        var varCaracterSimbolo1 = '$';
        //        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        //        
        //        int varEnteroChar = '$';
        //        System.out.println("varEnteroChar = " + varEnteroChar);
        //        int caracterChar = 'b';
        //        System.out.println("caracterChar = " + caracterChar);
        //        
        //        //Tipos primitivos-booleanos
        //        var varBool = false;
        //        System.out.println("varBool = " + varBool);
        //        
        //        if (varBool) {
        //            System.out.println("La bandera es verde");
        //        }
        //        else {
        //            System.out.println("La bandera es roja");
        //        }
        //        
        //        var edad = 18;
        //        //var adulto = edad >= 18;
        //        if (edad >= 18){
        //            System.out.println("Eres mayor de edad");
        //        }
        //        else{
        //            System.out.println("Eres menor de edad");
        //        }
        //        Conversion de tipos primitivos
        //        var edad = Integer.parseInt ("20");
        //        System.out.println("edad = " + (edad + 1));
        //        var valorPI = Double.parseDouble("3.1416");
        //        System.out.println("valorPI = " + valorPI);
        //        
        //        Pedir un valor
        //        var entrada = new Scanner(System.in);
        //        System.out.println("Digite su edad: ");
        //        edad = Integer.parseInt(entrada.nextLine());
        //        System.out.println("edad = " + edad);
        //        
        //        Conversion de tipos primitivos Parte 2
        //
        //        var edadTexto = String.valueOf(10);
        //        System.out.println("edadTexto = " + edadTexto);
        //        
        //        var fraseChar = "programadores".charAt(12);
        //        System.out.println("fraseChar = " + fraseChar);
        //        
        //        System.out.println("Digite un caracter: ");
        //        fraseChar = entrada.nextLine().charAt(0);
        //        System.out.println("fraseChar = " + fraseChar);
        //        int num1 = 5, num2 = 4;
        //        var solucion = num1 + num2;
        //        System.out.println("solucion de la suma = " + solucion);
        //
        //        solucion = num1 - num2;
        //        System.out.println("solucion de la resta = " + solucion);
        //
        //        solucion = num1 * num2;
        //        System.out.println("solucion de la multiplicacion = " + solucion);
        //
        //        solucion = num1 / num2;
        //        System.out.println("solucion de la division = " + solucion);
        //
        //        var solucion2 = 3.4 / num2;
        //        System.out.println("solucion2 resultado de la division = " + solucion2);
        //
        //        solucion = num1 % num2; //Guarda el residuo entero del a division
        //        System.out.println("solucion = " + solucion); // 5/4
        //
        //        if (num2 % 2 == 0) {
        //            System.out.println("Es un numero par");
        //        } else {
        //            System.out.println("Es un numero impar");
        //        }
        //        
        //        int varNum1 = 1, varNum2 = 4;
        //        var varNum3 = varNum1 + 6 - varNum2;
        //        System.out.println("varNum3 = " + varNum3);
        //        
        //        varNum1 += 1; //varNum1 = varNum1 + 1, operador de composicion
        //        System.out.println("varNum1 = " + varNum1);
        //        
        //        varNum2 -= 2;
        //        System.out.println("varNum2 = " + varNum2);
        //        
        //        varNum1 *= 5;
        //        System.out.println("varNum1 = " + varNum1);
        //        
        //        varNum3 /= 4;
        //        System.out.println("varNum3 = " + varNum3);
        //        
        //        varNum1 %= 6;
        //        System.out.println("varNum1 = " + varNum1);
//
//        //Operadores unarios: cambio de signo 
//        var varA = 7;
//        var varB = -varA;
//        System.out.println("varA = " + varA);
//        System.out.println("varB = " + varB);
//        
//        //Operadores unarios: operador de negacion
//        var varC = true;
//        var varD = !varC;
//        System.out.println("varC = " + varC);
//        System.out.println("varD = " + varD);
//        
//        //Operadores unarios de incremento: preincremento
//        var varE = 9;
//        var varF = ++varE;
//        System.out.println("varE = " + varE);
//        System.out.println("varF = " + varF);
//        
//        //Operadores unarios: post incremento
//        
//        var varG = 3;
//        var varH = varG++;
//        System.out.println("varG = " + varG);
//        System.out.println("varH = " + varH);
//        
//        //Operadores unarios: pre - decremento
//        
//        var varI = 4;
//        var varJ = --varI;
//        System.out.println("varI = " + varI);
//        System.out.println("varJ = " + varJ);
//        
//        //Operadores unarios: post-decremento
//        
//        var varK = 8;
//        var varL = varK--;
//        System.out.println("varK = " + varK);
//        System.out.println("varL = " + varL);
//        
//        //Operadores de igualdad y relacionales
//        var aNum = 5;
//        var bNum = 4;
//        var cNum = (aNum == bNum);
//        System.out.println("cNum = " + cNum);
//
//        var dNum = aNum != bNum;
//        System.out.println("dNum = " + dNum);
//
//        var cadenaA = "Hello";
//        var cadenaB = "bye bye";
//        var cVar = cadenaA == cadenaB;
//        System.out.println("cVar = " + cVar);
//
//        var fVar = cadenaA.equals(cadenaB);
//        System.out.println("fVar = " + fVar);
//
//        //Operadores relacionales
//        var gVar = aNum >= bNum; // != > >= < <= ==
//        System.out.println("gVar = " + gVar);
//
//        if (aNum % 2 == 0) {
//            System.out.println("El numero es par");
//        } else {
//            System.out.println("El numero es impar");
//        }
//
//        var edad = 15;
//        if (edad >= 18) {
//            System.out.println("Es mayor de edad");
//        } else {
//            System.out.println("Es menor de edad");
//        }
//        // Operadores condicionales: and y or
//
//        var valorA = 7;
//        var valorMinimo = 0;
//        var valorMaximo = 10;
//        var respuesta = valorA >= 0 && valorA < 10;
//
//        if (respuesta) {
//            System.out.println("Esta dentro del rango");
//        } else {
//            System.out.println("Esta fuera del rango");
//        }
//
//        var vacaciones = false;
//        var diaLibre = true;
//        if (vacaciones || diaLibre) {
//            System.out.println("Papa puede asistir al juego");
//        } else {
//            System.out.println("No puede asistir");
//        }
        //Operador ternario: expresiones sencillas
//        var resultadoT = (5 > 4) ? "Verdadero" : "Falso";
//        System.out.println("resultadoT = " + resultadoT);
//        
//        var numeroT = 7;
//        resultadoT = (numeroT % 2 == 0) ? "Par" : "Impar";
//        System.out.println("resultadoT = " + resultadoT);
        //Prioridad de los operadores
//        
//        var x = 5;
//        var y = 10;
//        var z = ++x + y--;
//        System.out.println("x = " + x);
//        System.out.println("y = " + y);
//        System.out.println("z = " + z);
//        
//        var solucionAritmetica = 4 + 5 * 6 / 3;
//        System.out.println("solucionAritmetica = " + solucionAritmetica);
//        
//        solucionAritmetica = (4+5) * 6 / 3;
//        System.out.println("solucionAritmetica = " + solucionAritmetica);
//        
    }
}
