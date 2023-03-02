/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package handagame;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Arrays;

/**
 *
 * @author Amaro
 */
public class HandAGame {

    public static void main(String[] args) {
        
        //User u1 = new User("Pedro", "879 8855-4459", "pedro.amaro@email.com", "Petrolina", "1234", 1);
        User u2 = new User("José", "87977665544", "jose.dias@email.com", "Petrolina", "minhasenha", 4);
        //User u3 = new User("Italo", "(87) 98866-5544", "italo@email.com", "Petrolina", "xadrez", 2);
        
        
        
        //DbObject o = new DbObject();
        
        //o.lookup("SELECT* FROM usuario", 6);
        
        Sistema s = new Sistema();
        
        s.login("José", "minhasenha");
        System.out.println("-----");
        System.out.println(u2.getHashsenha());
    }
}
