import java.util.Random;
import java.security.SecureRandom;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;


public class TokenGenerator2 {
    public static String generateAccessToken2(int length) {
        String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        SecureRandom secureRandom = new SecureRandom();
        StringBuilder token = new StringBuilder(length);

        for (int i = 0; i < length; i++) {
            token.append(characters.charAt(secureRandom.nextInt(characters.length())));
        }

        return token.toString();
    }

    public static void main(String[] args) {
        System.out.println("Token 2: " + generateAccessToken2(8));
    }
}




public class TokenGenerator3 {

    public static String[] generateAccessToken3(int tokenLength, int saltLength) throws NoSuchAlgorithmException {
        String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        SecureRandom secureRandom = new SecureRandom();
        StringBuilder token = new StringBuilder(tokenLength);
        StringBuilder salt = new StringBuilder(saltLength);

        // Generate salt
        for (int i = 0; i < saltLength; i++) {
            salt.append(characters.charAt(secureRandom.nextInt(characters.length())));
        }

        // Generate raw token
        for (int i = 0; i < tokenLength; i++) {
            token.append(characters.charAt(secureRandom.nextInt(characters.length())));
        }

        // Combine token and salt, then hash
        String combined = salt.toString() + token.toString();
        MessageDigest sha256 = MessageDigest.getInstance("SHA-256");
        byte[] hashedBytes = sha256.digest(combined.getBytes());
        String hashedToken = Base64.getEncoder().encodeToString(hashedBytes);

        return new String[]{hashedToken, salt.toString()};
    }

    public static void main(String[] args) throws NoSuchAlgorithmException {
        String[] result = generateAccessToken3(8, 8);
        System.out.println("Hashed Token: " + result[0]);
        System.out.println("Salt: " + result[1]);
    }
}
