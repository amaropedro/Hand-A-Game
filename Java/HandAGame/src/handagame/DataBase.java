/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package handagame;
import java.sql.Statement;
import java.sql.Connection;
import java.sql.DriverManager; 

/**
 *
 * @author Amaro
 */
public class DataBase {
  
    public static void main(String[] args) {
    // TODO code application logic here
        try {
            String url = "jdbc:postgresql://localhost:5432/postegres";
            String usuario = "postgres";
            String senha = "senha";
            Class.forName("org.postgresql.Driver");
            Connection con;
            con = DriverManager.getConnection(url, usuario, senha);
            System.out.println("Conexão realizada com sucesso.");
            Statement stm = con.createStatement();
            stm.executeQuery("Show tables");
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        } 
    }
}


    


