export default {
  get (key, defaultValue) {
    if (typeof window === 'undefined') {
      return defaultValue;
    }
    const value = localStorage.getItem(key);
    return (value && typeof value === 'string' ? JSON.parse(value) : defaultValue) || defaultValue;
  },

  set (key, value) {
    if (typeof window !== 'undefined') {
      localStorage.setItem(key, JSON.stringify(value));
    }
  },
};
