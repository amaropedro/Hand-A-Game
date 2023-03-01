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
         
        User u = new User("Italo", "8788990011", "italo@email.com", "Petrolina", "xadrez", 3);
        
        if(Arrays.equals(u.getHashsenha(), u.hash("1234")) ){
            System.out.println("Login efetuado com sucesso");
        }
        else{
            System.out.println("Senha incorreta!");
        }
        
        try {
            String url = "jdbc:postgresql://localhost:5432/postgres";
            String usuario = "postgres";
            String senha = "senha";
            Class.forName("org.postgresql.Driver");
            Connection con;
            con = DriverManager.getConnection(url, usuario, senha);
            System.out.println("CONECTADO!");
            Statement stm = con.createStatement();
            ResultSet rs = stm.executeQuery("SELECT* FROM usuario");
            while(rs.next()) {
                System.out.print(rs.getString(1));
                System.out.println();
                System.out.print(rs.getString(2));
                System.out.println();
            }
            
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        } 
    }
}
