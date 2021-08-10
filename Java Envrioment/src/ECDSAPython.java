import java.security.KeyFactory;
import java.security.Signature;
import java.security.interfaces.ECPublicKey;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;

public class ECDSAPython {
  public static void main(String[] args) throws Exception {
    String ecdsaVerifyString = "MEYCIQDZ2kRO+K6HuGP258bt7ttfQqNikxH8NpGS5ZCLBgU6AAIhALN/p/KA7Z1o3JC6d22KFLgpavF/u3WJE3QjlrbH304n";

    KeyFactory keyFactory = KeyFactory.getInstance("EC");
    Signature ecdsa = Signature.getInstance("SHA256withECDSA");

    String publicKeyPEM = "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAELDIqPmr5Oxklns5GgKTLrxfS0WcKIjaCCW2ZsjBpwxcnQAItqUKSh5GCfj0tW6jVm4adiCCAKIDOBWhvIYqZ1Q==";
    byte[] encoded = Base64.getDecoder().decode(publicKeyPEM);
    X509EncodedKeySpec keySpec = new X509EncodedKeySpec(encoded);
    ECPublicKey publicKey = (ECPublicKey) keyFactory.generatePublic(keySpec);

    ecdsa.initVerify(publicKey);

    String url = "https://www.theguardian.com/uk-news/2021/jul/24/uk-weather-lightning-strikes-homes-in-hampshire-as-country-hit-by-storms";
    ecdsa.update(url.getBytes("UTF-8"));
    Boolean result = ecdsa.verify(Base64.getDecoder().decode(ecdsaVerifyString));
    System.out.println(result);
  }
}
