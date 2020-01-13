import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	      String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	      if (vaultDoor.checkPassword(input)) {
	         System.out.println("Access granted.");
	      } else {
	         System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm11g94a_u_4_mar34e");
    }
}

// j U 5 t _ a _ s n a _  3 l p m 1  1 g 9 4 a  _ u _ 4 _ m  a r 3 4  e
// 0       4     7     10         15         20           26       30 31
//
//buffer = jU5t_a_s1mpl3_an4gr4m_4_u_aa931e
//flag = picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_aa931e}
//
// [16] = 46-16 = 30 = 4
// [17] = g
// [18] = 46 - 18 = 28 = r
// [19] = 4
// [20] = 46 - 20 = 26 = m
// [21] = _
// [22] = 46 - 22 = 24 = 4
// [23] = _
// [24] = 46 - 24 = 22 = u
// [25] = _
// [26] = 46 - 26 = 20 = a
// [27] = a
// [28] = 46 - 28 = 18 = 9
// [29] = 3
// [30] = 46 - 30 = 16 = 1
// [31] = e
