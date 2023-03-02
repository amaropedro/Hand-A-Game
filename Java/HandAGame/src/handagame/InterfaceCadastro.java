/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Interface.java to edit this template
 */
package handagame;

/**
 *
 * @author Amaro
 */
public interface InterfaceCadastro {
    //Segue o padrão Builder
    
    void setNome(String nome);
    void setSenha(String senha, String confirmarSenha);
    void setEmail(String email);
    void setCidade(String cidade);
    void setContato(String contato);
    void setID();
}
