/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package handagame;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

/**
 *
 * @author Amaro
 */
public class DbObject implements DataBase{
    
    public void updateTables(String qry){
        try{
            Class.forName("org.postgresql.Driver");
            Connection con;
            con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/postgres", "postgres", "senha");
            Statement stm = con.createStatement();
            
            stm.executeUpdate(qry);           
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public ResultSet search(String qry){
        try{
            Class.forName("org.postgresql.Driver");
            Connection con;
            con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/postgres", "postgres", "senha");
            Statement stm = con.createStatement();
            
            ResultSet rs = stm.executeQuery(qry);          
            con.close();
            return  rs;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    @Override
    public void lookup(String qry, int max_atributes) {
        try{
            ResultSet rs = search(qry);
            while(rs.next()) {
                int i=1;
                while( i <= max_atributes){
                    System.out.print(rs.getString(i));
                    System.out.println();
                    i = i+1;
                }
            }
        }catch (Exception e) {
            e.printStackTrace();
        }
    }
}
