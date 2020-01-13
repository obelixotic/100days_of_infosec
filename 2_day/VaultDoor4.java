import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
  // System.out.println(input);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
    //
    //  .:::.   .:::.
    // :::::::.:::::::
    // :::::::::::::::
    // ':::::::::::::'
    //   ':::::::::'
    //     ':::::'
    //       ':'
    // -Minion #7781
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 070 , 060 ,
            'f' , '8' , 'e' , '1' , 'e' , '0' , '4' , '7' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
}

//106 j
//85 U
//53 5
//116 t
//95 _
//52 4
//95 _
//98 b
//0x55 U
//0x6e n
//0x43 C
//0x68 h
//0x5f _
//0x30 0
//0x66 f
//0x5f _
//0142 b
//0131 Y
//0164 t
//063 3
//0163 s
//0137 _
//070 8
//060 0
//picoCTF{jU5t_4_bUnCh_0f_bYt3s_80f8e1e047}
