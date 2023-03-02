/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package handagame;

/**
 *
 * @author Amaro
 */
public class HandAGame {

    public static void main(String[] args) {
        //Cadastrando usuarios com o Padrão Builder
        CadastroUsuario U = new CadastroUsuario();
        
        U.setNome("Italo");
        U.setSenha("xadres", "xadres");
        U.setCidade("Petrolina");
        U.setContato("(87) 9 8800-4433");
        U.setEmail("italo.tenorio@email.com");
        U.efetuarCadastro();

        System.out.println("");
        System.out.println("---------");
        //Fazendo diferentes consultas ao BD com o Padrão Strategy
        DbObject o = new DbObject();
        
        o.lookup("SELECT* FROM usuario", 6);
        
        System.out.println("");
        System.out.println("---------");
        //Fazendo Login
        Sistema s = new Sistema();
        s.login("Pedro", "minhasenha");
        s.login("Pedro", "123");
        s.login("Italo", "xadres");
    }
}
