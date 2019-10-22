public class QueryStringParser {
    //  VERY BASIC
    //  this is parsing out a query string. Example:
    //  id=1234&username=gill@bates.com
    //  into {id: 1234, username: gill@bates.com}
    public static Map<String, String> buildParameterMap(String queryString) {
      return Arrays.stream(queryString.split("&"))
          .map(e -> e.split("="))
          .filter(e -> e.length > 1)
          .collect(Collectors.toMap(e -> e[0], e -> urlDecode(e[1])));
    }

    private static String urlDecode(String value) {
      try {
        return URLDecoder.decode(value, StandardCharsets.UTF_8.name());
      } catch (UnsupportedEncodingException ex) {
        ex.printStackTrace();
        return "";
      }
    }
  }
