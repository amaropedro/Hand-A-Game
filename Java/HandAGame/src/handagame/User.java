/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package handagame;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
 *
 * @author Amaro
 */
public class User {
    private String nome;
    private String contato;
    private String email;
    private String cidade;
    private byte[] hashsenha;
    private int ID;

    public User(String nome, String contato, String email, String cidade, String senha,int ID) {
        this.nome = nome;
        this.contato = contato;
        this.email = email;
        this.cidade = cidade;
        this.ID = ID;
        this.hashsenha = hash(senha);
    }
    
    //Deve ser uma classe separada no futuro. 
    //Essa função de hash não é das mais seguras, entretanto, para o escopo do projeto basta.
    public byte[] hash(String senha){
        try{
            MessageDigest md = MessageDigest.getInstance("SHA-512");
            byte[] hashedPassword = md.digest(senha.getBytes(StandardCharsets.UTF_8));
            return hashedPassword;
        }
        
        catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
    
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getContato() {
        return contato;
    }

    public void setContato(String contato) {
        this.contato = contato;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    public byte[] getHashsenha() {
        return hashsenha;
    }

    public void setHashsenha(byte[] hashsenha) {
        this.hashsenha = hashsenha;
    }

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }
    
}
