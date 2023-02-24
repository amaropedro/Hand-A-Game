/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.hand.a.game;

import java.util.Arrays;

/**
 *
 * @author Amaro
 */
public class HandAGame {

    public static void main(String[] args) {
        User u = new User("Pedro", "8788990011", "pedro@email.com", "Petrolina", "1234", 1);
        
        if(Arrays.equals(u.getHashsenha(), u.hash("1234")) ){
            System.out.println("Login efetuado com sucesso");
        }
        else{
            System.out.println("Senha incorreta!");
        }
    }
}
