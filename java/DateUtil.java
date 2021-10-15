import org.joda.time.DateTime;

public class DateUtil {
  /**
   * Helper method to check if a date falls between 2 dates. This is not a default for DateTime
   * nor is it in the other date utils, so I decided to make my own.
   *
   * This is also range exclusive, so be careful.
   */
  public static boolean isBetween(DateTime initialDate, DateTime startDate, DateTime endDate) {
    return initialDate != null
               && initialDate.isAfter(startDate)
               && initialDate.isBefore(endDate);
  }
}

