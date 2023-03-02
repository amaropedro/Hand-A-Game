/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package handagame;
import utils.Hash;
import java.sql.ResultSet;
/**
 *
 * @author Amaro
 */
public class CadastroUsuario extends DbObject implements InterfaceCadastro{
    //Segue o padrão Builder
    
    private String nome;
    private String contato;
    private String email;
    private String cidade;
    private String senha;
    private int ID;
    
    
    @Override
    public void setNome(String nome) {
        String qry = "SELECT nome FROM usuario WHERE nome ='" + nome + "'";
        ResultSet rs = search(qry);
        try{
            if(!rs.isBeforeFirst()){
                this.nome = nome;
            }
            else{
                System.out.println("Nome de usuario indisponivel!");
            }
        }catch (Exception e) {
            e.printStackTrace();
        } 
    }

    @Override
    public void setSenha(String senha, String confirmarSenha) {
        if (senha.equals(confirmarSenha)){
            this.senha = Hash.hash(senha);
        }
    }

    @Override
    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    @Override
    public void setContato(String contato) {
       this.contato = contato;
    }

    @Override
    public void setID() {
        this.ID = count()+1;
    }
    
    public User efetuarCadastro(){
        if(nome!=null && contato!=null && email!=null && cidade!=null && senha!=null ){
            setID();
            String qry = "INSERT INTO usuario values ('" + String.valueOf(this.ID) + "', '"+ this.nome + "', '" + this.contato + "', '" + this.cidade + "', '" + this.email + "', '" + this.senha +"')";
            updateTables(qry);
            return new User(nome, contato, email, cidade, senha, ID);
        }else{
            System.out.println("CAMPOS INCORRETOS OU NÃO PREENCHIDOS");
        }
        return null;
    }
}
