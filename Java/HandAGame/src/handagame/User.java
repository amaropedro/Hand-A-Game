/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package handagame;

/**
 *
 * @author Amaro
 */
public class User extends DbObject{
    private String nome;
    private String contato;
    private String email;
    private String cidade;
    private String hashsenha;
    private int ID;

    public User(String nome, String contato, String email, String cidade, String senha,int ID) {
        this.nome = nome;
        this.contato = contato;
        this.email = email;
        this.cidade = cidade;
        this.ID = ID;
        this.hashsenha = senha;
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

    public String getHashsenha() {
        return hashsenha;
    }

    public void setHashsenha(String hashsenha) {
        this.hashsenha = hashsenha;
    }

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }
    
}
