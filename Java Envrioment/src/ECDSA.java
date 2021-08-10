import java.math.BigInteger;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.SecureRandom;
import java.security.Signature;
import java.security.spec.ECGenParameterSpec;

public class ECDSA {
  public static void main(String[] args) throws Exception {
    KeyPairGenerator keyGen = KeyPairGenerator.getInstance("EC");

    keyGen.initialize(new ECGenParameterSpec("secp256r1"), new SecureRandom());

    KeyPair pair = keyGen.generateKeyPair();
    PrivateKey priv = pair.getPrivate();
    PublicKey pub = pair.getPublic();

    System.out.println(pub);

    Signature ecdsa = Signature.getInstance("SHA256withECDSA");

    ecdsa.initSign(priv);
    String str = "This is string to sign";
    byte[] strByte = str.getBytes("UTF-8");
    ecdsa.update(strByte);
    byte[] realSig = ecdsa.sign();
    System.out.println("Signature: " + new BigInteger(1, realSig).toString(16));

    ecdsa.initVerify(pub);
    ecdsa.update(strByte);
    Boolean result = ecdsa.verify(realSig);
    System.out.println(result);
  }
}
