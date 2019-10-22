public class Util {
    public static <T> Stream<T> convertGenericToStream(Collection<?> items, Class<T> clazz) {
      return items.stream()
          .map(o -> {
            try {
              return clazz.cast(o);
            } catch (ClassCastException e) {
              return null;
            }
          })
          .filter(Objects::nonNull);
    }
  }
