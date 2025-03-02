/**
 * @file TypeConversion.java
 * Interview Coding for Recruiting Point
 * 2014-06-10
 * @author Hai Vu
 */

package net.southeastwind.haivu;

/**
 * Given a String of digits (and possibly signs) such as "123", write a routine 
 * int stringToInteger( String s ) that converts the string to an integer, 
 * without using the built in Java functions that would do this. The code should
 * handle reasonable edge and error conditions gracefully. (You can rely on the
 * input being in base-10 representation - no need to worry about hex, octal, or
 * binary input.)
 */
public class TypeConversion {
    /**
     * Converts a string of digits to integer.
     * @param s The string which contains digits to convert
     * @return An integer presentation of for the input string
     * @exception NumberFormatException if the string represents an invalid
     * number
     */
    public static int stringToInteger(String s) {
        if (s.isEmpty()) { throw new NumberFormatException("Empty string"); }
        
        int result = 0; // The result of the conversion
        int sign = 0;   // sign = 0: no sign, 1: + sign found, -1: - sign found

        // Loop through the string and convert digit by digit
        // for (int i = 0; i < s.length(); i++) {
        //     char c = s.charAt(i);
        for (char c: s.toCharArray()) {
            if ('0' <= c && c <= '9') {
                // A digit, process it
                result = result * 10 + (c - '0');
            } else if (c == '-' && sign == 0) {
                // See a minus sign for the first time
                sign = -1;
            } else if (c == '+' && sign == 0) {
                // See a plus sign for the first time
                sign = 1;
            } else {
                // Everything else is invalid character, bark!
                throw new NumberFormatException("Invalid number: " + s);
            }
        }
        if (sign != 0) { result *= sign; }
        return result;
    }
}
