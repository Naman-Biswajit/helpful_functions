import org.apache.commons.validator.routines.EmailValidator;

import java.text.MessageFormat;

/*
  needs following in pom/gradle
  <dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-text</artifactId>
    <version>1.4</version>
  </dependency>
 */
public class EmailUtil {
  public static void validateEmail(String email) {
    EmailValidator validator = EmailValidator.getInstance();
    if (!validator.isValid(email)) {
      throw new RuntimeException(MessageFormat.format("Invalid Email: {0}", email));
    }
  }
}

