package Operaciones;
public class Aritmetica {
 //Atributos de la clase
    int a, b;
   
    //El constructor es un metodo especial
    public Aritmetica(){ //Constructor 1 vacio
        System.out.println("Se esta ejecutando el constructor numero 1");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){ //Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el constructor numero 2 ");
    }
    
    //Metodo
    public void sumarNumeros(){
    int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    public int sumarConRetorno(){
        //int resultado = a + b;
        return this.a + this.b;
    }
    
    public int sumarConArgumentos(int a, int b){ //No modifica el valor de los atributos
        this.a = a; //El argumeto "a" se asigna al atributo this.a
        this.b = b;
        //return a + b;
        return this.sumarConRetorno(); //Se llama a un metodo desde otro metodo (Esto se debe hacer solo con metodos que esten dentro de una misma clase)
        
    }
    

}
