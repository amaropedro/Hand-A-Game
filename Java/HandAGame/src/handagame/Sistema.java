/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package handagame;

import java.sql.ResultSet;
import utils.Hash;

/**
 *
 * @author Amaro
 */
public class Sistema extends DbObject{
    
    public void login(String nome, String senha){
        try{
            ResultSet rs = search("SELECT nome, hashsenha FROM usuario WHERE nome ='" + nome +"'");
            while(rs.next()) {                
                if(rs.getString(2).equals(Hash.hash(senha))){
                    System.out.println("Login efetuado com sucesso");
                }
                else{
                    System.out.println("Usuário ou Senha incorretos!");
                }
            }
        }catch (Exception e) {
            e.printStackTrace();
        } 
    }
}
